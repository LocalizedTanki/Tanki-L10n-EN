# Tanki-L10n-EN

**English Localization Project for Mir Tankov**

This repository contains:
- English and Russian `.po` translation files for Mir Tankov / World of Tanks
- Tools/scripts for managing, merging, and splitting `.po` files
- Documentation and contribution instructions

---

## Repository Structure

- `ru-current.po` – Original Russian translation file
- `all-translations.po` – Main English translation file (merged)
- `Decompiled_PO_Mixed/` – Decompiled `.po` files extracted from the game client
- `tools/` – Python scripts and utilities for translation management

---

## External Tools

### 🔗 [PO_AI_Translate](https://github.com/GtafanWRLD/PO_AI_Translate)
A Python-based tool uses OpenAI's GPT-3.5 API to automatically translate `.po` files to other languages.

**Features:**
- Skips strings already in English or empty
- Preserves placeholders and formatting (`\n`, `%d`, `{0}`, etc.)
- Parallel batch processing for faster translation

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

Contributions are welcome! Open a pull request if you wanna contribute.

---

## License

This project is licensed under the MIT License.

---
