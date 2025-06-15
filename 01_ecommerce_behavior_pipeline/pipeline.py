import os
from clean_data import load_raw_data, clean_data, save_cleaned_data

def run_pipeline():
    raw_path = 'data/raw/online_retail_II.csv'
    output_path = 'data/processed/cleaned_retail_data.csv'

    print("🚀 Loading raw data...")
    df_raw = load_raw_data(raw_path)

    print("🧹 Cleaning data...")
    df_clean = clean_data(df_raw)

    print("💾 Saving cleaned data...")
    os.makedirs('data/processed', exist_ok=True)
    save_cleaned_data(df_clean, output_path)

    print("✅ Pipeline completed! Cleaned data saved to:", output_path)