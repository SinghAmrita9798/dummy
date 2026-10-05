"""
Module 3 — FUNCTIONS IN PYTHON
Feature: Generators

Underlying concepts
- `yield` turns a function into a generator function. Calling it returns a
  generator object; the body does not run until you iterate / next().
- Values are produced lazily (one at a time) — useful for large / infinite data.
- A generator is an iterator: one-shot. After exhaustion, next() raises
  StopIteration. for-loops swallow that automatically.
- `yield from` delegates to another iterable/generator.
- Generator expressions `(x for x in ...)` are lazy cousins of list comps.
"""


print("=" * 60)
print("EXAMPLE 1 — yield, next, list(), empty input")
print("=" * 60)


def count_up_to(n):
    current = 1
    while current <= n:
        yield current
        current += 1


print("count_up_to(5):", list(count_up_to(5)))
print("count_up_to(0):", list(count_up_to(0)))   # empty generator is fine

gen = count_up_to(3)
print("manual next:", next(gen), next(gen), next(gen))
try:
    next(gen)
except StopIteration:
    print("StopIteration after exhaustion")

# Calling the function again creates a NEW generator
print("fresh generator:", list(count_up_to(2)))


print("\n" + "=" * 60)
print("EXAMPLE 2 — running totals, generator expressions")
print("=" * 60)


def squares(n):
    for i in range(1, n + 1):
        yield i * i


def running_total(values):
    total = 0
    for v in values:
        total += v
        yield total


print("squares(4):", list(squares(4)))
print("running total:", list(running_total([10, 20, 30])))
print("running total empty:", list(running_total([])))

even_squares = (x * x for x in range(10) if x % 2 == 0)
print("genexpr even squares:", list(even_squares))
print("genexpr is one-shot, second list:", list(even_squares))  # []


print("\n" + "=" * 60)
print("EXAMPLE 3 — infinite generators must be bounded")
print("=" * 60)


def forever_tick():
    n = 0
    while True:
        yield n
        n += 1


for tick in forever_tick():
    print("tick", tick)
    if tick >= 3:
        break

# next(..., default) avoids StopIteration
g = count_up_to(1)
print("next with default:", next(g), next(g, "done"), next(g, "done"))


print("\n" + "=" * 60)
print("EXAMPLE 4 — yield from, send, close")
print("=" * 60)


def chain(*iterables):
    for it in iterables:
        yield from it          # same as: for item in it: yield item


print("yield from:", list(chain([1, 2], (3, 4), "ab")))


def echo():
    received = yield "ready"   # first next() gets 'ready'; send() value arrives here
    yield f"got {received!r}"


e = echo()
print("prime:", next(e))
print("send :", e.send("ping"))
e.close()
try:
    next(e)
except StopIteration:
    print("closed generator is exhausted")


print("\n" + "=" * 60)
print("EXAMPLE 5 — why lazy? memory contrast")
print("=" * 60)

# list comprehension builds everything now
eager = [i for i in range(5)]
lazy = (i for i in range(5))
print("eager list:", eager)
print("lazy gen  :", lazy, "->", list(lazy))

# return vs yield: a generator function that also hits return just stops
def until_negative(values):
    for v in values:
        if v < 0:
            return          # equivalent to stop; does not yield None
        yield v


print("stop on negative:", list(until_negative([1, 2, -3, 4])))


if __name__ == "__main__":
    print("\nGenerators demo complete.")
