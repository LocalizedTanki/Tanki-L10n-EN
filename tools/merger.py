import polib
from langdetect import detect, DetectorFactory
import os
from shutil import copyfile

DetectorFactory.seed = 0

def detect_po_language(po_file, sample_size=10):
    po = polib.pofile(po_file)
    texts = [entry.msgstr for entry in po if entry.msgstr.strip()]
    sample_texts = texts[:sample_size]
    langs = []
    for text in sample_texts:
        try:
            langs.append(detect(text))
        except:
            continue
    if langs:
        return max(set(langs), key=langs.count)
    return 'unknown'

# Directories
en_dir = "en"
ru_dir = "ru"
merged_dir = "merged"

# Ensure folders exist
for folder in [en_dir, ru_dir, merged_dir]:
    os.makedirs(folder, exist_ok=True)

# Get all PO filenames from both folders
ru_files = {f for f in os.listdir(ru_dir) if f.endswith('.po')}
en_files = {f for f in os.listdir(en_dir) if f.endswith('.po')}

# Only process files that exist in Russian
for ru_filename in sorted(ru_files):
    ru_path = os.path.join(ru_dir, ru_filename)
    en_path = os.path.join(en_dir, ru_filename)
    merged_path = os.path.join(merged_dir, ru_filename)

    if os.path.isfile(en_path):
        # Merge if English file exists
        ru_lang = detect_po_language(ru_path)
        en_lang = detect_po_language(en_path)
        if ru_lang != "ru" or en_lang != "en":
            print(f"Warning: Detected {ru_lang} for {ru_filename} (ru) and {en_lang} for {ru_filename} (en)")

        ru_po = polib.pofile(ru_path)
        en_po = polib.pofile(en_path)
        en_map = {entry.msgid: entry.msgstr for entry in en_po}

        replaced = 0
        for entry in ru_po:
            if entry.msgid in en_map:
                if entry.msgstr != en_map[entry.msgid]:
                    entry.msgstr = en_map[entry.msgid]
                    replaced += 1
        ru_po.save(merged_path)
        print(f"{ru_filename}: Merged, replaced {replaced} entries.")

    else:
        # No English file, just copy Russian file as-is
        copyfile(ru_path, merged_path)
        print(f"{ru_filename}: English version of the file not found. Copied Russian file as-is.")

# Optionally, warn about English files that don't have a Russian original
for en_filename in sorted(en_files - ru_files):
    print(f"{en_filename}: Russian version of the file not found. Skipped, no file saved in merged.")

print("Done! All merged files saved in 'merged' folder.")
