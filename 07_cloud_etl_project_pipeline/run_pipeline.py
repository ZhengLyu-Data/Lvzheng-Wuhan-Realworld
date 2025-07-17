import subprocess

print("Step 1: Cleaning data...")
subprocess.run(["python", "clean_data.py"])

print("Step 2: Running analysis pipeline...")
subprocess.run(["python", "pipeline.py"])

print("ETL pipeline finished.")

from google.colab import files
files.download("avg_price_by_region.png")
files.download("property_count_by_year.png")
files.download("real_estate_cleaned.csv")