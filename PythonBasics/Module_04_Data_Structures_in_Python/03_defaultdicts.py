"""
Module 4 — DATA STRUCTURE IN PYTHON
Feature: Defaultdicts

Underlying concepts
- defaultdict(factory) calls factory() whenever you READ a missing key
  via d[key]. factory must be a zero-arg callable: int, list, set, lambda...
- .get() and `in` do NOT create the key. Only __getitem__ / d[key] does.
- The created default is stored, so later lookups see it.
- dict.setdefault(key, []) is similar but you pass the value, not a factory;
  a shared mutable default there is a classic bug.
- Nested defaultdict needs a lambda (or a named factory) because the inner
  type itself takes an argument.
"""

from collections import defaultdict


print("=" * 60)
print("EXAMPLE 1 — list factory: grouping")
print("=" * 60)

groups = defaultdict(list)
pairs = [("fruit", "apple"), ("color", "red"), ("fruit", "mango"), ("color", "blue")]
for kind, value in pairs:
    groups[kind].append(value)
print("groups:", dict(groups))
print("missing key via [] creates []:", groups["missing"], "keys now:", list(groups))


print("\n" + "=" * 60)
print("EXAMPLE 2 — int / set factories")
print("=" * 60)

counts = defaultdict(int)
for ch in "banana":
    counts[ch] += 1
print("letter counts:", dict(counts))

students_by_city = defaultdict(set)
for name, city in [("Amrita", "Delhi"), ("Riya", "Pune"), ("Aman", "Delhi"), ("Amrita", "Delhi")]:
    students_by_city[city].add(name)
print("by city (unique names):", {k: sorted(v) for k, v in students_by_city.items()})


print("\n" + "=" * 60)
print("EXAMPLE 3 — [] creates, .get / in do not")
print("=" * 60)

d = defaultdict(int)
print("'x' in d before access:", "x" in d)
print("d.get('x'):", d.get("x"), "  still not in d:", "x" in d)
print("d['x'] inserts 0:", d["x"], "  now in d:", "x" in d)

normal = {}
try:
    normal["missing"] += 1
except KeyError as extra:
    print("plain dict KeyError:", extra)


print("\n" + "=" * 60)
print("EXAMPLE 4 — nested defaultdict and custom factory")
print("=" * 60)

tree = defaultdict(lambda: defaultdict(int))
tree["module4"]["namedtuple"] += 1
tree["module4"]["deque"] += 2
print("nested:", {k: dict(v) for k, v in tree.items()})


def roster():
    return {"students": [], "count": 0}


school = defaultdict(roster)
school["B"]["students"].append("Riya")
school["B"]["count"] += 1
print("custom factory:", dict(school))


print("\n" + "=" * 60)
print("EXAMPLE 5 — pitfalls: factory must be callable, shared setdefault")
print("=" * 60)

try:
    defaultdict(0)
except TypeError as extra:
    print("factory must be callable:", extra)

# setdefault with a shared list — DANGEROUS
shared = []
plain = {}
plain.setdefault("a", shared).append(1)
plain.setdefault("b", shared).append(2)
print("shared list leaked across keys:", plain)

safe = defaultdict(list)
safe["a"].append(1)
safe["b"].append(2)
print("defaultdict list is per-key:", dict(safe))


if __name__ == "__main__":
    print("\nDefaultdicts demo complete.")
