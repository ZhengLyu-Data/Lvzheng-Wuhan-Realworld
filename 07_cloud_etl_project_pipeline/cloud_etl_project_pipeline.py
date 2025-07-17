import pandas as pd

# Load raw dataset
df = pd.read_csv("real_estate_raw.csv")

# Drop rows with missing target variable
df = df.dropna(subset=["Price"])

# Fill missing numerical values with median
num_cols = ['Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt']
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill missing categorical values with mode
cat_cols = ['CouncilArea']
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove outliers in Price
df = df[(df['Price'] >= 100000) & (df['Price'] <= 3000000)]

# Save cleaned data
df.to_csv("real_estate_cleaned.csv", index=False)
print("Data cleaned and saved to real_estate_cleaned.csv")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("real_estate_cleaned.csv")

# 1. Average price by region
region_price = df.groupby("Regionname")["Price"].mean().sort_values(ascending=False)
region_price.plot(kind="barh", title="Average Price by Region")
plt.xlabel("Average Price")
plt.tight_layout()
plt.savefig("avg_price_by_region.png")

# 2. Relationship: Landsize vs Price
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Landsize", y="Price", hue="Regionname", alpha=0.6)
plt.title("Landsize vs Price")
plt.savefig("landsize_vs_price.png")

# 3. Number of properties by year built
df["YearBuilt"] = df["YearBuilt"].astype(int)
year_count = df["YearBuilt"].value_counts().sort_index()
year_count.plot(kind="line", title="Property Count by Year Built")
plt.ylabel("Count")
plt.xlabel("Year Built")
plt.savefig("property_count_by_year.png")

print("Pipeline analysis completed and charts saved.")

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
