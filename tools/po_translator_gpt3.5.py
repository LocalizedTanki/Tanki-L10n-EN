import os
import re
import polib
import openai
from send2trash import send2trash
from tqdm import tqdm
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # For consistent language detection

# === CONFIG ===
OPENAI_MODEL = "gpt-3.5-turbo"
BATCH_SIZE = 50 #higher values than it will result in the errors in the entire file
INPUT_FOLDER = "input"
OUTPUT_FOLDER = "translated"
# ==============

def mask_placeholders(text):
    PLACEHOLDER_PATTERN = re.compile(r"%\([^)]+\)[sd]|%[sd]|\{[^}]+\}")
    text = text.replace('\n', '\\n')  # Escape real line breaks as literal "\n"
    placeholders = PLACEHOLDER_PATTERN.findall(text)
    mapping = {}
    masked = text
    for idx, ph in enumerate(placeholders):
        token = f"<<PH_{idx}>>"
        mapping[token] = ph
        masked = masked.replace(ph, token)
    return masked, mapping

def unmask_placeholders(text, mapping):
    for token, ph in mapping.items():
        token_id = re.findall(r"\d+", token)[0]
        possible_patterns = [
            re.escape(token),                   
            re.escape(token.replace("<<", "[[").replace(">>", "]]")),
            rf"\(PH_{token_id}\)",              
            rf"\[PH_{token_id}\]",              
            rf"PH_{token_id}",                  
            rf"%\(PH_{token_id}\)[sd]?",        
        ]
        for pat in possible_patterns:
            text = re.sub(pat, ph, text)
    text = text.replace('\\n', '\n')
    text = re.sub(r"[\[\(<%]*PH_\d+[\]\)>d%s]*", "", text)
    return text

def get_language_name(text):
    try:
        lang_code = detect(text)
        if lang_code == "ru":
            return "Russian"
        if lang_code in ("zh-cn", "zh-tw", "zh"):
            return "Chinese"
        if lang_code == "en":
            return "English"
        return "Unknown"
    except Exception:
        return "Unknown"

def translate_batch(batch, client):
    masked_batch = []
    all_mappings = []
    lang_set = set()
    for text in batch:
        masked, mapping = mask_placeholders(text)
        masked_batch.append(masked)
        all_mappings.append(mapping)
        lang_set.add(get_language_name(text))

    if "Russian" in lang_set:
        src_lang = "Russian"
    elif "Chinese" in lang_set:
        src_lang = "Chinese"
    else:
        src_lang = "source language"

    batch_text = "\n".join(f"{i+1}. {line}" for i, line in enumerate(masked_batch))
    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": (
                f"You are a professional video game localization specialist working on World of Tanks. "
                f"Translate these {src_lang} interface strings into clear, natural English for the game World of Tanks. "
                "Use proper and established World of Tanks in-game terminology. "
                "Be concise, prefer official wording, and preserve formatting.\n"
                "NEVER change or touch placeholders like %(foo), %s, %d, {foo}, <<PH_0>>. "
                "Return ONLY the translations, in the same order, numbered as in input, nothing else."
            )},
            {"role": "user", "content": batch_text}
        ],
        temperature=0.1,
    )
    output_lines = resp.choices[0].message.content.strip().split('\n')
    translations = []
    for line, mapping in zip(output_lines, all_mappings):
        line = line.strip()
        line = re.sub(r"^\d+\.\s*", "", line)
        translations.append(unmask_placeholders(line, mapping))
    return translations

def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False

def translate_po_file(input_path, output_path, client):
    po = polib.pofile(input_path)
    entries_to_translate = []
    indexes_to_translate = []

    # Identify which entries need translation (non-English)
    for idx, entry in enumerate(po):
        if entry.msgstr and entry.msgstr != entry.msgid:
            if not is_english(entry.msgstr):
                entries_to_translate.append(entry)
                indexes_to_translate.append(idx)

    if not entries_to_translate:
        print(f"No strings to translate in {input_path}")
        po.save(output_path)
        return

    translations = []
    for i in tqdm(range(0, len(entries_to_translate), BATCH_SIZE),
                  desc=f"Translating '{os.path.basename(input_path)}' (batches of {BATCH_SIZE})"):
        batch = [entry.msgstr for entry in entries_to_translate[i:i+BATCH_SIZE]]
        batch_translations = translate_batch(batch, client)
        translations.extend(batch_translations)

    # Assign translations back only to entries that were translated
    for idx, translated in zip(indexes_to_translate, translations):
        if translated:
            po[idx].msgstr = translated

    po.save(output_path)
    print(f"✅ Saved: {output_path}")

def main():
    input_folder = INPUT_FOLDER
    out_folder = OUTPUT_FOLDER

    # Always create both folders, even if they already exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(out_folder, exist_ok=True)

    # Load API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        try:
            with open('key.txt', 'r', encoding='utf-8') as f:
                api_key = f.read().strip()
        except FileNotFoundError:
            print("❌ ERROR: Set OPENAI_API_KEY env var or provide key.txt file.")
            exit(1)
    client = openai.OpenAI(api_key=api_key)

    po_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.po')]
    if not po_files:
        print("❌ No .po files found in the input folder.")
        exit(1)

    for po_file in po_files:
        input_path = os.path.join(input_folder, po_file)
        output_path = os.path.join(out_folder, po_file)

        if os.path.exists(output_path):
            print(f"⚠️ Skipping '{po_file}' — already exists in 'translated/'")
            continue

        print(f"--- Processing: {po_file} ---")
        try:
            translate_po_file(input_path, output_path, client)
        except Exception as e:
            print(f"❌ Failed to translate {po_file}: {e}")
            continue

        # Optional: Move original to Recycle Bin
        try:
            send2trash(input_path)
            print(f"🗑️ Moved to Recycle Bin: {input_path}")
        except Exception as e:
            print(f"⚠️ Failed to move to Recycle Bin: {e}")

    print("\n🎉 All files processed!")

if __name__ == '__main__':
    main()
