# clean_data.py
import pandas as pd

def clean_and_aggregate(input_csv: str, output_csv: str):
    """
    Load, clean, and aggregate Walmart weekly sales data.
    Saves the cleaned dataset to output_csv.
    """
    df = pd.read_csv(input_csv)

    # Ensure date type
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.rename(columns={'Date': 'week_start'})

    # Example cleaning: fill NA with 0 for Weekly_Sales
    df['Weekly_Sales'] = df['Weekly_Sales'].fillna(0)

    # Feature engineering: 4-week moving average
    df = df.sort_values(['Store', 'Dept', 'week_start'])
    df['sales_ma_4'] = df.groupby(['Store', 'Dept'])['Weekly_Sales'].transform(
        lambda x: x.rolling(window=4, min_periods=1).mean()
    )

    # YoY growth (requires at least 52 weeks back)
    df['yoy_growth'] = df.groupby(['Store', 'Dept'])['Weekly_Sales'].pct_change(periods=52)

    # Save cleaned dataset
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}")
