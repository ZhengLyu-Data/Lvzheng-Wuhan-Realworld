from pyspark.sql import DataFrame
from pyspark.sql import functions as F
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def enrich_viewactivity(sdf: DataFrame) -> DataFrame:
    return (sdf
            .withColumn("date", F.to_date("started_at"))
            .withColumn("hour", F.hour("started_at"))
            .withColumn("weekday", F.date_format("started_at", "E"))
            .withColumn("minutes", F.col("duration_sec") / 60.0))

def make_aggregates(sdf: DataFrame) -> dict:
    top_titles = sdf.groupBy("title").agg(F.sum("minutes").alias("total_minutes"))
    hourly     = sdf.groupBy("hour").agg(F.sum("minutes").alias("total_minutes"))
    weekday    = sdf.groupBy("weekday").agg(F.sum("minutes").alias("total_minutes"))
    daily      = sdf.groupBy("date").agg(F.sum("minutes").alias("total_minutes"))
    return {
        "top_titles": top_titles,
        "hourly_minutes": hourly,
        "weekday_minutes": weekday,
        "daily_minutes": daily
    }

# ---------- plotting (pure, optionally save if filename provided) ----------
def plot_top_titles(pdf: pd.DataFrame, top_n: int = 15, filename: str | None = None):
    pdf = pdf.nlargest(top_n, "total_minutes").iloc[::-1]
    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot(x="total_minutes", y="title", data=pdf, ax=ax)
    ax.set_title(f"Top {top_n} Titles by Viewing Minutes")
    ax.set_xlabel("Total Minutes"); ax.set_ylabel("Title")
    fig.tight_layout()
    if filename: fig.savefig(filename, dpi=160)
    return fig

def plot_hourly(pdf: pd.DataFrame, filename: str | None = None):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="hour", y="total_minutes", data=pdf, marker="o", ax=ax)
    ax.set_title("Viewing Minutes by Hour")
    ax.set_xlabel("Hour of Day"); ax.set_ylabel("Total Minutes")
    fig.tight_layout()
    if filename: fig.savefig(filename, dpi=160)
    return fig

def plot_weekday(pdf: pd.DataFrame, filename: str | None = None):
    order = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    pdf = pdf.copy()
    if "weekday" in pdf.columns:
        pdf["weekday"] = pd.Categorical(pdf["weekday"], categories=order, ordered=True)
        pdf = pdf.sort_values("weekday")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x="weekday", y="total_minutes", data=pdf, ax=ax)
    ax.set_title("Viewing Minutes by Weekday")
    ax.set_xlabel("Weekday"); ax.set_ylabel("Total Minutes")
    fig.tight_layout()
    if filename: fig.savefig(filename, dpi=160)
    return fig