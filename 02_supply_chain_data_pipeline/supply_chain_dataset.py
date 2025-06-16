# clean_data.py
import pandas as pd

def clean_supply_chain_data(file_path):
    df = pd.read_csv(file_path)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Rename key columns
    df = df.rename(columns={
        'reached.on_time_y.n': 'on_time_delivery',
        'cost_of_the_product': 'product_cost',
        'discount_offered': 'discount',
        'weight_in_gms': 'weight_grams'
    })

    return df

# run_pipeline.py
from clean_data import clean_supply_chain_data
import pandas as pd

input_file = "supply_chain_raw.csv"

# Clean and export
cleaned_df = clean_supply_chain_data(input_file)
cleaned_df.to_csv("supply_chain_cleaned_by_python.csv", index=False)

print("Cleaned file saved as supply_chain_cleaned_by_python.csv")

# pipeline.py
def process_data(df):
    results = {}

    # 1. Average Product Cost by Shipping Mode
    avg_cost_by_mode = df.groupby("mode_of_shipment")["product_cost"].mean()
    results["avg_cost_by_mode"] = avg_cost_by_mode

    # 2. Average Discount by Product Importance
    avg_discount_by_importance = df.groupby("product_importance")["discount"].mean()
    results["avg_discount_by_importance"] = avg_discount_by_importance

    # 3. Correlation between Customer Rating and Product Cost
    correlation_rating_cost = df["customer_rating"].corr(df["product_cost"])
    results["correlation_rating_cost"] = correlation_rating_cost

    return results

# test_pipeline.py
import pandas as pd
from pipeline import process_data

df = pd.read_csv("supply_chain_cleaned_by_python.csv")
results = process_data(df)

print("📦 Average Product Cost by Shipping Mode:")
print(results["avg_cost_by_mode"])

print("\n💸 Average Discount by Product Importance:")
print(results["avg_discount_by_importance"])

print("\n📊 Correlation between Customer Rating and Product Cost:")
print(results["correlation_rating_cost"])

# STEP 1: Read the original CSV data
import pandas as pd

df = pd.read_csv("supply_chain_raw.csv")

# Check the first few lines
print("🔍 Original data preview：")
print(df.head())

# STEP 2: Field standardization（The column name is lowercase, and the space is replaced）
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# STEP 3: Field name change unified style
df = df.rename(columns={
    'reached.on_time_y.n': 'on_time_delivery',
    'cost_of_the_product': 'product_cost',
    'discount_offered': 'discount',
    'weight_in_gms': 'weight_grams'
})

# STEP 4: Check the missing value
print("\n🧹 missing value statistics：")
print(df.isnull().sum())

# STEP 5: Data type check（Convert before visualization）
print("\n📐 field type：")
print(df.dtypes)

# STEP 6: Export the cleaned csv file
output_path = "supply_chain_cleaned.csv"
df.to_csv(output_path, index=False)

# STEP 7: Provide downloads
files.download(output_path)
