"""
Module 3 — FUNCTIONS IN PYTHON
Feature: Built-in functions

Underlying concepts
- Built-ins live in the builtins module and are always available.
- Many consume *iterables* (not only lists): min, max, sum, any, all, sorted.
- min/max/sum on an empty sequence raise (or need a default).
- round uses banker's rounding (ties to even) — surprising for 2.5 / 3.5.
- isinstance is preferred over type(x) == ... because it allows subclasses.
- eval/exec run code: never pass untrusted input.
"""

nums = [4, 1, 7, 3, 9, 2]


print("=" * 60)
print("EXAMPLE 1 — len, sum, min, max, sorted, reversed")
print("=" * 60)

print("len:", len(nums))
print("sum / min / max:", sum(nums), min(nums), max(nums))
print("sum with start:", sum(nums, 100))
print("sorted new list:", sorted(nums), " original unchanged:", nums)
print("reversed iterator:", list(reversed(nums)))
print("min with key:", min(["fig", "banana", "kiwi"], key=len))

# Empty-sequence edge cases
print("sum([]) is 0:", sum([]))
try:
    min([])
except ValueError as exc:
    print("min([]) raises:", exc)
print("min with default:", min([], default="empty"))


print("\n" + "=" * 60)
print("EXAMPLE 2 — conversions, abs, round, bool")
print("=" * 60)

print("int/float/str:", int("10"), float("2.5"), str(99))
print("list/tuple/set:", list("ab"), tuple([1, 2]), set([1, 1, 2]))
print("bool empty/non-empty:", bool([]), bool([1]))
print("abs:", abs(-12), abs(3 + 4j))  # complex -> magnitude
print("round 2 dp:", round(3.14159, 2))
print("banker's rounding: round(2.5)=", round(2.5), " round(3.5)=", round(3.5))
print("divmod(17, 5):", divmod(17, 5))  # (quotient, remainder)
print("pow(2, 10), pow(2, 10, 1000) mod:", pow(2, 10), pow(2, 10, 1000))


print("\n" + "=" * 60)
print("EXAMPLE 3 — any, all, map, filter, zip, enumerate, range")
print("=" * 60)

print("any n > 8:", any(n > 8 for n in nums))
print("all n > 0:", all(n > 0 for n in nums))
print("any([]) is False, all([]) is True:", any([]), all([]))  # vacuous truth

print("map *2:", list(map(lambda n: n * 2, nums)))
print("filter odd:", list(filter(lambda n: n % 2, nums)))
print("enumerate:", list(enumerate(nums, start=1)))
print("zip stops early:", list(zip(["a", "b", "c"], nums)))
print("range(2, 10, 2):", list(range(2, 10, 2)))

# zip longest via padding yourself (itertools.zip_longest is extra, skip)
names = ["a", "b"]
print("manual pad zip:", list(zip(names, nums[: len(names)])))


print("\n" + "=" * 60)
print("EXAMPLE 4 — type checks and object inspection")
print("=" * 60)

print("type(nums):", type(nums))
print("isinstance list:", isinstance(nums, list))
print("isinstance (list, tuple):", isinstance(nums, (list, tuple)))
print("callable(len):", callable(len), " callable(3):", callable(3))
print("id(nums):", id(nums))
print("dir(str) is* methods:", [m for m in dir(str) if m.startswith("is")][:6])
print("hasattr(nums, 'append'):", hasattr(nums, "append"))
print("getattr fallback:", getattr(nums, "missing", "nope"))


print("\n" + "=" * 60)
print("EXAMPLE 5 — slice, format, and dangerous eval")
print("=" * 60)

print("slice object nums[1:5:2]:", nums[slice(1, 5, 2)])
print("format built-in:", format(3.14159, ".2f"), format(255, "x"))
print("ascii vs repr:", ascii("café"), repr("café"))
print("ord/chr:", ord("A"), chr(65))
print("sorted unique via set then list:", sorted(set(nums)))

# eval is a built-in but unsafe with untrusted strings
print("eval of a literal:", eval("[1, 2, 3]"))
print("prefer ast.literal_eval for data — never eval(user_input)")

# input() is built-in too; skipped so this file stays non-interactive
# name = input("Your name: ")


if __name__ == "__main__":
    print("\nBuilt-in functions demo complete.")
