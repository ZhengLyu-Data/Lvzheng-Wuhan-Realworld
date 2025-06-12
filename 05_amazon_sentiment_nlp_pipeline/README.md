## 🛍️ Amazon Sentiment NLP Pipeline

## 📦 Project Overview
This project performs real-world sentiment analysis on Amazon product reviews using natural language processing (NLP) techniques. It builds a full data pipeline from text preprocessing to sentiment scoring and final visualization.

## 🎯 Business Objective
Help product teams identify customer satisfaction drivers and pain points through large-scale review mining and sentiment dashboards.

## 🧱 Data Pipeline Architecture
1. **Data Source:** Amazon Fine Food Reviews (Kaggle)
2. **Text Cleaning & Preprocessing:** Python (re, NLTK, stopwords, lemmatization)
3. **Sentiment Modeling:**
   - VADER for polarity scoring
   - TF-IDF for keyword extraction
4. **Dashboard Visualization:**
   - Word clouds for top positive/negative terms
   - Sentiment breakdown by product
   - Timeline of average sentiment scores

## 🧰 Tech Stack
- **Languages:** Python (NLTK, VADER, matplotlib, seaborn)
- **Platforms:** Google Colab, GitHub, Kaggle
- **Visualization:** Tableau Public (optional), Power BI
- **Data:** Amazon Fine Food Reviews dataset (500K+ samples)

## 📊 Key Insights
- Top phrases in 5-star vs 1-star reviews
- Sentiment intensity distribution
- Common customer complaints (negative TF-IDF terms)
- Time-based sentiment drift

## 📁 Repository Structure

```
├── data/
│   ├── amazon_reviews_raw Part 1.csv                       # Raw dataset CSV from Kaggle (500K reviews)
│   ├── amazon_reviews_raw Part 2.csv                        
│   ├── ...                         
│   ├── amazon_reviews_raw Part 23.csv:                         
│   ├── clean_reviews.csv:                                  # Load and Cleaned dataset (20,000 records)
│   └── clean_reviews_labeled.csv                           # Labeled dataset with sentiment predictions
├── script
│   └── amazon_sentiment_nlp_pipeline.python                # NLP + semtiment notebook (.ipynb)
├── dashboard
│   ├── wordcloud.png                                       # Visualization of key keywords based on TF-IDF
│   └── sentiment_distribution.png                          # Distribution of sentiment classes
└── README.md                                               # Project pipeline and structure
 
```

## 🔗 GitHub Project
[Click to view project](https://github.com/ZhengLyu-Data/Lvzheng-Wuhan-Data/tree/main/05_amazon_sentiment_nlp_pipeline)

## 🧑‍💻 Author & Project Statement
This project was independently designed, implemented, and documented by **Zheng Lyu** as part of a professional data engineering portfolio.  
It combines real-world data with end-to-end NLP pipelines and business-oriented dashboards.

## 📬 Contact
For questions or collaboration opportunities, please connect via LinkedIn https://www.linkedin.com/in/zheng-lyu-951295323/.
