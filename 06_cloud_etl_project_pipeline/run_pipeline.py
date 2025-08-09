from pyspark.sql import functions as F
from pyspark.sql import types as T
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_pipeline(sdf_raw):
    # === Data Cleaning ===
    for c in sdf_raw.columns:
        sdf_raw = sdf_raw.withColumnRenamed(c, c.strip().lower().replace(" ", "_"))

    required = ["start_time", "duration", "title"]
    missing = [c for c in required if c not in sdf_raw.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    sdf_raw = sdf_raw.withColumn("started_at", F.to_timestamp("start_time"))
    parts = F.split(F.col("duration"), ":")
    hr  = F.when(F.size(parts) == 3, F.element_at(parts, 1).cast("int")).otherwise(F.lit(0))
    mn  = F.when(F.size(parts) == 3, F.element_at(parts, 2).cast("int"))\
           .when(F.size(parts) == 2, F.element_at(parts, 1).cast("int"))\
           .otherwise(F.lit(0))
    sec = F.when(F.size(parts) >= 1, F.element_at(parts, F.size(parts)).cast("int")).otherwise(F.lit(0))
    sdf_raw = sdf_raw.withColumn("duration_sec", (hr * 3600 + mn * 60 + sec).cast(T.LongType()))

    if "device_type" not in sdf_raw.columns:
        sdf_raw = sdf_raw.withColumn("device_type", F.lit(None).cast(T.StringType()))
    if "profile_name" not in sdf_raw.columns:
        sdf_raw = sdf_raw.withColumn("profile_name", F.lit(None).cast(T.StringType()))

    sdf = (sdf_raw
           .select("profile_name", "title", "started_at", "duration_sec", "device_type")
           .filter(F.col("title").isNotNull())
           .filter(F.col("started_at").isNotNull())
           .filter(F.col("duration_sec").isNotNull() & (F.col("duration_sec") > 0)))

    # === Data Enrichment ===
    sdf = (sdf
           .withColumn("date", F.to_date("started_at"))
           .withColumn("hour", F.hour("started_at"))
           .withColumn("weekday", F.date_format("started_at", "E"))
           .withColumn("minutes", F.col("duration_sec")/60.0))

    # === Aggregations ===
    top_titles = sdf.groupBy("title").agg(F.sum("minutes").alias("total_minutes"))
    hourly     = sdf.groupBy("hour").agg(F.sum("minutes").alias("total_minutes"))
    weekday    = sdf.groupBy("weekday").agg(F.sum("minutes").alias("total_minutes"))

    pdf_top  = top_titles.orderBy(F.desc("total_minutes")).limit(30).toPandas()
    pdf_hour = hourly.orderBy("hour").toPandas()
    pdf_week = weekday.toPandas()

    # === Plot 1: Top 15 Titles ===
    fig1, ax1 = plt.subplots(figsize=(9,6))
    sns.barplot(x="total_minutes", y="title",
                data=pdf_top.nlargest(15, "total_minutes").iloc[::-1], ax=ax1)
    ax1.set_title("Top 15 Titles by Viewing Minutes")
    ax1.set_xlabel("Total Minutes"); ax1.set_ylabel("Title")
    fig1.tight_layout()
    fig1.savefig("top_titles.png", dpi=160)

    # === Plot 2: Viewing Minutes by Hour ===
    fig2, ax2 = plt.subplots(figsize=(8,4))
    sns.lineplot(x="hour", y="total_minutes", data=pdf_hour, marker="o", ax=ax2)
    ax2.set_title("Viewing Minutes by Hour")
    ax2.set_xlabel("Hour of Day"); ax2.set_ylabel("Total Minutes")
    fig2.tight_layout()
    fig2.savefig("hourly.png", dpi=160)

    # === Plot 3: Viewing Minutes by Weekday ===
    order = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    pdf_week["weekday"] = pd.Categorical(pdf_week["weekday"], categories=order, ordered=True)
    pdf_week = pdf_week.sort_values("weekday")
    fig3, ax3 = plt.subplots(figsize=(8,4))
    sns.barplot(x="weekday", y="total_minutes", data=pdf_week, ax=ax3)
    ax3.set_title("Viewing Minutes by Weekday")
    ax3.set_xlabel("Weekday"); ax3.set_ylabel("Total Minutes")
    fig3.tight_layout()
    fig3.savefig("weekday.png", dpi=160)

    return {
        "pdf_top_titles": pdf_top,
        "pdf_hourly": pdf_hour,
        "pdf_weekday": pdf_week
    }