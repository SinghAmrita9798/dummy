"""
Module 5 — FILE HANDLING AND EXCEPTION HANDLING
Feature: File Modes — Read ('r'), write ('w'), append ('a'), functions

Underlying concepts
- Always use `with open(...)` so the file is closed even if an error occurs.
- Text mode ('t', default) needs an encoding. Prefer encoding='utf-8'.
- 'w' truncates (erases) an existing file. 'a' never truncates. 'x' fails if
  the path already exists. 'r' fails if the path is missing.
- read() / readline() / readlines() / iterate the file object.
- After read() the cursor is at EOF; a second read() returns ''.
- Binary modes ('rb', 'wb') are for non-text (images, pdf). No encoding=.
"""

from pathlib import Path

NOTES = Path(__file__).with_name("sample_notes.txt")
MISSING = Path(__file__).with_name("does_not_exist.txt")


print("=" * 60)
print("EXAMPLE 1 — 'w' write (overwrite) and 'a' append")
print("=" * 60)

with open(NOTES, "w", encoding="utf-8") as f:
    n = f.write("Python file handling\n")
    f.write("Mode w overwrites existing content.\n")
    print("write() returns character count:", n)
print("wrote", NOTES.name)

with open(NOTES, "a", encoding="utf-8") as f:
    f.write("Mode a appends this extra line.\n")
print("appended a line")


print("\n" + "=" * 60)
print("EXAMPLE 2 — 'r' read, cursor, line helpers")
print("=" * 60)

with open(NOTES, "r", encoding="utf-8") as f:
    content = f.read()
    print("second read at EOF is empty:", repr(f.read()))
print("--- full content ---")
print(content, end="")

with open(NOTES, "r", encoding="utf-8") as f:
    print("readline 1:", repr(f.readline()))
    print("readlines rest:", [ln.rstrip("\n") for ln in f.readlines()])

print("line-by-line (best for large files):")
with open(NOTES, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"  {i}: {line.rstrip()}")


print("\n" + "=" * 60)
print("EXAMPLE 3 — missing file, 'x' exclusive create")
print("=" * 60)

try:
    open(MISSING, "r", encoding="utf-8")
except FileNotFoundError as extra:
    print("'r' missing file:", extra)

try:
    with open(NOTES, "x", encoding="utf-8") as f:
        f.write("should not happen")
except FileExistsError as extra:
    print("'x' when file exists:", extra)


print("\n" + "=" * 60)
print("EXAMPLE 4 — seek/tell, pathlib extras, encoding")
print("=" * 60)

with open(NOTES, "r", encoding="utf-8") as f:
    print("tell start:", f.tell())
    f.read(6)
    print("tell after 6 chars:", f.tell())
    f.seek(0)
    print("after seek(0):", f.readline().rstrip())

print("exists / size:", NOTES.exists(), NOTES.stat().st_size, "bytes")
print("Path.read_text shortcut:\n", NOTES.read_text(encoding="utf-8"), end="")

# encoding matters: writing bytes that are not valid utf-8 will fail in text mode
try:
    Path(__file__).with_name("bad.txt").write_text("ok", encoding="utf-8")
except OSError:
    pass


print("\n" + "=" * 60)
print("EXAMPLE 5 — binary vs text; why with matters")
print("=" * 60)

blob = Path(__file__).with_name("sample.bin")
with open(blob, "wb") as f:
    f.write(b"\x00\x01\xffhello")
with open(blob, "rb") as f:
    data = f.read()
print("binary bytes:", data)

# Other modes: 't' text (default), '+' read-and-write ('r+', 'w+', 'a+')
print("modes recap: r read | w overwrite | a append | x create-only | b binary | + update")


if __name__ == "__main__":
    print("\nFile modes demo complete.")
