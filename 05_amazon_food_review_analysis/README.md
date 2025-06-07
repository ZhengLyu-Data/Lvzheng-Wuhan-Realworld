## Amazon Review Sentiment Analysis

This project analyzes customer product reviews from the Amazon Fine Food Reviews dataset using natural language processing (NLP) techniques. The objective is to clean the raw text data, predict sentiment (positive/neutral/negative), visualize insights, and build a simple classification model.

---

## Project Structure

```

├── amazon_review_nlp_analysis_colab_final.ipynb`: Jupyter Notebook containing the complete analysis workflow
├── amazon_reviews_raw.csv: Raw dataset (not uploaded due to size, available on Kaggle)
├── clean_reviews.csv: Cleaned and sampled data (20,000 records)
├── clean_reviews_labeled.csv`: Labeled dataset with sentiment predictions
├── wordcloud.png: Visualization of key keywords based on TF-IDF
├── sentiment_distribution.png`: Distribution of sentiment classes
├── README.md: Project documentation
```

---

## Data Cleaning

- Removed null entries and unnecessary columns
- Standardized text to lowercase and removed punctuation/special characters
- Sampled 20,000 reviews from the full dataset (~500,000 rows)
- Exported cleaned and labeled data for modeling

---

## Key Insights

- Majority of reviews in the dataset are positive
- TextBlob provides an efficient way to label sentiment with minimal configuration
- Logistic regression based on TF-IDF features achieved meaningful performance for binary classification (positive vs. negative)
- Visualizations such as word clouds and sentiment distribution help interpret the data effectively

---

## Tools Used
- Python
- Pandas
- TextBlob
- Scikit-learn
- Matplotlib
- WordCloud

---

## Contact
For questions or collaboration opportunities, please connect via LinkedIn https://www.linkedin.com/in/zheng-lyu-951295323/.
