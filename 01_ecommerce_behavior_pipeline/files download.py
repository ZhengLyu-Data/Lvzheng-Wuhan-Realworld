import pandas as pd
from google.colab import files

# Load cleaned data
cleaned_df = pd.read_csv("order_items_cleaned.csv")

# Export and download
cleaned_df.to_csv("order_items_cleaned_download.csv", index=False)
files.download("order_items_cleaned.csv")