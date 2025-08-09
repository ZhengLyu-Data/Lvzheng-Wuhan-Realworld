from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql import types as T

def clean_viewactivity(sdf: DataFrame) -> DataFrame:
    """
    Input columns expected from All_ViewingActivity.csv:
      'Profile Name', 'Start Time', 'Duration', 'Title', 'Device Type', ...
    Output columns:
      profile_name STRING,
      title        STRING,
      started_at   TIMESTAMP,
      duration_sec BIGINT,
      device_type  STRING
    """
    # normalize column names
    for c in sdf.columns:
        sdf = sdf.withColumnRenamed(c, c.strip().lower().replace(" ", "_"))

    required = ["start_time", "duration", "title"]
    missing = [c for c in required if c not in sdf.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # timestamp
    sdf = sdf.withColumn("started_at", F.to_timestamp("start_time"))

    # parse duration "HH:MM:SS" or "MM:SS" -> seconds
    parts = F.split(F.col("duration"), ":")
    hr   = F.when(F.size(parts) == 3, F.element_at(parts, 1).cast("int")).otherwise(F.lit(0))
    mn   = F.when(F.size(parts) == 3, F.element_at(parts, 2).cast("int"))\
            .when(F.size(parts) == 2, F.element_at(parts, 1).cast("int"))\
            .otherwise(F.lit(0))
    sec  = F.when(F.size(parts) >= 1, F.element_at(parts, F.size(parts)).cast("int")).otherwise(F.lit(0))
    sdf = sdf.withColumn("duration_sec", (hr * 3600 + mn * 60 + sec).cast(T.LongType()))

    # optional columns
    if "device_type" not in sdf.columns:
        sdf = sdf.withColumn("device_type", F.lit(None).cast(T.StringType()))
    if "profile_name" not in sdf.columns:
        sdf = sdf.withColumn("profile_name", F.lit(None).cast(T.StringType()))

    out = (sdf
           .select("profile_name", "title", "started_at", "duration_sec", "device_type")
           .filter(F.col("title").isNotNull())
           .filter(F.col("started_at").isNotNull())
           .filter(F.col("duration_sec").isNotNull() & (F.col("duration_sec") > 0)))
    return out
    
if __name__ == "__main__":
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()

    # Read raw CSV file
    sdf_raw = spark.read.option("header", True).csv("All_ViewingActivity.csv")

    # Clean data
    sdf_clean = clean_viewactivity(sdf_raw)

    # Save cleaned data to current directory
    sdf_clean.toPandas().to_csv("clean_viewactivity.csv", index=False)
    print("Cleaned data saved to clean_viewactivity.csv")