"""
Module 2 — PYTHON LANGUAGE BASICS
Feature: Syntax and Data Types

Underlying concepts
- Python is dynamically typed: the name has no type, the *object* does.
- Indentation (4 spaces) defines blocks. Mixing tabs/spaces is a SyntaxError.
- Everything is an object: int, function, None, even classes.
- Mutable vs immutable: list/dict/set can change in place; int/str/tuple cannot.
- Truthiness: 0, 0.0, "", [], {}, set(), None are False; everything else is True.
"""


print("=" * 60)
print("EXAMPLE 1 — Names, objects, and dynamic typing")
print("=" * 60)

course_name = "Python Class"          # str
module_number = 2                     # int  (unlimited size, not 32-bit)
duration_hours = 2.5                  # float (IEEE-754, binary, not exact money)
is_beginner_friendly = True           # bool is a subclass of int (True == 1)
optional_note = None                  # None is a singleton


print("Course:", course_name, type(course_name))
print("Module:", module_number, type(module_number))
print("Hours:", duration_hours, type(duration_hours))
print("Beginner:", is_beginner_friendly, "and True == 1 is", True == 0)
print("Optional:", optional_note, optional_note is None)

# Same name can later point at a different type (legal, but confusing)
module_number = "two"
print("re-bound module_number:", module_number, type(module_number))
module_number = 2  # put the int back

print("\n\n\n")
print("\n" + "=" * 60)
print("EXAMPLE 2 — Type conversion and conversion edge cases")
print("=" * 60)

a= int("21")
print("int('21'):", type(a))
print("float('89.5'):", float("89.5"))
print("str(99):", str(99))
print("bool(0), bool(1), bool(''):", bool(0), bool(1), bool(""))
print("int(True), int(False):", int(True), int(False))
print("int(3.9) truncates toward 0:", int(3.9), int(-3.9))  # 3, -3

# Edge cases — these raise ValueError / TypeError
for raw in ["21", "  21  ", "21.0", "", "abc", None]:
    try:
        print(f"  int({raw!r}) ->", int(raw))
    except (ValueError, TypeError) as exc:
        print(f"  int({raw!r}) failed:", type(exc).__name__, exc)

print("int('21', base=2) binary:", int("1010", 2))   # 10
print("int('ff', base=16) hex:", int("ff", 16))      # 255


print("\n" + "=" * 60)
print("EXAMPLE 3 — Sequence types: list, tuple, set, dict")
print("=" * 60)

skills = ["python", "git", "sql", "sql", "python", "Python"]                    # mutable, ordered, duplicates ok
levels = ("beginner", "intermediate", "advanced", "beginner", "intermediate", "Intermediate")    # immutable, ordered
unique_tags = {"python", "basics", "python", "python", "basics", "Python"}         # unique, unordered
student = {"name": "Amrita", "module": 2, "passed": True, "name": "abc"}

print("list:", skills, "len:", len(skills))
print("tuple:", levels)
print("set dropped duplicate 'python':", unique_tags)
print("dict lookup:", student["name"], student.get("city", "unknown"))

# Mutability contrast
skills.append("flask")          # list can grow
try:
    levels[0] = "intro"         # tuple cannot
except TypeError as exc:
    print("tuple item assign failed:", exc)

# Empty containers are NOT None
print("[] == None:", [] == None, "[] is None:", [] is None)
print("empty list truthiness:", bool([]), "non-empty:", bool(skills))


print("\n" + "=" * 60)
print("EXAMPLE 4 — Arithmetic, comparison, identity vs equality")
print("=" * 60)

a, b = 10, 3
print("+/−/*:", a + b, a - b, a * b)
print("/ true div:", a / b, "  // floor:", a // b, "  % mod:", a % b)
print("** power:", a ** b)
print("negative floor: -10 // 3 =", -10 // 3, "  (goes toward -inf, not 0)")
print("float surprise: 0.1 + 0.2 == 0.3 is", 0.1 + 0.2 == 0.3)
print("safer: abs((0.1 + 0.2) - 0.3) < 1e-9 ->", abs((0.1 + 0.2) - 0.3) < 1e-9)

print("chained compare 1 < 2 < 3:", 1 < 2 < 3)
print("'==' value equality:", [1, 2] == [1, 2])
x = [1, 2]
y = x
z = [1, 2]
print("'is' identity: x is y", x is y, "| x is z", x is z)  # y aliases x; z is a copy
print("None checks should use 'is':", optional_note is None)


print("\n" + "=" * 60)
print("EXAMPLE 5 — Unpacking, multiple assignment, and copy pitfalls")
print("=" * 60)

first, *rest = skills
print("first:", first, "rest:", rest)

# Swap without a temp
left, right = 1, 2
left, right = right, left
print("swapped:", left, right)

# Nested unpack
row = ("Amrita", (91, 88))
name, (quiz, exam) = row
print("nested unpack:", name, quiz, exam)

# Copy pitfall: assignment copies the *name*, not the list
alias = skills
alias.append("oops")
print("skills also changed via alias:", skills)

shallow = skills.copy()          # or skills[:]
shallow.append("only-copy")
print("original after copy.append:", skills)
print("copy:", shallow)

# Nested mutable inside a tuple is still mutable
pair = ("ok", ["inner"])
pair[1].append("changed")
print("tuple with list inside:", pair)


if __name__ == "__main__":
    print("\nSyntax and data types demo complete.")
