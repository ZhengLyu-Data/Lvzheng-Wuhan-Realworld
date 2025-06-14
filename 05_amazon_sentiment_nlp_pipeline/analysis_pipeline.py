import pandas as pd

print("🔍 Loading raw data...")
df = pd.read_csv("/content/amazon_reviews_raw.csv")

# Select useful fleids
cols = ['Time', 'UserId', 'ProfileName', 'Score', 'Text']
df = df[[col for col in cols if col in df.columns]]
df = df.dropna(subset=['Text'])
df = df.sample(n=5000, random_state=42)

# Convert the time field
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], unit='s', errors='coerce')

# Conver the score to emotioanl label
def map_score(score):
    try:
        s = int(score)
        if s <= 2:
            return "negative"
        elif s == 3:
            return "neutral"
        else:
            return "positive"
    except:
        return "unknown"

df['sentiment_score'] = df['Score'].apply(map_score)
df = df[df['sentiment_score'] != 'unknown']

# Save the cleaning results
df.to_csv("/content/amazon_reviews_cleaned.csv", index=False)
print("Cleaned data saved as amazon_reviews_cleaned.csv")

!pip install textblob

!ls /content/

!python run_pipeline.py

import pandas as pd

# Read pipeline clean output files
df = pd.read_csv("/content/processed_reviews.csv")

# Print field view structure
print("🧾 Original field：", df.columns.tolist())

# Simplified fields(only keep these columns)
columns_to_keep = ['Time', 'UserId', 'sentiment', 'Text']
df = df[columns_to_keep]

df = df.dropna(subset=['Text'])
df = df[df['sentiment'].isin(['positive', 'neutral', 'negative'])]

print(df['sentiment'].unique())
print(df['sentiment'].isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

print("🚀 Loading and cleaning data...")

from google.colab import files
df = pd.read_csv("/content/amazon_reviews_raw.csv")

df = pd.read_csv("amazon_reviews_raw.csv")

# Select essential columns (adjust if not present)
cols = ['Time', 'UserId', 'ProfileName', 'Score', 'Text']
df = df[[col for col in cols if col in df.columns]]
df = df.dropna(subset=['Text'])
df = df.sample(n=5000, random_state=42)

# Convert time if present
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], unit='s', errors='coerce')

# Convert score to sentiment label
def map_score(score):
    try:
        s = int(score)
        if s <= 2:
            return "negative"
        elif s == 3:
            return "neutral"
        else:
            return "positive"
    except:
        return "unknown"

df['sentiment_score'] = df['Score'].apply(map_score)
df = df[df['sentiment_score'] != 'unknown']

# Save cleaned data for later steps
df.to_csv("clean_reviews.csv", index=False)
print("Data cleaned. Total records:", len(df))

df = pd.read_csv("amazon_reviews_raw.csv")

# Select essential columns (adjust if not present)
cols = ['Time', 'UserId', 'ProfileName', 'Score', 'Text']
df = df[[col for col in cols if col in df.columns]]
df = df.dropna(subset=['Text'])
df = df.sample(n=5000, random_state=42)

# Convert time if present
if 'Time' in df.columns:
    df['Time'] = pd.to_datetime(df['Time'], unit='s', errors='coerce')

# Convert score to sentiment label
def map_score(score):
    try:
        s = int(score)
        if s <= 2:
            return "negative"
        elif s == 3:
            return "neutral"
        else:
            return "positive"
    except:
        return "unknown"

df['sentiment_score'] = df['Score'].apply(map_score)
df = df[df['sentiment_score'] != 'unknown']

# Save cleaned data for later steps
df.to_csv("clean_reviews.csv", index=False)
print("Data cleaned. Total records:", len(df))

import pandas as pd
from textblob import TextBlob

# Load the cleaned review dataset from Step 2
df = pd.read_csv("clean_reviews.csv")

# Define the sentiment labeling function
def get_sentiment(text):
    try:
        text = str(text)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # ranges from -1 to 1
        if polarity > 0.1:
            return "positive"
        elif polarity < -0.1:
            return "negative"
        else:
            return "neutral"
    except:
        return "neutral"

# Apply the function to the 'Text' column
print("🔍 Running sentiment analysis. This may take a few minutes...")
df['predicted_sentiment'] = df['Text'].apply(get_sentiment)

# Save the labeled dataset for later use (visualization & modeling)
df.to_csv("clean_reviews_labeled.csv", index=False)
print("Sentiment analysis complete. Output saved as: clean_reviews_labeled.csv")

import pandas as pd

print("🧪 Step 3: Checking columns and previewing data...")
df = pd.read_csv("clean_reviews_labeled.csv")
print(df.head())
print(" Step 3 complete.")

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

print("🎨 Step 4: Generating word cloud...")
df = pd.read_csv("clean_reviews_labeled.csv")
texts = df['Text'].fillna('').tolist()
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(texts)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(texts))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Most Frequent Words in Amazon Reviews")
plt.tight_layout()
plt.savefig("wordcloud.png")
plt.show()
print("Step 4 complete: wordcloud.png saved.")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("📊 Step 5: Plotting sentiment distribution...")
df = pd.read_csv("clean_reviews_labeled.csv")
plt.figure(figsize=(6, 4))
sns.countplot(x='predicted_sentiment', data=df, palette='pastel')
plt.title("Predicted Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Review Count")
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()
print("Step 5 complete: sentiment_distribution.png saved.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

print("🤖 Step 6: Training sentiment classification model...")
df = pd.read_csv("clean_reviews_labeled.csv")
df = df[df['sentiment_score'] != 'neutral']

vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
X = vectorizer.fit_transform(df['Text'].astype(str))
y = df['sentiment_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

print("💾 Step 7: All outputs (CSV and PNG) are saved automatically in earlier steps.")

# 💡 Step 8: Optional file downloads for Google Colab users
from google.colab import files

print("📦 Downloading processed and cleaned data...")

# Simplified fields are saved as the final emotional output (only emotions and text are retained)
df[['sentiment_score', 'Text']].to_csv("/content/processed_reviews.csv", index=False)

# Optional：Compressed version 
# df[['sentiment_score', 'Text']].to_csv("/content/processed_reviews.csv.gz", index=False, compression='gzip')

# Download the main processing results
files.download("/content/amazon_reviews_cleaned.csv")       
files.download("/content/processed_reviews.csv")            
# files.download("/content/processed_reviews.csv.gz")        

# Download the data files required for visualization
files.download("clean_reviews.csv")                 
files.download("clean_reviews_labeled.csv")       
files.download("wordcloud.png")                   
files.download("sentiment_distribution.png")

print("All files prepared and downloaded.")    
