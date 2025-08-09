import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========== Cleaning & Aggregation ==========
def _to_bool(x):
    s = str(x).strip().lower()
    if s in {"1","true","t","y","yes"}: return True
    if s in {"0","false","f","n","no"}: return False
    if isinstance(x, (bool, np.bool_)): return bool(x)
    if isinstance(x, (int, float)):     return bool(int(x))
    return False

def clean_and_aggregate(input_csv="train.csv", output_csv="walmart_weekly_clean.csv"):
    # Load CSV and normalize column names
    df = pd.read_csv(input_csv)
    df.columns = [c.strip().lower() for c in df.columns]

    # Required columns check
    required = {"store","dept","date","weekly_sales","isholiday"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Type conversion & missing handling
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"]).copy()
    df["weekly_sales"] = pd.to_numeric(df["weekly_sales"], errors="coerce").fillna(0)
    df["isholiday"] = df["isholiday"].apply(_to_bool)

    # Week-level key
    df["week_start"] = df["date"] - pd.to_timedelta(df["date"].dt.weekday, unit="D")
    iso = df["date"].dt.isocalendar()
    df["year"] = iso.year.astype(int)
    df["week"] = iso.week.astype(int)

    # Aggregate to ensure unique (store, dept, week)
    gcols = ["store","dept","week_start","year","week","isholiday"]
    agg = (df.groupby(gcols, as_index=False)
             .agg(weekly_sales=("weekly_sales","sum"))
             .sort_values(["store","dept","week_start"]))

    # Rolling averages by store-dept
    agg["sales_ma_4"]  = agg.groupby(["store","dept"])["weekly_sales"].transform(lambda s: s.rolling(4,  min_periods=1).mean())
    agg["sales_ma_12"] = agg.groupby(["store","dept"])["weekly_sales"].transform(lambda s: s.rolling(12, min_periods=1).mean())

    # YoY growth (previous year same week, 364 days offset)
    prev = agg[["store","dept","week_start","weekly_sales"]].copy()
    prev["week_start"] = prev["week_start"] + pd.Timedelta(days=364)
    prev = prev.rename(columns={"weekly_sales":"prev_year_sales"})
    agg = agg.merge(prev, on=["store","dept","week_start"], how="left")

    agg["yoy_growth"] = np.where(
        agg["prev_year_sales"].notna() & (agg["prev_year_sales"] != 0),
        agg["weekly_sales"] / agg["prev_year_sales"] - 1,
        np.nan
    )

    # Export cleaned dataset
    agg.to_csv(output_csv, index=False)
    print(f"[clean] saved -> {output_csv} ({len(agg)} rows)")
    return agg

# ========== Generate 3 Charts ==========
def generate_charts(clean_csv="walmart_weekly_clean.csv"):
    df = pd.read_csv(clean_csv, parse_dates=["week_start"])

    # Chart 1: Weekly total sales trend (line chart)
    c1 = (df.groupby("week_start", as_index=False)
            .agg(total_sales=("weekly_sales","sum"))
            .sort_values("week_start"))
    plt.figure()
    plt.plot(c1["week_start"], c1["total_sales"])
    plt.title("Weekly Total Sales Trend")
    plt.xlabel("Week Start"); plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("chart1_weekly_trend.png"); plt.close()

    # Chart 2: Top 10 stores by average YoY growth (bar chart)
    c2 = (df.groupby("store", as_index=False)
            .agg(avg_yoy_growth=("yoy_growth","mean"),
                 total_sales=("weekly_sales","sum"),
                 n=("weekly_sales","count")))
    c2 = c2[c2["n"] > 10].sort_values("avg_yoy_growth", ascending=False).head(10)
    plt.figure()
    plt.bar(c2["store"].astype(str), c2["avg_yoy_growth"])
    plt.title("Store YoY Growth Top 10")
    plt.xlabel("Store"); plt.ylabel("Avg YoY Growth")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("chart2_store_yoy_top10.png"); plt.close()

    # Chart 3: Top 20 store-dept combos by lift vs 4-week MA (bar chart)
    df["lift_vs_ma4"] = (df["weekly_sales"] - df["sales_ma_4"]) / df["sales_ma_4"].replace(0, np.nan)
    c3 = (df.groupby(["store","dept"], as_index=False)
            .agg(avg_lift=("lift_vs_ma4","mean"),
                 total_sales=("weekly_sales","sum"),
                 n=("weekly_sales","count")))
    c3 = c3[c3["n"] > 10].sort_values("avg_lift", ascending=False).head(20)
    labels = c3.apply(lambda r: f"{int(r['store'])}-{int(r['dept'])}", axis=1)
    plt.figure()
    plt.bar(labels, c3["avg_lift"])
    plt.title("Dept Lift vs 4-Week MA Top 20 (Store-Dept)")
    plt.xlabel("Store-Dept"); plt.ylabel("Avg Lift vs MA4")
    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()
    plt.savefig("chart3_dept_lift_top20.png"); plt.close()

    print("[charts] saved: chart1_weekly_trend.png, chart2_store_yoy_top10.png, chart3_dept_lift_top20.png")

# ========== CLI Entry ==========
def main():
    parser = argparse.ArgumentParser(description="Walmart pipeline: clean + charts")
    parser.add_argument("--input", default="train.csv", help="Raw CSV filename (default: train.csv)")
    parser.add_argument("--out-csv", default="walmart_weekly_clean.csv", help="Cleaned CSV output filename")
    args, _ = parser.parse_known_args()  # Ignore extra Jupyter/Colab args

    # Step 1: Clean & Aggregate
    clean_and_aggregate(input_csv=args.input, output_csv=args.out_csv)
    # Step 2: Generate Charts
    generate_charts(clean_csv=args.out_csv)
    print("[run_pipeline] Done.")

if __name__ == "__main__":
    main()
