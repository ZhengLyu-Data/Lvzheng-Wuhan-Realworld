import pandas as pd

def load_data(file_name):
    return pd.read_csv(file_name)

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()

    # Show existing columns for safety
    print("🧾 Columns in dataset:", df.columns.tolist())

    # Convert numeric columns if they exist
    if 'order_item_product_price' in df.columns:
        df['order_item_product_price'] = pd.to_numeric(df['order_item_product_price'], errors='coerce')

    if 'order_item_subtotal' in df.columns:
        df['order_item_subtotal'] = pd.to_numeric(df['order_item_subtotal'], errors='coerce')

    df = df.dropna()

    return df

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    input_file = 'order_items.csv'
    output_file = 'order_items_cleaned.csv'

    df = load_data(input_file)
    cleaned_df = clean_data(df)
    save_data(cleaned_df, output_file)

    print("Cleaned file saved successfully.")