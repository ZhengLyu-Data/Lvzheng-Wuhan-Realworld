import pandas as pd

def load_data(file_name):
    return pd.read_csv(file_name)

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()

    df['order_item_quantity'] = pd.to_numeric(df['order_item_quantity'], errors='coerce')
    df['order_item_subtotal'] = pd.to_numeric(df['order_item_subtotal'], errors='coerce')
    df = df.dropna(subset=['order_item_quantity', 'order_item_subtotal'])

    return df

def save_data(df, output_file):
    df.to_csv(output_file, index=False)