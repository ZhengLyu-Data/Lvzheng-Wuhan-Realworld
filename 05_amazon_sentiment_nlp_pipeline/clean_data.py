import pandas as pd
import re

def clean_text(text):
    text = str(text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()

# Load raw data
df = pd.read_csv("processed_reviews.csv")

# Drop rows with null comments
df = df[df["Text"].notnull()].copy()

# Clean text
df["cleaned_text"] = df["Text"].apply(clean_text)

# Save cleaned data
df.to_csv("cleaned_reviews.csv", index=False)