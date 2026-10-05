from pathlib import Path

RAW_PATH = Path("data/raw/myscheme_kcc_2026-10-03.txt")
OUT_PATH = Path("data/processed/myscheme_kcc_2026-10-03.txt")

# (wrong, right). Every pair here must also be a row in docs/audit.md.
FIXES = [
    ("availableat", "available at"),
    ("andfacilitate", "and facilitate"),
    ("authentication),debit", "authentication), debit"),
    ("20%of", "20% of"),
    ("cashcredit", "cash credit"),
    ("website ofthe", "website of the"),
]


def clean_text(text):
    # Rule 1: remove invisible BOM characters anywhere in the text
    text = text.replace("\ufeff", "")

    # Rule 2: fix joined words
    for wrong, right in FIXES:
        text = text.replace(wrong, right)

    return text


raw_text = RAW_PATH.read_text(encoding="utf-8")
cleaned_text = clean_text(raw_text)

# Verify: every rule should show a count before and 0 after
print("BOM characters:", raw_text.count("\ufeff"), "->", cleaned_text.count("\ufeff"))
for wrong, right in FIXES:
    print(f"{wrong!r}: {raw_text.count(wrong)} -> {cleaned_text.count(wrong)}")

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUT_PATH.write_text(cleaned_text, encoding="utf-8")
print("Saved to", OUT_PATH)