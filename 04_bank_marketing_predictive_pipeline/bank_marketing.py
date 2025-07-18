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
    print("Cleaned data saved as bank_marketing_cleaned.csv")

if __name__ == "__main__":
    clean_data()

import pandas as pd
import os

def load_data():
    filename = "bank_marketing_cleaned.csv"
    if not os.path.exists(filename):
        raise FileNotFoundError("❌ bank_marketing_cleaned.csv not found. Run clean_data.py first.")
    df = pd.read_csv(filename)
    print("Loaded cleaned data")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())

import pandas as pd
import plotly.express as px
import os

def clean_data():
    df = pd.read_csv("bank_marketing.csv")
    numeric_cols = [
        "age", "campaign", "pdays", "previous",
        "emp.var.rate", "cons.price.idx", "cons.conf.idx",
        "euribor3m", "nr.employed"
    ]
    df_cleaned = df[numeric_cols].dropna()
    df_cleaned.to_csv("bank_marketing_cleaned.csv", index=False)
    print("Cleaned data saved as bank_marketing_cleaned.csv")

def load_data():
    if not os.path.exists("bank_marketing_cleaned.csv"):
        raise FileNotFoundError("❌ bank_marketing_cleaned.csv not found.")
    df = pd.read_csv("bank_marketing_cleaned.csv")
    print("Loaded cleaned data")
    return df

def run_all():
    clean_data()
    df = load_data()

    fig1 = px.scatter(df, x="campaign", y="euribor3m", title="Campaign vs Euribor Rate")
    fig1.write_html("campaign_vs_euribor.html")

    fig2 = px.histogram(df, x="campaign", title="Distribution of Campaign Count")
    fig2.write_html("campaign_histogram.html")

    fig3 = px.imshow(df.corr(), text_auto=True, title="Correlation Heatmap")
    fig3.write_html("correlation_heatmap.html")

    print("All plots saved as HTML files.")

if __name__ == "__main__":
    run_all()

import shutil

def download_outputs():
    from IPython.display import FileLink, display
    files = [
        "campaign_vs_euribor.html",
        "campaign_histogram.html",
        "correlation_heatmap.html"
	"bank_marketing_cleaned.csv"
    ]
    for f in files:
        try:
            display(FileLink(f))
        except:
            print(f"❌ {f} not found.")

download_outputs()

from google.colab import files

files.download("fig_campaign_vs_euribor.html")
files.download("fig_campaign_histogram.html")
files.download("fig_correlation_heatmap.html")
files.download("bank_marketing_cleaned.csv")
