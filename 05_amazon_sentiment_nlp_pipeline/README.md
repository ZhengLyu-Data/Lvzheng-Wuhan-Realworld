## Overview

This project analyzes sentiment in Amazon product reviews using a full data engineering and NLP pipeline. The goal is to classify customer reviews into positive, neutral, or negative sentiment using TextBlob, and to visualize overall sentiment trends. The project demonstrates end-to-end data ingestion, text processing, and automated visualization.

## Data Visualization

This project does not use Tableau or Power BI. All visualizations are generated programmatically using Python libraries:
sentiment_distribution.png: a bar chart created with matplotlib showing counts of positive, neutral, and negative reviews.
wordcloud.png: a visual representation of the most frequently used words in the review texts, generated using the wordcloud library.
These visuals help users quickly understand the overall emotional tone of the product feedback.

## Data Architecture

Raw CSV (Amazon Reviews)
      ↓
Text Cleaning & Preprocessing (pandas)
      ↓
Sentiment Classification (TextBlob)
      ↓
Visualizations (matplotlib, wordcloud)

We chose Python and TextBlob due to their fast prototyping capabilities. The entire pipeline runs efficiently in Google Colab and is modular for future upgrades to more advanced NLP models (e.g., BERT).

## Prerequisites

Before running the project, ensure the following:
Python 3.x installed or use Google Colab
Clone this repository
Download the Kaggle dataset: Amazon Fine Food Reviews
Place Reviews.csv into the data/ directory

## How to Run This Project

Open terminal or Google Colab
Navigate to project directory:
cd 05_amazon_review_nlp
Run the sentiment pipeline script:
python scripts/analysis_pipeline.py
Output files will be generated:
Cleaned CSV: /data/amazon_reviews_cleaned.csv
Sentiment-labeled CSV: /data/clean_reviews_labeled.csv
Visuals: /visualizations/sentiment_distribution.png, wordcloud.png

## Lessons Learned

TextBlob is simple but limited; future versions should incorporate deep learning models.
Review scores and text polarity are not always aligned — combining both is more robust.
Preprocessing quality directly affects model output; consistent text normalization is critical.
For large datasets, sampling is a good tradeoff to avoid overloading runtime.

## Contact

Please feel free to contact me if you have any questions:
LinkedIn: Zheng Lyu
GitHub: ZhengLyu-Data
