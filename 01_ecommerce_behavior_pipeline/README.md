🛒 E-commerce Behavior Pipeline
This project builds a complete customer behavior analysis pipeline using real-world Brazil e-commerce data from Kaggle. It demonstrates a full-stack data engineering workflow — from raw data ingestion, preprocessing, behavioral aggregation, to visualized insight delivery.

📁 Project Structure
File	Description
preprocessing.py	All-in-one Python script: cleaning, timestamp processing, aggregation
ecommerce_raw.csv	Original e-commerce dataset (from Kaggle)
ecommerce_cleaned.csv	Cleaned and preprocessed data for visualization
ecommerce_behavior.pbix	Final Power BI dashboard file
preview_top_customers.png	Bar chart of top 10 customers by revenue
preview_product_ranking.png	Ribbon chart of product quantity rankings over time
preview_customer_matrix.png	Matrix chart of customer monthly activity
README.md	This documentation file

🔧 Technologies Used
🐍 Python 3

pandas, numpy for data transformation

Power BI Desktop for interactive dashboarding

Google Colab for cloud-based Python execution

📊 Workflow Overview
Raw Data Cleaning

Drop missing and duplicate values

Convert InvoiceDate to datetime

Normalize categorical fields like CustomerID, Description, Country

Save as ecommerce_cleaned.csv

Behavior Aggregation

Calculate total order value (Price × Quantity) per customer

Rank product sales trends across time

Track customer engagement frequency by month

Visualization

Load cleaned data into Power BI

Build 3 core dashboard views:

Top customers

Product trends

Monthly customer activity

Export preview charts for documentation

🧠 Behavior Mapping Dimensions
Entity	Metric Tracked
Customer	Total Order Value, Activity by Month
Product	Quantity Sold Over Time
Time	Daily and Monthly Order Trends

📊 Dashboard Components
Chart	Title	Type	Description
🟦 Chart 1	Top 10 Customers by Total Order Value	Bar Chart	Ranks highest-spending customers in descending order
🟧 Chart 2	Product Sales Ranking Over Time	Ribbon Chart	Visualizes product quantity rankings by month
🟣 Chart 3	Customer Order Activity by Month	Matrix Table	Shows how frequently each customer places orders per month

🚀 How to Run
You can open and run the entire workflow using Google Colab and Power BI Desktop:

python

# Step 1: Upload ecommerce_raw.csv to /content/
!python preprocessing.py
This will generate ecommerce_cleaned.csv for Power BI import.

Then open the file ecommerce_behavior.pbix using Power BI Desktop. All charts are pre-built and filtered. You may adjust product/customer/time filters as needed.

📌 Note
The original raw dataset is sourced from Kaggle: Brazilian E-Commerce Public Dataset.
It contains over 100K orders from multiple CSVs. We use a cleaned and flattened version for demo purposes.

All visualizations are reproducible from the public dataset with the included script.

📍 Author
This project was created by a transitioning data engineer targeting positions in Wuhan starting August 2025. It is part of a 5-project portfolio demonstrating end-to-end data processing, real-world analytics, and cloud-compatible tooling.

📬 Contact
For questions or collaboration opportunities, please connect via LinkedIn:
👉 linkedin.com/in/zheng-lyu-951295323
