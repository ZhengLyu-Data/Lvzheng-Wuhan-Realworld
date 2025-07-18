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

import pandas as pd
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

# Load cleaned data
df = pd.read_csv("cleaned_reviews.csv")

# Perform sentiment analysis
df["sentiment"] = df["cleaned_text"].apply(get_sentiment)

# Save result
df.to_csv("final_reviews.csv", index=False)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load final dataset
try:
    df = pd.read_csv("final_reviews.csv")
    print("Data loaded successfully.")
except Exception as e:
    print("Error loading data:", e)
    exit()

# Check if sentiment column exists
if "sentiment" not in df.columns:
    print("'sentiment' column not found.")
    print("Available columns:", df.columns.tolist())
    exit()

# Plot sentiment distribution
try:
    plt.figure(figsize=(6,4))
    sns.countplot(data=df, x="sentiment", palette="Set2", order=["positive", "neutral", "negative"])
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("sentiment_distribution.png")
    print("Sentiment distribution chart saved.")
except Exception as e:
    print("Error plotting sentiment distribution:", e)

# Generate WordCloud
try:
    text_all = " ".join(df["cleaned_text"].dropna().astype(str).tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_all)
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud of Reviews")
    plt.tight_layout()
    plt.savefig("wordcloud_reviews.png")
    print("Word cloud saved.")
except Exception as e:
    print("Error generating word cloud:", e)

# Optional: Download files if running in Google Colab
try:
    import google.colab
    from google.colab import files

    # Download the cleaned dataset
    files.download("cleaned_reviews.csv")

    # Download the two visualization charts
    files.download("sentiment_distribution.png")
    files.download("wordcloud_reviews.png")

    print("All files downloaded (Colab environment).")
except:
    print("Files saved locally. You can manually access them in the current directory.")    
