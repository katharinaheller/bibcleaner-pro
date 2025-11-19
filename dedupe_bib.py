## Robust BibTeX dedupe with logging
from pathlib import Path
import re

input_file = Path("references.bib")            # input file
output_file = Path("references_cleaned.bib")   # output file
log_file = Path("dedupe.log")                  # log file

# Patterns for fields
DOI_PATTERN = re.compile(r"doi\s*=\s*[{\"]([^}\"{]+)[\"}]", re.IGNORECASE)
TITLE_PATTERN = re.compile(r"title\s*=\s*[{\"]([^}\"{]+)[\"}]", re.IGNORECASE)
URL_PATTERN = re.compile(r"url\s*=\s*[{\"]([^}\"{]+)[\"}]", re.IGNORECASE)

# --- Robust BibTeX entry reader (brace counter) ---
def read_entries(text: str):
    entries = []
    pos = 0
    n = len(text)

    while True:
        start = text.find("@", pos)
        if start == -1:
            break

        # Find first "{"
        brace_start = text.find("{", start)
        if brace_start == -1:
            break

        # Walk forward until braces match
        depth = 0
        i = brace_start
        while i < n:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    entries.append(text[start:end])
                    pos = end
                    break
            i += 1

        # If something broke, stop reading
        if depth != 0:
            break

    return entries


# Helper to extract fields safely
def extract(pattern, entry):
    m = pattern.search(entry)
    return m.group(1).strip().lower() if m else ""


# Load file
text = input_file.read_text(encoding="utf-8")
entries = read_entries(text)

seen = set()
unique = []
log = []

for entry in entries:
    doi = extract(DOI_PATTERN, entry)
    title = extract(TITLE_PATTERN, entry)
    url = extract(URL_PATTERN, entry)

    key = (doi, title, url)

    if key not in seen:
        seen.add(key)
        unique.append(entry)
    else:
        log.append(f"Duplicate removed:\n---\n{entry}\n---\nKey={key}\n")

# Write cleaned file
output_file.write_text("\n\n".join(unique), encoding="utf-8")

# Write log file
log_file.write_text("\n".join(log), encoding="utf-8")

print(f"Done. Clean file -> {output_file}")
print(f"Log written to -> {log_file}")
