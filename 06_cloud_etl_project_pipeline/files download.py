# build_and_download.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F, types as T
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from zipfile import ZipFile

# 1) Spark session
spark = SparkSession.builder.getOrCreate()

# 2) Load raw CSV (header only; local file in current dir)
sdf = spark.read.option("header", True).csv("All_ViewingActivity.csv")

# 3) Clean function (inline)
def clean_viewactivity(sdf):
    # normalize column names
    for c in sdf.columns:
        sdf = sdf.withColumnRenamed(c, c.strip().lower().replace(" ", "_"))
    # required cols
    if not {"start_time","duration","title"}.issubset(set(sdf.columns)):
        raise ValueError("Columns 'Start Time', 'Duration', 'Title' are required.")
    # parse timestamp and duration
    sdf = sdf.withColumn("started_at", F.to_timestamp("start_time"))
    parts = F.split(F.col("duration"), ":")
    hr  = F.when(F.size(parts) == 3, F.element_at(parts, 1).cast("int")).otherwise(F.lit(0))
    mn  = F.when(F.size(parts) == 3, F.element_at(parts, 2).cast("int")) \
           .when(F.size(parts) == 2, F.element_at(parts, 1).cast("int")) \
           .otherwise(F.lit(0))
    sec = F.when(F.size(parts) >= 1, F.element_at(parts, F.size(parts)).cast("int")).otherwise(F.lit(0))
    sdf = sdf.withColumn("duration_sec", (hr*3600 + mn*60 + sec).cast(T.LongType()))
    # optional columns
    if "device_type" not in sdf.columns:
        sdf = sdf.withColumn("device_type", F.lit(None).cast(T.StringType()))
    if "profile_name" not in sdf.columns:
        sdf = sdf.withColumn("profile_name", F.lit(None).cast(T.StringType()))
    # filter and select final schema
    return (sdf
            .select("profile_name","title","started_at","duration_sec","device_type")
            .filter(F.col("title").isNotNull())
            .filter(F.col("started_at").isNotNull())
            .filter(F.col("duration_sec").isNotNull() & (F.col("duration_sec") > 0)))

# 4) Clean + save CSV
sdf_clean = clean_viewactivity(sdf)
pdf_clean = sdf_clean.toPandas()
pdf_clean.to_csv("clean_viewactivity.csv", index=False)

# 5) Aggregations (in pandas for quick plotting)
pdf_clean["started_at"] = pd.to_datetime(pdf_clean["started_at"])
pdf_clean["hour"] = pdf_clean["started_at"].dt.hour
pdf_clean["weekday"] = pdf_clean["started_at"].dt.day_name()
pdf_clean["minutes"] = pdf_clean["duration_sec"] / 60.0

top_titles = (pdf_clean.groupby("title", as_index=False)["minutes"]
              .sum().sort_values("minutes", ascending=False).head(15))
hourly = pdf_clean.groupby("hour", as_index=False)["minutes"].sum()
weekday = pdf_clean.groupby("weekday", as_index=False)["minutes"].sum()
weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
weekday["weekday"] = pd.Categorical(weekday["weekday"], categories=weekday_order, ordered=True)
weekday = weekday.sort_values("weekday")

# 6) Plot and save PNGs
plt.figure(figsize=(9,6))
sns.barplot(x="minutes", y="title", data=top_titles)
plt.title("Top 15 Titles by Viewing Minutes")
plt.xlabel("Total Minutes"); plt.ylabel("Title")
plt.tight_layout()
plt.savefig("top_titles.png", dpi=160)
plt.close()

plt.figure(figsize=(8,4))
sns.lineplot(x="hour", y="minutes", data=hourly, marker="o")
plt.title("Viewing Minutes by Hour")
plt.xlabel("Hour of Day"); plt.ylabel("Total Minutes")
plt.tight_layout()
plt.savefig("hourly.png", dpi=160)
plt.close()

plt.figure(figsize=(8,4))
sns.barplot(x="weekday", y="minutes", data=weekday)
plt.title("Viewing Minutes by Weekday")
plt.xlabel("Weekday"); plt.ylabel("Total Minutes")
plt.tight_layout()
plt.savefig("weekday.png", dpi=160)
plt.close()

# 7) Zip and trigger download (Colab)
with ZipFile("netflix_outputs.zip", "w") as zf:
    zf.write("clean_viewactivity.csv")
    zf.write("top_titles.png")
    zf.write("hourly.png")
    zf.write("weekday.png")

print("Created netflix_outputs.zip and triggering download...")

try:
    from google.colab import files
    files.download("netflix_outputs.zip")
except Exception:
    print("Not running in Google Colab. Please download netflix_outputs.zip manually.")