## 🗣️ Amazon Sentiment NLP Pipeline

This project builds a complete NLP pipeline to analyze sentiment in Amazon product reviews using real-world data from Kaggle. It demonstrates a full-stack data engineering workflow — from raw data ingestion, preprocessing, sentiment classification, to visualized insight delivery.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `analysis_pipeline.py` | All-in-one Python pipeline: cleaning, sentiment analysis, and visualization |
| `amazon_reviews_cleaned.csv` | Cleaned and preprocessed raw data (10,000 samples) |
| `processed_reviews.csv` | Final output with predicted sentiment labels |
| `clean_reviews.csv` | Filtered & cleaned review data |
| `clean_reviews_labeled.csv` | Labeled data for sentiment visualization |
| `wordcloud.png` | Word cloud of most common review terms |
| `sentiment_distribution.png` | Bar chart showing sentiment distribution |
| `pipeline.py` | Modular sentiment processing logic |
| `run_pipeline.py` | Script to execute the processing pipeline |
| `README.md` | This documentation file |

---

## 🔧 Technologies Used

- 🐍 Python 3
- `pandas`, `textblob` for data processing
- `matplotlib`, `wordcloud` for visualization
- Google Colab for runtime

---

## 📊 Workflow Overview

1. **Raw Data Cleaning**  
   - Select key columns, drop nulls  
   - Sample 10,000 reviews from full dataset  
   - Save as `amazon_reviews_cleaned.csv`

2. **Sentiment Mapping**  
   - Convert review `Score` to sentiment label: `positive`, `neutral`, `negative`
   - Use TextBlob to predict polarity from review text
   - Save full output as `processed_reviews.csv`

3. **Visualization**  
   - Generate word cloud: `wordcloud.png`  
   - Plot sentiment distribution bar chart: `sentiment_distribution.png`

---

## 🧠 Sentiment Mapping Rules

| Score | Mapped Sentiment |
|-------|------------------|
| 1–2   | negative          |
| 3     | neutral           |
| 4–5   | positive          |

---

## 🚀 How to Run

You can open and run the entire workflow using Google Colab:

```python
# Upload raw amazon_reviews_raw.csv to /content/
!python analysis_pipeline.py
It will produce all outputs automatically and allow you to download the files.

📌 Note
The original raw dataset is large (~500MB) and not included in this repo.

A cleaned 10,000-row sample is provided for demo and visualization purposes.

For full-scale processing, refer to the Kaggle dataset: Amazon Fine Food Reviews

📍 Author
This project was created by a transitioning data engineer targeting positions in Wuhan starting August 2025. It is part of a 5-project portfolio demonstrating end-to-end data processing, real-world analysis, and cloud-compatible tooling.

## 📬 Contact
For questions or collaboration opportunities, please connect via LinkedIn https://www.linkedin.com/in/zheng-lyu-951295323/.
