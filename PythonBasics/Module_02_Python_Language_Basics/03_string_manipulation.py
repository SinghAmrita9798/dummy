"""
Module 2 — PYTHON LANGUAGE BASICS
Feature: String Manipulation — Methods, formatting, f-strings

Underlying concepts
- str is immutable: methods return a NEW string; the original is unchanged.
- Indexing is 0-based. Slices [start:stop:step] exclude stop and never raise
  IndexError (they just return a shorter / empty string).
- Prefer f-strings for readability. .format() is useful when the template
  is stored separately. % formatting is legacy.
- Unicode: a character may be more than one code point (emoji, combining marks).
- split() with no args splits on any whitespace and drops empties;
  split(',') keeps empties between commas.
"""

title = "  python language basics  "
name = "Amrita"
module = 2
progress = 0.856


print("=" * 60)
print("EXAMPLE 1 — Methods: strip, case, replace, split, join")
print("=" * 60)

print("original:", repr(title))
print("strip :", repr(title.strip()))
print("lstrip:", repr(title.lstrip()))
print("rstrip:", repr(title.rstrip()))
print("title :", title.strip().title())
print("upper :", title.strip().upper())
print("lower :", "PyThOn".lower())
print("swapcase:", "PyThOn".swapcase())
print("replace one:", title.strip().replace("python", "Python"))
print("replace limit:", "aa-aa-aa".replace("aa", "bb", 1))  # only first

print("split default:", title.strip().split())
print("split comma :", "a,b,,c".split(","))          # keeps empty
print("split maxsplit:", "a-b-c-d".split("-", 2))
print("rsplit:", "a-b-c-d".rsplit("-", 1))
print("partition:", "user@example.com".partition("@"))
print("join:", " | ".join(["syntax", "loops", "strings"]))

# Immutability: original title is still padded
print("title unchanged after strip():", repr(title))

# join edge case
try:
    print("-".join([1, 2, 3]))
except TypeError as exc:
    print("join requires str items:", exc)


print("\n" + "=" * 60)
print("EXAMPLE 2 — Search, tests, and slicing")
print("=" * 60)
print("\n\n\n")
clean = title.strip()
print("startswith / endswith:", clean.startswith("python"), clean.endswith("basics"))
print("startswith tuple:", clean.startswith(("python", "java")))
print("find (index or -1):", clean.find("language"), clean.find("xyz"))
print("index raises if missing:")
try:
    clean.index("xyz")
except ValueError as exc:
    print(" ", exc)
print("count 'a':", clean.count("a"))
print("in operator:", "language" in clean)

# Character class tests — edge cases
samples = ["42", "42.0", "Ⅳ", "Python", "Py3", " ", "\n", "١٢٣"]
for s in samples:
    print(f"  {s!r:8} isdigit={s.isdigit()} isnumeric={s.isnumeric()} "
          f"isalpha={s.isalpha()} isalnum={s.isalnum()} isspace={s.isspace()}")

word = "Python"
print("index 0 / -1:", word[0], word[-1])
print("[0:3]:", word[0:3], "  [1:]:", word[1:], "  [:-1]:", word[:-1])
print("reverse [::-1]:", word[::-1])
print("step [::2]:", word[::2])
print("out-of-range slice is empty, not error:", word[50:60], word[-50:-40])
try:
    print(word[50])
except IndexError as exc:
    print("single index out of range DOES raise:", exc)


print("\n" + "=" * 60)
print("EXAMPLE 3 — Formatting: %, .format(), f-strings")
print("=" * 60)

print("\n\n\n")
print("percent: Hello %s, module %d" % (name, module))
print("format pos: Hello {}, module {}".format(name, module))
print("format named: Hello {n}, module {m}".format(n=name, m=module))
print(f"f-string: Hello {name}, you are on Module {module}")
print(f"progress percent: {progress:.1%}")       # 85.6%
print(f"float 2 dp: {progress:.2f}")
print(f"padded int: {module:03d}")               # 002
print(f"aligned: '{name:>10}' '{name:<10}' '{name:^10}'")
print(f"debug = syntax: {name=}, {module=}")     # Python 3.8+
print(f"expression: {2 + 2}  {name.upper()}")

template = "Hello {name}, module {module}"
print("reusable template:", template.format(name="Riya", module=5))


print("\n" + "=" * 60)
print("EXAMPLE 4 — Quotes, escapes, raw, multi-line, unicode")
print("=" * 60)
print("\n\n\n")
print("single quotes can hold double: 'say \"hi\"'")
print("double quotes can hold single: \"it's fine\"")
print("newline \\n and tab \\t:\nline1\tcol2")
print(r"raw path keeps backslashes: C:\new\folder")
notes = """Line 1
Line 2
Line 3"""
print("triple-quoted:\n", notes)

print("unicode length 'café':", len("café"))
print("emoji length '🙂':", len("🙂"), "  encode bytes:", "🙂".encode("utf-8"))
print("casefold vs lower (German ß):", "straße".lower(), "straße".casefold())


print("\n" + "=" * 60)
print("EXAMPLE 5 — Practical recipes and pitfalls")
print("=" * 60)
print("\n\n\n")
email = "  Student@Example.COM  "
normalized = email.strip().lower()
print("normalized email:", normalized)
print("looks like email:", "@" in normalized and "." in normalized.split("@")[-1])

# Don't use `is` to compare string values (interning is an implementation detail)
a = "python"
b = "".join(["py", "thon"])
print("a == b:", a == b, "  a is b (identity, may be False):", a is b)

# Building many pieces: join is faster / cleaner than + in a loop
parts = ["Module", "2", "strings"]
print("join parts:", " ".join(parts))

# strip vs replace for leftover characters
messy = "++hello++"
print("strip('+'):", messy.strip("+"), "  remove all +:", messy.replace("+", ""))

# translate / maketrans for many 1-char replacements
table = str.maketrans({"-": "_", " ": "_"})
print("maketrans:", "python language-basics".translate(table))


if __name__ == "__main__":
    print("\nString manipulation demo complete.")
