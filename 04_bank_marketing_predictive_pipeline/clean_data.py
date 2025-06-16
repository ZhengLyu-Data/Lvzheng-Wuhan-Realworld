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