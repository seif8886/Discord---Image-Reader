### Installation
- Install tesseract https://sourceforge.net/projects/tesseract-ocr-alt/files/
- validate tesseract path on `/imagereader.py` -> `path_to_tesseract variable`.
- pip install -r requirements.txt
- validate your discord bot token from `.env` & run `main.py`.

### Usage

- Add a new argument via `/agenda_messages.json`
- message formula: 

```py
    "found_issue_name": {
        "keywords": ["keyword1", "keyword2"],
        "regex": "[a-z]", # leave blank if none.
        "reply_message": "reply message here",
        "alt_message": "alt_issue_name" # leave blank if none
    }
```

- for regex statements https://regex101.com/ can be used.
  - e.g. expression: `[oO0]x..3C91CC`
  - test string: ```Offset = Ox003C91CC```