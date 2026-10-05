"""
Module 3 — FUNCTIONS IN PYTHON
Feature: Lambda function

Underlying concepts
- `lambda args: expression` is a one-expression anonymous function.
- It CANNOT contain statements (if/for/return/assignment). Use `def` then.
- Same calling rules as def: defaults, *args, **kwargs all work.
- Common with sorted(key=...), min/max(key=...), map, filter.
- Late-binding closure: a lambda inside a loop sees the *final* loop variable
  unless you bind it as a default argument.
"""


print("=" * 60)
print("EXAMPLE 1 — Basic lambda vs equivalent def")
print("=" * 60)

square = lambda x: x * x
print("square(6):", square(6))
print("add:", (lambda a, b: a + b)(2, 3))
print("default arg:", (lambda x, y=10: x + y)(5))
print("immediate call:", (lambda a, b: a if a > b else b)(9, 4))

# Identity / type
print("type:", type(square), "name:", square.__name__)  # name is always '<lambda>'


print("\n" + "=" * 60)
print("EXAMPLE 2 — map, filter, and when a comprehension is clearer")
print("=" * 60)

nums = [1, 2, 3, 4, 5, 6]
print("map squares:", list(map(lambda n: n ** 2, nums)))
print("filter evens:", list(filter(lambda n: n % 2 == 0, nums)))
print("same with comprehension:", [n ** 2 for n in nums if n % 2 == 0])

# filter keeps truthy results of the callback — 0 is dropped
print("filter(None, [0, 1, '', 'x']):", list(filter(None, [0, 1, "", "x"])))


print("\n" + "=" * 60)
print("EXAMPLE 3 — sorted / min / max with key=")
print("=" * 60)

students = [
    {"name": "Riya", "score": 88},
    {"name": "Aman", "score": 72},
    {"name": "Neha", "score": 95},
    {"name": "Dev", "score": 88},
]
print("by score desc:", sorted(students, key=lambda s: s["score"], reverse=True))
print("tie-break name:", sorted(students, key=lambda s: (-s["score"], s["name"])))
print("top student:", max(students, key=lambda s: s["score"]))

words = ["banana", "fig", "apple", "kiwi"]
print("by length:", sorted(words, key=lambda w: len(w)))
print("case-insensitive:", sorted(["Banana", "apple", "Fig"], key=lambda w: w.lower()))


print("\n" + "=" * 60)
print("EXAMPLE 4 — closures and the late-binding trap")
print("=" * 60)

# BUG: every lambda reads the *current* i, which is 2 after the loop
bad = [lambda: i for i in range(3)]
print("late binding (all 2):", [fn() for fn in bad])

# FIX: bind i as a default argument (evaluated at lambda-create time)
good = [lambda i=i: i for i in range(3)]
print("default-arg bind:", [fn() for fn in good])


print("\n" + "=" * 60)
print("EXAMPLE 5 — limits of lambda; use def instead")
print("=" * 60)

# No statements, no type hints that read well, no multi-line body.
# This is the kind of logic that should be a named function:

def grade(score):
    if score < 0 or score > 100:
        raise ValueError("score out of range")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    return "C"


for s in [95, 82, 40]:
    print(f"  grade({s}) = {grade(s)}")

# You *can* stuff a ternary into a lambda, but it gets unreadable fast:
tiny = lambda s: "A" if s >= 90 else "B" if s >= 75 else "C"
print("tiny lambda grade(82):", tiny(82))


if __name__ == "__main__":
    print("\nLambda function demo complete.")
