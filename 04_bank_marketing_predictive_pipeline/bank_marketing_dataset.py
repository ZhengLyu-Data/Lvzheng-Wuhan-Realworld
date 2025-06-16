# run clean_data.py

import pandas as pd

def clean_bank_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df = df.rename(columns={
        'y': 'response',
        'job': 'occupation',
        'marital': 'marital_status',
        'education': 'education_level',
        'default': 'has_default',
        'housing': 'has_housing_loan',
        'loan': 'has_personal_loan',
        'poutcome': 'previous_outcome'
    })
    df = df.dropna()
    return df

# pipeline.py

def analyze_marketing_data(df):
    results = {}

    # Response by Occupation
    results['response_by_occupation'] = (
        df.groupby('occupation')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    # Response by Housing Loan
    results['response_by_housing'] = (
        df.groupby('has_housing_loan')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    # Response by Education Level
    results['response_by_education'] = (
        df.groupby('education_level')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    return results

# run_pipeline.py

def analyze_marketing_data(df):
    results = {}

    # Response by Occupation
    results['response_by_occupation'] = (
        df.groupby('occupation')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    # Response by Housing Loan
    results['response_by_housing'] = (
        df.groupby('has_housing_loan')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    # Response by Education Level
    results['response_by_education'] = (
        df.groupby('education_level')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    return results

from google.colab import files
files.download("bank_marketing_cleaned.csv")

# 📌 STEP 1: Read dataset
import pandas as pd
df = pd.read_csv('bank_marketing_raw.csv', sep=';')

# 📌 STEP 2: Preview data
print("Initial shape:", df.shape)
print(df.head())

# 📌 STEP 3: Basic Cleaning
# Replace 'unknown' with NaN for proper handling
df.replace('unknown', pd.NA, inplace=True)

# Drop rows with too many unknowns (optional)
threshold = int(len(df.columns) * 0.5)
df.dropna(thresh=threshold, inplace=True)

# Example: Fill NaNs in selected categorical fields with mode
for col in ['job', 'marital', 'education', 'default', 'housing', 'loan']:
    if df[col].isna().sum() > 0:
        df[col].fillna(df[col].mode()[0], inplace=True)

# Drop 'duration' if you aim for realistic modeling (see Kaggle note)
df.drop(columns=['duration'], inplace=True)

# Optional: Rename columns to snake_case for clarity
df.columns = [col.lower().replace('.', '_') for col in df.columns]

# Save and download the cleaned data
df_cleaned.to_csv("bank_marketing_cleaned.csv", index=False)
