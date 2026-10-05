"""
Module 8 — PYTHON LIBRARIES
Feature: Seaborn

Seaborn sits on matplotlib and makes statistical plots with less code.
This demo saves a PNG next to the file (no GUI required).

Install if needed:
  pip install seaborn pandas matplotlib
"""

from pathlib import Path

try:
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
except ImportError:
    print("Install first: pip install seaborn pandas matplotlib")
    raise SystemExit(1)

OUT = Path(__file__).with_name("seaborn_scores.png")

df = pd.DataFrame(
    {
        "city": ["Delhi", "Delhi", "Pune", "Pune", "Mumbai", "Mumbai"],
        "score": [91, 84, 88, 95, 76, 80],
        "module": [8, 8, 8, 8, 8, 8],
    }
)

sns.set_theme(style="whitegrid")
ax = sns.barplot(data=df, x="city", y="score", estimator="mean", errorbar=None)
ax.set_title("Average score by city")
ax.set_ylim(0, 100)
plt.tight_layout()
plt.savefig(OUT, dpi=120)
plt.close()
print("saved plot:", OUT.name)
print("tip: sns.histplot, sns.scatterplot, sns.heatmap, sns.boxplot")


if __name__ == "__main__":
    print("\nSeaborn demo complete.")
