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
python merge_po.py ru-current.po all-translations.po -o merged.po
```

**Features:**
- Preserves all existing English translations
- Adds new strings from Russian `.po` to English `.po`
- Outputs a fully merged file for translation

### 2. `po_splitter.py` (Python)
Splits a large `.po` file into multiple smaller `.po` files for collaborative translation work.

**Usage:**
```bash
python po_splitter.py all-translations.po -n 5
```

**Features:**
- Splits one `.po` into `n` smaller files
- Useful for distributing translation work

### 3. `po_combiner.py` (Python)
Combines several split `.po` files back into a single file, ready for testing or use in-game.

**Usage:**
```bash
python po_combiner.py split1.po split2.po split3.po -o combined.po
```

**Features:**
- Merges multiple `.po` files
- Maintains consistent formatting

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

Please follow existing code style and add docstrings/comments if you add a new tool.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

For questions, open an issue at [https://github.com/LocalizedTanki/Tanki-L10n-EN/issues](https://github.com/LocalizedTanki/Tanki-L10n-EN/issues)

---
