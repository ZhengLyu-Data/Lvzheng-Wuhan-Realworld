import pandas as pd

def clean_supply_chain_data(file_name):
    # Load the dataset
    df = pd.read_csv(file_name)

    # Standardize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Rename selected columns for consistency
    df = df.rename(columns={
        'reached.on_time_y.n': 'on_time_delivery',
        'cost_of_the_product': 'product_cost',
        'discount_offered': 'discount',
        'weight_in_gms': 'weight_grams'
    })

    # Drop rows with missing values
    df = df.dropna()

    return df