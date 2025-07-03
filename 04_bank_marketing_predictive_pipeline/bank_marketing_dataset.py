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

# STEP 1: Read dataset
import pandas as pd
df = pd.read_csv('bank_marketing_raw.csv', sep=';')

# STEP 2: Preview data
print("Initial shape:", df.shape)
print(df.head())

# STEP 3: Basic Cleaning
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
df.to_csv("bank_marketing_cleaned.csv", index=False)

import pandas as pd
import plotly.express as px
from google.colab import files
import os

# Read the cleaned dataset
df = pd.read_csv("bank_marketing_cleaned.csv")
df.columns = df.columns.str.lower()

# Create output directory
output_dir = "visualizations"
os.makedirs(output_dir, exist_ok=True)

# Group by education and response
grouped = df.groupby(['education', 'y']).size().reset_index(name='count')
grouped.columns = ['education', 'response', 'count']

# Create interactive bar chart
fig = px.bar(grouped, x='education', y='count', color='response',
             barmode='group', title='Subscription Outcome by Education Level')

# Save as interactive html(offline-compatible)
output_path = f"{output_dir}/fig1_education.html"
fig.write_html(output_path)

# Download the file (for Google Colab)
files.download(output_path)

# Group by housing loan and response
grouped2 = df.groupby(['housing', 'y']).size().reset_index(name='count')
grouped2.columns = ['housing', 'response', 'count']

# Create interactive bar chart
fig2 = px.bar(grouped2, x='housing', y='count', color='response',
              barmode='group', title='Subscription Outcome by Housing Loan Status')

# Save as HTML
output_path2 = f"{output_dir}/fig2_housing.html"
fig2.write_html(output_path2)

# Download
files.download(output_path2)

# Group by occupation and response
grouped3 = df.groupby(['job', 'y']).size().reset_index(name='count')
grouped3.columns = ['occupation', 'response', 'count']

# Create interactive bar chart
fig3 = px.bar(grouped3, x='occupation', y='count', color='response',
              barmode='group', title='Subscription Outcome by Occupation')

# Adjust x-axis label order
fig3.update_layout(xaxis={'categoryorder': 'total descending'})

# Save as HTML
output_path3 = f"{output_dir}/fig3_occupation.html"
fig3.write_html(output_path3)

# Download
files.download(output_path3)
