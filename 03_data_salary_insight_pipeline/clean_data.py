
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
