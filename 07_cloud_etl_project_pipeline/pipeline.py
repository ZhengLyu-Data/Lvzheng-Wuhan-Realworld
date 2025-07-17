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