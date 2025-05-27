# Tanki-L10n-EN

**English Localization Project for Mir Tankov**

This repository contains:
- English  `.po` translation files for Mir Tankov
- Tools/scripts for managing, merging, splitting and translating `.po` files

---

## External Tools To Translate

### 🔗 [PO_AI_Translate](https://github.com/GtafanWRLD/PO_AI_Translate)
A Python-based tool uses OpenAI's GPT-3.5 API to automatically translate `.po` files to other languages.

**Features:**
- Skips strings already in English or empty
- Preserves placeholders and formatting (`\n`, `%d`, `{0}`, etc.)
- Batch processing for faster translation

---

### 🔗 [PO_En_Ru_Merger](https://github.com/GtafanWRLD/PO_En_Ru_Merger)
A utility to merge English and Russian `.po` files efficiently.

**Features:**
- Replaces Russian `msgstr` with counterparts in other languages.
- Useful for syncing updated files to have less work.

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/LocalizedTanki/Tanki-L10n-EN.git
   cd Tanki-L10n-EN
   ```

2. **Install dependencies**
   ```bash
   pip install polib openai tqdm langdetect
   ```

3. **Place `.po` files in `input/` and run your tool of choice.**

---

## Contributing

Contributions are welcome! Open a pull request if you wanna contribute. You can edit .po files which have wrong translations. Feel free to fork the repo to translate the repo to different languages!

---

## License

This project is licensed under the MIT License.

---
