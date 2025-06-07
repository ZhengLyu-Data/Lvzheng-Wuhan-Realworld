
## Project Title: Amazon Review Sentiment Analysis System

## Folder Name: 05_amazon_review_nlp

## Dataset Description:
- Raw Data File: amazon_reviews_raw.csv (not uploaded due to large size)
- Cleaned Data File: clean_reviews.csv (sampled and cleaned text data)
- Labeled Data File: clean_reviews_labeled.csv (includes sentiment predictions)
- Visualization Files: wordcloud.png, sentiment_distribution.png

## Tools Used:
Python + Pandas + TextBlob + Scikit-learn + Matplotlib + WordCloud

## Data Source:
[Kaggle - Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)

## Project Overview:

This project focuses on Natural Language Processing (NLP) applied to real-world e-commerce customer reviews. The goal is to clean and analyze review texts, perform sentiment classification, and visualize key insights.

Key steps in the analysis:
1. Load and sample 20,000 reviews from the original Amazon dataset (~500,000 records)
2. Clean text fields using Pandas
3. Predict sentiment (positive / neutral / negative) using TextBlob
4. Generate a keyword word cloud using TF-IDF scores
5. Plot a sentiment distribution chart
6. Build a logistic regression classifier using TF-IDF vectors

This project was developed entirely in Python and is suitable for demonstrating entry-level NLP and data engineering skills in a job application.
