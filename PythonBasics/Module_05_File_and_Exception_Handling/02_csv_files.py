"""
Module 5 — FILE HANDLING AND EXCEPTION HANDLING
Feature: CSV Files — csv.reader(), csv.writer()

Underlying concepts
- CSV = comma-separated values. The csv module handles quoting, commas
  inside fields, and newlines. Do not split on ',' yourself.
- Always open with newline="" (csv docs) so Windows extra blank lines
  are not created.
- csv.reader yields lists of strings. Numbers come back as strings.
- csv.writer / writerow / writerows. DictWriter / DictReader use headers.
- Dialect / delimiter: ',' default, but tabs and ';' also exist.
"""

import csv
from pathlib import Path

CSV_PATH = Path(__file__).with_name("students.csv")
EMPTY_PATH = Path(__file__).with_name("empty.csv")
TSV_PATH = Path(__file__).with_name("students.tsv")


print("=" * 60)
print("EXAMPLE 1 — csv.writer / csv.reader")
print("=" * 60)

rows = [
    ["name", "module", "score"],
    ["Amrita", 5, 91],
    ["Riya", 5, 88],
    ["Aman", 5, 76],
    ["Note, comma", 5, 70],   # comma in field — csv will quote it
]
with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(rows[0])
    writer.writerows(rows[1:])
print("wrote", CSV_PATH.name)

print("--- csv.reader (all values are str) ---")
with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)


print("\n" + "=" * 60)
print("EXAMPLE 2 — DictWriter / DictReader, type conversion")
print("=" * 60)

extra = [
    {"name": "Neha", "module": 5, "score": 95},
    {"name": "Vikram", "module": 5, "score": 80},
]
with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "module", "score"])
    writer.writerows(extra)

print("--- DictReader ---")
with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("fieldnames:", reader.fieldnames)
    for row in reader:
        score = int(row["score"])          # convert yourself
        print(f"  {row['name']:12} module={row['module']} score={score}")


print("\n" + "=" * 60)
print("EXAMPLE 3 — extrasaction, missing keys, empty file")
print("=" * 60)

# extrasaction='raise' (default) if the dict has unknown keys
try:
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name", "module", "score"])
        w.writerow({"name": "X", "module": 1, "score": 1, "extra": "nope"})
except ValueError as extra_err:
    print("unknown dict key:", extra_err)

EMPTY_PATH.write_text("", encoding="utf-8")
with open(EMPTY_PATH, "r", newline="", encoding="utf-8") as f:
    print("empty file rows:", list(csv.reader(f)))


print("\n" + "=" * 60)
print("EXAMPLE 4 — delimiter / quoting")
print("=" * 60)

with open(TSV_PATH, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
    w.writerow(["name", "city"])
    w.writerow(["Amrita", "New Delhi"])

with open(TSV_PATH, "r", newline="", encoding="utf-8") as f:
    print("tab reader:", list(csv.reader(f, delimiter="\t")))


print("\n" + "=" * 60)
print("EXAMPLE 5 — skip header with next(), restcheck")
print("=" * 60)

with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("header:", header)
    rest = list(reader)
    print("data rows:", len(rest))
    print("quoted comma field survived:", rest[3][0] if len(rest) > 3 else rest)


if __name__ == "__main__":
    print("\nCSV files demo complete.")
