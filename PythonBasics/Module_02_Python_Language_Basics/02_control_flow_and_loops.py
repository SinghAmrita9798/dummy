"""
Module 2 — PYTHON LANGUAGE BASICS
Feature: Control Flow and Loops

Underlying concepts
- Conditions use truthiness, not only True/False. Empty / 0 / None are False.
- `if / elif / else` is exclusive: the first matching branch wins.
- `for` walks an iterable; `while` repeats until a condition is False.
- `break` leaves the loop; `continue` skips to the next iteration.
- `for/while ... else` runs the else ONLY if the loop did not break.
- `range(start, stop, step)` excludes stop. Empty range is legal.
- `zip` stops at the shortest input unless you use zip(..., strict=True).
"""


print("=" * 60)
print("EXAMPLE 1 — if / elif / else, ternary, truthiness")
print("=" * 60)

def letter_grade(score):
    # Order matters: check the highest band first.
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"


for sample in [100, 90, 89.9, 75, 60, 59, 0]:
    print(f"  score={sample!r:6} -> {letter_grade(sample)}")

score = 82
status = "pass" if score >= 60 else "fail"   # ternary: value_if_true if cond else value_if_false
print("ternary status:", status)

# Truthiness edge cases — these all take the False branch
for value in [0, 0.0, "", [], {}, set(), None, False]:
    if value:
        print("  truthy:", value)
    else:
        print("  falsy :", repr(value))

# Non-empty containers are truthy even if they hold zeros / False
print("non-empty [0] is truthy:", bool([0]))
print("non-empty '0' is truthy:", bool("0"))


print("\n" + "=" * 60)
print("EXAMPLE 2 — for, range, enumerate, zip")
print("=" * 60)

topics = ["syntax", "loops", "strings"]
for topic in topics:
    print("studying:", topic)

print("range(3):", list(range(3)))           # 0, 1, 2
print("range(1, 4):", list(range(1, 4)))     # 1, 2, 3
print("range(0, 10, 3):", list(range(0, 10, 3)))
print("range(5, 0, -1):", list(range(5, 0, -1)))
print("empty range(0):", list(range(0)))
print("empty range(5, 2):", list(range(5, 2)))  # start > stop with +step -> empty, not error

for index, topic in enumerate(topics, start=1):
    print(f"  {index}. {topic}")

tcs = [True, False, True]
hours = [2, 2, 1]
for topic, hour, tc in zip(topics, hours, tcs):
    print(f"  {topic} takes {hour}h")

# zip edge case: extra values on the longer sequence are silently dropped
print("zip short:", list(zip(["a", "b", "c"], [1, 2])))
try:
    pass #print(list(zip(["a", "b", "c"], [1, 2], strict=True)))  # Python 3.10+
except ValueError as exc:
    print("zip strict=True:", exc)


print("\n" + "=" * 60)
print("EXAMPLE 3 — while, break, continue, else-on-loop")
print("=" * 60)

countdown = 3
while countdown > 0:
    print("countdown:", countdown)
    countdown -= 1
print("after while, countdown is", countdown)

print("-- break / continue --")
for n in range(1, 8):
    if n == 3:
        continue     # skip this iteration
    if n == 6:
        break        # leave the loop entirely
    print("n =", n)

def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            print("found even:", n)
            break
    else:
        # runs only when the loop finished without break
        print("no even number in", nums)


find_first_even([1, 3, 5, 8, 9])
find_first_even([1, 3, 5])

# Infinite-loop guard (never `while True` without a break)
n = 0
while True:
    n += 1
    if n >= 3:
        break
print("while True broke at", n)


print("\n" + "=" * 60)
print("EXAMPLE 4 — nested loops, mutating while iterating, comprehensions")
print("=" * 60)

# Multiplication table snippet
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    print("row", i, row)

# Mutating a list you are iterating can skip items — don't do this
nums = [1, 2, 3, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print("BUG skipped 4 because the list shifted:", nums)

# Safer: iterate a copy, or build a new list
nums = [1, 2, 3, 4]
odds = [n for n in nums if n % 2]
print("comprehension filter odds:", odds)

squares = [n * n for n in range(5)]
print("squares:", squares)
print("dict comprehension:", {n: n * n for n in range(4)})
print("set comprehension unique lengths:", {len(t) for t in topics})


print("\n" + "=" * 60)
print("EXAMPLE 5 — match / case (Python 3.10+) and short-circuit logic")
print("=" * 60)

def handle(command):
    pass
    # match command:
    #     case "start" | "run":
    #         return "starting"
    #     case "stop":
    #         return "stopping"
    #     case ("goto", int(n)) if n > 0:
    #         return f"jump to module {n}"
    #     case {"op": "echo", "text": text}:
    #         return f"echo {text!r}"
    #     case _:
    #         return "unknown"


for cmd in ["start", "run", "stop", ("goto", 4), {"op": "echo", "text": "hi"}, 123]:
    print(f"  {cmd!r} -> {handle(cmd)}")

# Short-circuit: `and` / `or` return operands, not always True/False
print("'0' or 'fallback' ->", "" or "fallback")
print("'hi' or 'fallback' ->", "hi" or "fallback")
print("'hi' and 'ok' ->", "hi" and "ok")
print("None or 0 or 'last' ->", None or 0 or "last")


if __name__ == "__main__":
    print("\nControl flow and loops demo complete.")
