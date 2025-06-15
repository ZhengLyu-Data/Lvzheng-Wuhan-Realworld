import pandas as pd

def load_raw_data(filepath):
    return pd.read_csv(filepath, encoding='ISO-8859-1')

def clean_data(df):
    df = df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'])
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
