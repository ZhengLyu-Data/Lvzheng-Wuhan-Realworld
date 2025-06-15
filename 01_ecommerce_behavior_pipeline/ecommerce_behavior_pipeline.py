import pandas as pd

def load_raw_data():
    return pd.read_csv("online_retail_II.csv", encoding="ISO-8859-1")

def clean_data(df):
    df = df.dropna(subset=["Invoice", "Customer ID", "Description", "Quantity", "Price"])
    df = df[df["Quantity"] > 0]
    df = df[df["Price"] > 0]
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["TotalPrice"] = df["Quantity"] * df["Price"]
    return df

def save_clean_data(df):
    df.to_csv("ecommerce_cleaned.csv", index=False)
    print("✅ Saved: ecommerce_cleaned.csv")

!python run_pipeline.py

import pandas as pd
df = pd.read_csv("online_retail_II.csv")

import os
print("online_retail_II.csv" in os.listdir())

import os
print(os.listdir())

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("online_retail_II_cleaned.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["TotalAmount"] = df["Price"] * df["Quantity"]

# Group by month
df.set_index("InvoiceDate", inplace=True)
monthly_sales = df.resample("ME")["TotalAmount"].sum()

# Plot without displaying
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (£)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# ✅ ONLY save, do NOT show
plt.savefig("monthly_sales_trend.png")
plt.close()  # ⚠️ prevent inline rendering in Colab

from google.colab import files
files.download("monthly_sales_trend.png")

import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("online_retail_II_cleaned.csv")

# Create total sales amount
df["TotalAmount"] = df["Price"] * df["Quantity"]

# Group by product description and sum total amount
top_products = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 10 Best-Selling Products by Revenue")
plt.ylabel("Total Revenue (£)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save figure
plt.savefig("top_products.png")
plt.close()

from google.colab import files
files.download("top_products.png")

import os
print("File exists?", os.path.exists("monthly_sales_trend.png"))

plt.savefig("monthly_sales_trend.png")

from google.colab import files
files.download("online_retail_II_cleaned.csv")
