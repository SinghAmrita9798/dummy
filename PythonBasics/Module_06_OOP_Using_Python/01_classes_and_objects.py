"""
Module 6 — OBJECT ORIENTED PROGRAMMING USING PYTHON
Feature: Classes and Objects — define classes and create objects

Underlying concepts
- A class is a blueprint. An object (instance) is one concrete value of that blueprint.
- `__init__` is not the constructor — it *initializes* an already-created instance.
  `self` is that instance (the name is convention).
- Class attributes live on the class and are shared. Instance attributes live on
  `self` and are per-object.
- Methods are functions that receive the instance as the first argument.
- `__str__` is for users (print); `__repr__` is for developers (debug / lists).
"""


class Student:
    """A simple class: blueprint for student objects."""

    school = "Python Class"  # class attribute (shared)

    def __init__(self, name, module):
        self.name = name          # instance attributes
        self.module = module
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        return f"Student({self.name}, module={self.module})"

    def __repr__(self):
        return f"Student(name={self.name!r}, module={self.module})"


print("=" * 60)
print("EXAMPLE 1 — create objects, call methods")
print("=" * 60)

s1 = Student("Amrita", 6)
s2 = Student("Riya", 6)
s1.add_score(90)
s1.add_score(88)
s2.add_score(76)
print(s1)
print("repr:", repr(s1))
print("s1 average:", s1.average())
print("s2 average:", s2.average())
print("empty average:", Student("New", 6).average())


print("\n" + "=" * 60)
print("EXAMPLE 2 — class vs instance attributes")
print("=" * 60)

print("Student.school:", Student.school, " s1.school:", s1.school)
s1.school = "Local branch"     # creates an INSTANCE attr that shadows the class attr
print("after s1.school = ... :", s1.school, "| s2 still:", s2.school)
print("class attribute unchanged:", Student.school)
del s1.school
print("after del, s1 sees class again:", s1.school)


print("\n" + "=" * 60)
print("EXAMPLE 3 — identity, equality default, vars / __dict__")
print("=" * 60)

print("isinstance:", isinstance(s1, Student), isinstance(s1, object))
print("s1 is s2:", s1 is s2)
print("default == is identity:", s1 == Student("Amrita", 6))
print("vars:", vars(s1))
print("type:", type(s1), "class name:", s1.__class__.__name__)


print("\n" + "=" * 60)
print("EXAMPLE 4 — mutable default pitfall on a class")
print("=" * 60)


class BadStudent:
    scores = []          # SHARED across all instances — usually a bug

    def __init__(self, name):
        self.name = name


b1, b2 = BadStudent("A"), BadStudent("B")
b1.scores.append(10)
print("b2.scores also changed:", b2.scores)


print("\n" + "=" * 60)
print("EXAMPLE 5 — __init__ is required args; extra attrs")
print("=" * 60)

try:
    Student()
except TypeError as extra:
    print("missing args:", extra)

s1.city = "Delhi"        # Python lets you add attributes later
print("ad-hoc attr city:", s1.city)


if __name__ == "__main__":
    print("\nClasses and objects demo complete.")
