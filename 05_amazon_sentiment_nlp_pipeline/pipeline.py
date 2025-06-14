import pandas as pd
import re
from textblob import TextBlob

def clean_text(text):
    # Clean up the text：remove punctuation marks and non-letter characters
    text = str(text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

def get_sentiment(text):
    # Use TextBlob conduct emotional analysis
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def process_reviews(input_path, output_path):
    # Read the data
    df = pd.read_csv(input_path)

    # Only keep records with comments
    df = df[df['Text'].notnull()].copy()

    # Clean the text
    df['cleaned_text'] = df['Text'].apply(clean_text)

    # Emotional analysis of cleansing text
    df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

    # Output results
    df.to_csv(output_path, index=False)