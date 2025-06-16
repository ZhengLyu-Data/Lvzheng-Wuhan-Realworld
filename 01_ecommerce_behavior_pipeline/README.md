## E-commerce Behavior Pipeline
🧠 Overview
This project analyzes customer transaction behavior using the UCI Online Retail II dataset. It demonstrates an end-to-end data engineering pipeline from raw data preprocessing in Python to interactive visual analysis in Power BI.

The goal is to identify high-value customers, understand product performance trends, and detect seasonal ordering patterns.

## 🧱 Architecture

Raw Excel (.xlsx)
      ↓
Python ETL (preprocessing.py)
      ↓
Cleaned CSV
      ↓
Power BI Dashboard (.pbix)

## 🧰 Tools & Technologies
Layer	Tools Used
Data Source	UCI Online Retail II (via Kaggle)
ETL	Python (pandas, numpy)
Storage	CSV
BI / Viz	Power BI Desktop
Platform	Google Colab, GitHub

## 📦 Dataset
Source: Online Retail II UCI Dataset

File: online_retail_II.xlsx

Coverage: 2010–2011 transactions across multiple countries (mainly UK)

Fields Used:

Invoice, Customer ID, Invoice Date, Description, Country, Quantity, Price

## ⚙️ Data Pipeline Steps
1. Data Ingestion
Load Excel file (online_retail_II.xlsx)

Convert to pandas DataFrame

Select core columns needed for behavioral analysis

2. Data Cleaning
Remove nulls and duplicates

Filter out refunds or canceled invoices

Convert InvoiceDate to datetime

Save cleaned result to ecommerce_cleaned.csv

3. Aggregation (Python)
Compute total value: Price × Quantity

Group by Customer ID, Product, InvoiceDate (Month)

Generate summary table for dashboarding

4. Visualization (Power BI)
Import cleaned CSV into Power BI

Build three visual components:

Top 10 customers by revenue

Monthly product ranking (quantity)

Customer order frequency matrix

## 📊 Dashboard Components
Chart	Title	Type	Description
🟦 Chart 1	Top 10 Customers by Revenue	Bar Chart	Ranks top-spending customers using total purchase value
🟧 Chart 2	Product Quantity Ranking Over Time	Ribbon Chart	Visualizes top-selling products by month
🟣 Chart 3	Customer Order Activity by Month	Matrix Table	Displays order frequency across customers and months

📝 Note: A geographic sales map (Chart 4) was planned but not included in this version.

---
、、、
## 🧪 Project Structure

01_ecommerce_behavior_pipeline/
│
├── data/
│   ├── online_retail_II.xlsx
│   └── ecommerce_cleaned.csv
│
├── scripts/
│   └── preprocessing.py
│
├── dashboard/
│   ├── ecommerce_behavior.pbix
│   ├── preview_top_customers.png
│   ├── preview_product_ranking.png
│   └── preview_customer_matrix.png
│
└── README.md
、、、

---


## ▶️ How to Run
Upload raw file online_retail_II.xlsx to /data/

Execute data cleaning script:

python scripts/preprocessing.py
Open ecommerce_behavior.pbix in Power BI Desktop

Refresh and interact with filters (e.g., by month, customer)

## 📌 Notes
This project uses a filtered version of the UCI Online Retail II dataset for demonstration.

Power BI charts are built-in with no additional DAX.

Aggregations are pre-computed via Python to ensure performance.

## 👤 Author
Created by Zheng Lyu, a transitioning data engineer targeting roles in Wuhan starting August 2025.
This is part of a 5-project portfolio showcasing real-world, end-to-end data workflows using cloud-compatible tooling.
