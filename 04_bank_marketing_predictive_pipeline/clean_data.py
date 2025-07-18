import pandas as pd

def clean_data():
    df = pd.read_csv("bank_marketing.csv")
    numeric_cols = [
        "age", "campaign", "pdays", "previous", 
        "emp.var.rate", "cons.price.idx", "cons.conf.idx", 
        "euribor3m", "nr.employed"
    ]
    df_cleaned = df[numeric_cols].dropna()
    df_cleaned.to_csv("bank_marketing_cleaned.csv", index=False)
    print("✅ Cleaned data saved as bank_marketing_cleaned.csv")

if __name__ == "__main__":
    clean_data()