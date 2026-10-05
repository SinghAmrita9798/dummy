"""
Module 8 — PYTHON LIBRARIES
Feature: Math

The built-in `math` module covers constants, rounding, powers,
logs, trig, and combinatorics. No extra install needed.
"""

import math

print("pi:", math.pi, "e:", math.e, "tau:", math.tau)
print("sqrt(16):", math.sqrt(16))
print("pow(2, 10):", math.pow(2, 10), "exp(1):", math.exp(1))
print("log(100, 10):", math.log(100, 10), "log2(8):", math.log2(8))
print("ceil(2.1):", math.ceil(2.1), "floor(2.9):", math.floor(2.9))
print("fabs(-7):", math.fabs(-7), "factorial(5):", math.factorial(5))
print("gcd(24, 18):", math.gcd(24, 18), "lcm(4, 6):", math.lcm(4, 6))
print("comb(5, 2):", math.comb(5, 2), "perm(5, 2):", math.perm(5, 2))

# Trig uses radians
angle = math.radians(90)
print("sin(90°):", math.sin(angle), "cos(0):", math.cos(0))
print("hypot(3, 4):", math.hypot(3, 4))  # 5.0
print("isclose(0.1+0.2, 0.3):", math.isclose(0.1 + 0.2, 0.3))


if __name__ == "__main__":
    print("\nMath module demo complete.")
