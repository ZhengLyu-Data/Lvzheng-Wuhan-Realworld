import pandas as pd

# Load original data
df = pd.read_csv("order_items.csv")

# Print basic info
print("Original shape:", df.shape)

# Drop rows with missing values
df = df.dropna()

# Drop duplicate rows
df = df.drop_duplicates()

# Convert shipping date column to datetime (if exists)
if 'shipping_limit_date' in df.columns:
    df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'], errors='coerce')

# Standardize column names to snake_case
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Save cleaned dataset
df.to_csv("order_items_cleaned_final.csv", index=False)

print("Cleaning complete. Saved as order_items_cleaned_final.csv")