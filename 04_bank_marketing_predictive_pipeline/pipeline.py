import pandas as pd
import os

def load_data():
    filename = "bank_marketing_cleaned.csv"
    if not os.path.exists(filename):
        raise FileNotFoundError("❌ bank_marketing_cleaned.csv not found. Run clean_data.py first.")
    df = pd.read_csv(filename)
    print("Loaded cleaned data")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
