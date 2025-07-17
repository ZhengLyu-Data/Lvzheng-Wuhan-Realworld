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