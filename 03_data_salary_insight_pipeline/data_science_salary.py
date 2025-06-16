# clean_data.py

import pandas as pd

def clean_salary_data(input_file):
    df = pd.read_csv(input_file)

    # Drop unnamed index column if exists
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Rename for clarity
    df = df.rename(columns={
        'salary_in_usd': 'salary_usd',
        'employee_residence': 'residence',
        'company_location': 'location',
        'company_size': 'size'
    })

    return df

# run_pipeline.py

import pandas as pd
from clean_data import clean_salary_data
from pipeline import process_salary_data

# Load and clean data
input_file = 'data_science_salaries_raw.csv'
df_cleaned = clean_salary_data(input_file)

# Analyze
results = process_salary_data(df_cleaned)

# Show results
print("📊 Avg Salary by Experience Level:")
print(results['salary_by_experience'])

print("\n🏆 Top 10 Salaries by Job Title:")
print(results['top10_salary_by_title'])

print("\n🌍 Top 10 Salaries by Location:")
print(results['top10_salary_by_location'])

# pipeline.py

import pandas as pd

def process_salary_data(df):
    results = {}

    # Average salary by experience level
    results['salary_by_experience'] = df.groupby('experience_level')['salary_usd'].mean().round(2).sort_values(ascending=False)

    # Average salary by job title (Top 10)
    results['top10_salary_by_title'] = df.groupby('job_title')['salary_usd'].mean().round(2).sort_values(ascending=False).head(10)

    # Average salary by company location (Top 10)
    results['top10_salary_by_location'] = df.groupby('location')['salary_usd'].mean().round(2).sort_values(ascending=False).head(10)

    return results

# STEP 1: Read and clean uploaded raw data
import pandas as pd

df = pd.read_csv("data_science_salaries_raw.csv")

# Remove unnamed columns (e.g., index)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Standardize column names
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Rename selected columns
df = df.rename(columns={
    'salary_in_usd': 'salary_usd',
    'employee_residence': 'residence',
    'company_location': 'location',
    'company_size': 'size'
})

# STEP 2: Save cleaned data
df.to_csv("data_science_salaries_cleaned.csv", index=False)
print(" Cleaned file saved as: data_science_salaries_cleaned.csv")

# STEP 3: Download cleaned file
from google.colab import files
files.download("data_science_salaries_cleaned.csv")
