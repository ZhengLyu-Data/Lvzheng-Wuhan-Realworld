import pandas as pd

def load_and_clean(csv_path: str) -> pd.DataFrame:
    # Read CSV file and treat the first column as date
    df = pd.read_csv(csv_path, index_col=0, parse_dates=True)

    # Reset index and rename to 'date'
    df = df.reset_index().rename(columns={"index": "date"})

    # Standardize column names to lowercase with underscores
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Keep only required columns
    required = ["date", "open", "high", "low", "close", "volume"]
    if not all(col in df.columns for col in required):
        raise ValueError(f"Missing required columns. Expected: {required}")

    # Convert data types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows with missing values and duplicates
    df = df.dropna(subset=required)
    df = df.drop_duplicates(subset=["date"]).sort_values("date").reset_index(drop=True)

    return df

if __name__ == "__main__":
    clean_df = load_and_clean("apple_stock.csv")
    clean_df.to_csv("clean_apple_stock.csv", index=False)
    print("Cleaned data saved to clean_apple_stock.csv")
