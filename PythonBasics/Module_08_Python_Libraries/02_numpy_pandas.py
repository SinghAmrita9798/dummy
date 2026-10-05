"""
Module 8 — PYTHON LIBRARIES
Feature: Numpy, Pandas

NumPy  -> fast n-dimensional arrays and numeric ops
Pandas -> labelled tables (DataFrame) for data analysis

Install if needed:
  pip install numpy pandas
"""

try:
    import numpy as np
    import pandas as pd
except ImportError:
    print("Install first: pip install numpy pandas")
    raise SystemExit(1)

# --- NumPy ---
arr = np.array([1, 2, 3, 4, 5])
matrix = np.arange(1, 7).reshape(2, 3)
print("array:", arr, "mean:", arr.mean(), "*2:", arr * 2)
print("matrix:\n", matrix)
print("column sums:", matrix.sum(axis=0))
print("zeros / ones:", np.zeros(3), np.ones((2, 2)))
print("dot [[1,2],[3,4]]:", np.dot([[1, 2], [3, 4]], [5, 6]))

# --- Pandas ---
df = pd.DataFrame(
    {
        "name": ["Amrita", "Riya", "Aman", "Neha"],
        "module": [8, 8, 8, 8],
        "score": [91, 88, 76, 95],
        "city": ["Delhi", "Pune", "Delhi", "Pune"],
    }
)
print("\nDataFrame:\n", df)
print("describe:\n", df["score"].describe())
print("filter score>=90:\n", df[df["score"] >= 90])
print("mean by city:\n", df.groupby("city")["score"].mean())
print("new column grade:\n", df.assign(grade=np.where(df["score"] >= 90, "A", "B")))


if __name__ == "__main__":
    print("\nNumPy + Pandas demo complete.")
