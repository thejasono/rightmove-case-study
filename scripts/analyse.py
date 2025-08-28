from __future__ import annotations
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=Path("examples/rightmove.csv"))
    args = ap.parse_args()

    df = pd.read_csv(args.csv, encoding="utf-8-sig")
    # Convert numeric
    for col in ["price_gbp", "price_pcm_est", "bedrooms", "bathrooms"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Summary
    by_bed = df.groupby("bedrooms", dropna=True)["price_pcm_est"].median().sort_index()
    print("Median price_pcm_est by bedrooms:\n", by_bed)

    # Chart
    out_png = args.csv.parent / "summary.png"
    plt.figure()
    by_bed.plot(kind="bar", title="Median Monthly Price by Bedrooms")
    plt.ylabel("Price (GBP)")
    plt.xlabel("Bedrooms")
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Wrote {out_png}")
