## Overview

This project analyzes sentiment in Amazon food product reviews using natural language processing (NLP). It classifies reviews as positive, neutral, or negative using TextBlob and visualizes the results using Python libraries. The pipeline demonstrates data ingestion, preprocessing, sentiment analysis, and visualization.

## Data Visualization

Below are screenshots of the final visualizations:

Sentiment Distribution ![Tableau dashboard image](sentiment_distribution.png)

Word Cloud ![Tableau dashboard image](wordcloud.png)

## Data Architecture

![data_architecture image](amazon_sentiment_nlp_architecture.png)

## Prerequisites

- Before running the project, ensure the following: Python 3.x installed (or use Google Colab)
- Install required libraries: pandas, numpy, textblob, matplotlib, wordcloud
- Place Reviews.csv into the data/ directory

## How to Run This Project

- Open terminal or Google Colab
- Navigate to the project folder: cd 05_amazon_review_nlp

## Run the analysis pipeline:

- python scripts/analysis_pipeline.py
- Outputs will be saved to:
- Labeled reviews: /data/clean_reviews_labeled.csv
- Word cloud and sentiment distribution plots: /visualizations/

## Lessons Learned

- Rule-based sentiment classification (TextBlob) is fast and easy, but less accurate than ML model
- Combining score fields and polarity improves label consistency
- Creating the dataset is essential for fast prototyping and visualization
- Python scripting enables modular and reproducible NLP workflows

## Contact
Please feel free to contact me if you have any questions: Linkedin, Twitter
