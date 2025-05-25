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

## Tools Included

### 1. `merge_po.py` (Python)
A tool to merge updated Russian `.po` files with the current English translation, preserving all existing English translations and adding any new Russian entries.

**Usage:**
```bash
python merger.po
```

**Features:**
- Preserves all existing English translations
- Adds new English `.po` strings to alrady existing Russian `.po` to reduce amount of translation needed

### 2. `po_translator_gpt3.5` (Python)
Uses chat GPT 3.5 Turbo to translate Russian exclusively lines. Program will ignore English lines itself

**Usage:**
```bash
python po_translator_gpt3.5
```

**Features:**
- Splits one `.po` into `n` smaller files
- Puts fragmented strings into batches to speed up the translation speed
- Saving your time by reducing amount of Russian text you have to translate :)


---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/LocalizedTanki/Tanki-L10n-EN.git
   cd Tanki-L10n-EN
   ```
2. **Install dependencies**
   - Requires Python 3
   - Install `polib` for Python:
     ```bash
     pip install polib
     ```
3. **Use the tools**
   - All tools are located in the `tools/` directory. Run as shown in the usage examples above.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork this repository
2. Create a new branch for your feature or fix
3. Submit a pull request with a clear description

Please follow existing code style and add docstrings/comments if you add or modify a  tool.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

For questions, open an issue at [https://github.com/LocalizedTanki/Tanki-L10n-EN/issues](https://github.com/LocalizedTanki/Tanki-L10n-EN/issues)

---
