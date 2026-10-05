"""
Module 8 — PYTHON LIBRARIES
Feature: Scipy

SciPy builds on NumPy: stats, optimize, interpolate, linalg, signal...
Install if needed:
  pip install scipy numpy
"""

try:
    import numpy as np
    from scipy import stats, optimize, linalg
except ImportError:
    print("Install first: pip install scipy numpy")
    raise SystemExit(1)

# --- stats ---
data = np.array([12, 15, 14, 10, 18, 20, 16])
print("mean / std:", stats.tmean(data), stats.tstd(data))
print("describe:", stats.describe(data))
print("normal pdf at 0:", stats.norm.pdf(0))

# --- optimize: find minimum of (x-3)^2 + 1 ---
def f(x):
    return (x - 3) ** 2 + 1


result = optimize.minimize_scalar(f)
print("min of (x-3)^2+1 at x =", result.x, "f =", result.fun)

# --- linalg ---
A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])
x = linalg.solve(A, b)
print("solve Ax=b ->", x)
print("det(A):", linalg.det(A))
print("inv(A):\n", linalg.inv(A))


if __name__ == "__main__":
    print("\nSciPy demo complete.")
