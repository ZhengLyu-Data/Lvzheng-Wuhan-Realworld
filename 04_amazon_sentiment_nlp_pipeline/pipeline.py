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
