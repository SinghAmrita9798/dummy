"""
Module 4 — DATA STRUCTURE IN PYTHON
Feature: Collections Module — Overview, use cases

Underlying concepts
- collections is in the standard library (no pip).
- Counter is a dict subclass: missing keys read as 0 (no KeyError on []).
- ChainMap searches mappings left-to-right; writes go to the FIRST map.
- OrderedDict still matters for move_to_end / popitem(last=False). Plain
  dict already keeps insertion order (Python 3.7+).
- Also useful: Counter arithmetic, most_common, subtract.
"""

from collections import Counter, defaultdict, deque, namedtuple, ChainMap, OrderedDict


print("=" * 60)
print("EXAMPLE 1 — Counter: count, most_common, arithmetic")
print("=" * 60)

text = "python python class data python"
word_counts = Counter(text.split())
print("Counter:", word_counts)
print("most_common 2:", word_counts.most_common(2))
print("total:", sum(word_counts.values()))
print("missing key reads as 0:", word_counts["xyz"])
print("elements replayed:", list(Counter(a=2, b=1).elements()))

a = Counter(python=3, git=1)
b = Counter(python=1, sql=2)
print("add:", a + b)
print("subtract (keep positive):", a - b)
print("empty Counter most_common:", Counter().most_common())


print("\n" + "=" * 60)
print("EXAMPLE 2 — defaultdict + deque + namedtuple recap")
print("=" * 60)

by_first = defaultdict(list)
for word in ["apple", "ant", "banana", "berry"]:
    by_first[word[0]].append(word)
print("defaultdict:", dict(by_first))

window = deque(maxlen=3)
for n in range(5):
    window.append(n)
print("deque window:", list(window))

Record = namedtuple("Record", "topic hours")
print("namedtuple:", Record("collections", 1))


print("\n" + "=" * 60)
print("EXAMPLE 3 — ChainMap lookup vs write")
print("=" * 60)

defaults = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}
settings = ChainMap(user, defaults)
print("theme (user wins):", settings["theme"], " lang (default):", settings["lang"])

settings["lang"] = "hi"          # writes to FIRST map (user), does not edit defaults
print("user after write:", user)
print("defaults unchanged:", defaults)
print("missing key:", "nope" in settings)

try:
    ChainMap()["x"]
except KeyError as extra:
    print("empty ChainMap KeyError:", extra)


print("\n" + "=" * 60)
print("EXAMPLE 4 — OrderedDict move_to_end / popitem")
print("=" * 60)

lru_like = OrderedDict()
for key in ["a", "b", "c"]:
    lru_like[key] = True
lru_like.move_to_end("a")
print("after move_to_end(a):", list(lru_like))
print("pop oldest (last=False):", lru_like.popitem(last=False))
print("pop newest (last=True):", lru_like.popitem(last=True))

plain = {}
plain["a"] = 1
plain["b"] = 2
print("plain dict also keeps order:", list(plain))


print("\n" + "=" * 60)
print("EXAMPLE 5 — When to pick which type")
print("=" * 60)

print("- Counter: word frequency, vote tally, bags of items")
print("- defaultdict: grouping records, adjacency lists")
print("- deque: queues, BFS, last-N events")
print("- namedtuple: CSV rows, points, immutable records")
print("- ChainMap: layered config (cli > env > file > defaults)")
print("- OrderedDict: LRU cache / reorder keys")


if __name__ == "__main__":
    print("\nCollections module demo complete.")
