"""
Module 3 — FUNCTIONS IN PYTHON
Feature: Defining a function, calling a function

Underlying concepts
- `def` creates a function object and binds it to a name.
- Parameters are local names. Arguments are the values you pass in.
- No `return` (or bare `return`) yields None.
- Default values are evaluated ONCE, at def time — never use a mutable default.
- *args is a tuple of extra positional args; **kwargs is a dict of extra keywords.
- `/` makes earlier params positional-only; `*` makes later params keyword-only.
"""


print("=" * 60)
print("EXAMPLE 1 — def, return, docstring, None")
print("=" * 60)


def greet(name):
    """Return a greeting for the given name."""
    print("hii")
    return f"Hello, {name}!"


def say_hi(name):
    """Prints, does not return a useful value."""
    print(f"Hi, {name}")
    # implicit return None


print(greet("Amrita"))
print("docstring:", greet.__doc__)
print("say_hi returns:", say_hi("Class"))  # None
print("bare return:", (lambda: (1, None)[1] if False else None)())

# Missing required argument
try:
    greet()
except TypeError as exc:
    print("missing arg:", exc)


print("\n" + "=" * 60)
print("EXAMPLE 2 — defaults, positional vs keyword, / and *")
print("=" * 60)


def add(a, b=0):
    """b is optional."""
    return a + b


def describe_student(name, module, *, passed=True):
    """`passed` is keyword-only (must write passed=...)."""
    status = "passed" if passed else "in progress"
    return f"{name} is on Module {module} ({status})"


def volume(length, width, /, *, height=1):
    """length, width positional-only; height keyword-only."""
    return length * width * height


print("add(5):", add(5), " add(5, 3):", add(5, 3), " add(a=2, b=4):", add(a=2, b=4))
print(describe_student("Amrita", 3, passed=True))
try:
    describe_student("Amrita", 3, False)  # False is positional — not allowed
except TypeError as exc:
    print("keyword-only enforced:", exc)

print("volume(2, 3, height=4):", volume(2, 3, height=4))
try:
    volume(length=2, width=3, height=4)
except TypeError as exc:
    print("positional-only enforced:", exc)


print("\n" + "=" * 60)
print("EXAMPLE 3 — *args, **kwargs, unpacking at the call site")
print("=" * 60)


def total(*scores):
    return sum(scores)


def profile(**info):
    return info


def mix(required, *args, flag=False, **kwargs):
    return {"required": required, "args": args, "flag": flag, "kwargs": kwargs}


print("total():", total(), " total(10, 20, 30):", total(10, 20, 30))
print("profile:", profile(name="Amrita", city="Delhi", module=3))
print("mix:", mix(1, 2, 3, flag=True, city="Pune"))

nums = [10, 20, 30]
info = {"name": "Riya", "city": "Pune"}
print("unpack list with *:", total(*nums))
print("unpack dict with **:", profile(**info))


print("\n" + "=" * 60)
print("EXAMPLE 4 — multiple return values and early return")
print("=" * 60)


def split_name(full_name):
    parts = full_name.split()
    if not parts:
        return "", ""          # early return for edge case
    first = parts[0]
    last = parts[-1] if len(parts) > 1 else ""
    return first, last         # actually returns a tuple


for sample in ["Amrita Kumari", "Riya", "", "A B C"]:
    first, last = split_name(sample)
    print(f"  {sample!r:16} -> first={first!r} last={last!r}")

result = split_name("Amrita Kumari")
print("type of multi-return:", type(result), result)


print("\n" + "=" * 60)
print("EXAMPLE 5 — functions as objects, mutable-default pitfall, scope")
print("=" * 60)

action = greet
print("via variable:", action("Class"))
print("callable:", callable(greet), "name:", greet.__name__)


def add_item_bad(item, bucket=[]):
    """BUG: the same list is reused across calls."""
    bucket.append(item)
    return bucket


def add_item_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print("bad 1:", add_item_bad("a"))
print("bad 2 (shared list!):", add_item_bad("b"))
print("good 1:", add_item_good("a"))
print("good 2 (fresh list):", add_item_good("b"))

# LEGB scope: Local, Enclosing, Global, Built-in
counter = 0


def bump():
    global counter
    counter += 1
    return counter


print("global counter:", bump(), bump())


if __name__ == "__main__":
    print("\nDefining and calling functions demo complete.")
