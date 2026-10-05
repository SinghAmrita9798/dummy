"""
Module 5 — FILE HANDLING AND EXCEPTION HANDLING
Feature: Exception handling

Underlying concepts
- Exceptions interrupt normal flow. Uncaught, they crash the program.
- try runs code. except catches matching types (most specific first).
- else runs only if try did NOT raise. finally ALWAYS runs (cleanup).
- `raise` starts an exception. `raise from` chains causes.
- Catch specific types, not bare `except:` (that also catches KeyboardInterrupt).
- Custom exceptions should subclass Exception, not BaseException.
"""


class ScoreError(Exception):
    """Raised when a score is outside 0–100."""


def grade(score):
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise TypeError("score must be a number")
    if score < 0 or score > 100:
        raise ScoreError(f"invalid score: {score}")
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    return "C"


def demo_try_except():
    samples = [95, -1, "high", 80, True]
    for value in samples:
        try:
            print(value, "->", grade(value))
        except ScoreError as exc:
            print("ScoreError:", exc)
        except TypeError as exc:
            print("TypeError:", exc)
        else:
            print("  (no error)")
        finally:
            print("  done with", value)


def demo_file_errors(path="missing_file.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found:", path)
        return ""
    except PermissionError:
        print("No permission to read:", path)
        return ""


def parse_score(text):
    try:
        return grade(int(text))
    except (ValueError, ScoreError) as extra:
        return f"could not grade {text!r}: {extra}"
    except Exception as extra:
        return f"unexpected {type(extra).__name__}: {extra}"


def read_lbyl(path):
    from pathlib import Path
    p = Path(path)
    if not p.exists():
        print("LBYL missing:", path)
        return ""
    return p.read_text(encoding="utf-8")


def load_module_number(raw):
    try:
        n = int(raw)
    except ValueError as extra:
        raise ScoreError(f"not a module number: {raw!r}") from extra
    if n < 2:
        raise ScoreError("module too small")
    return n


if __name__ == "__main__":
    print("=" * 60)
    print("EXAMPLE 1 — try / except / else / finally")
    print("=" * 60)
    demo_try_except()

    print("\n" + "=" * 60)
    print("EXAMPLE 2 — catching several types, order matters")
    print("=" * 60)
    for raw in ["91", "150", "abc"]:
        print(" ", raw, "->", parse_score(raw))

    print("\n" + "=" * 60)
    print("EXAMPLE 3 — file errors, EAFP vs LBYL")
    print("=" * 60)
    print("EAFP:", repr(demo_file_errors()))
    print("LBYL:", repr(read_lbyl("missing_file.txt")))

    print("\n" + "=" * 60)
    print("EXAMPLE 4 — raise from (chaining)")
    print("=" * 60)
    try:
        load_module_number("x")
    except ScoreError as extra:
        print("chained:", extra)
        print("  cause:", extra.__cause__)

    print("\n" + "=" * 60)
    print("EXAMPLE 5 — ZeroDivision / IndexError")
    print("=" * 60)
    samples = [(10, 2), (10, 0), ([], 0)]
    for seq_or_n, d in samples:
        try:
            if isinstance(seq_or_n, list):
                print("item:", seq_or_n[d])
            else:
                print("div:", seq_or_n / d)
        except ZeroDivisionError:
            print("cannot divide by zero")
        except IndexError:
            print("list index out of range")

    print("\nException handling demo complete.")

