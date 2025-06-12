## 🛒 Brazil E-Commerce Sales Intelligence Pipeline

## 📦 Project Overview  
This project analyzes Brazilian e-commerce data from Kaggle (Olist) and builds a full data intelligence pipeline.  
From structured data queries to Python-based analysis and BI dashboards, it demonstrates an end-to-end solution for e-commerce performance monitoring and optimization.

## 🎯 Business Objective  
To help e-commerce businesses and logistics teams gain insights into delivery efficiency, customer satisfaction, and product category performance.

## 🧱 Data Pipeline Architecture  
- **Data Source:** Olist Brazilian E-Commerce Dataset (Kaggle)  
- **SQL Query Layer:** SQLite to extract relational metrics across sellers, orders, payments, and reviews  
- **Python Processing:** Data cleaning, delay flagging, freight analysis (Google Colab)  
- **Visualization Layer:**  
  - Tableau: Product category distribution, review score heatmaps  
  - Power BI: Delivery delay vs. cost scatter plots, review timeline, payment type comparison  

## 🧰 Tech Stack  
- **Languages:** SQL (SQLite), Python (pandas, matplotlib)  
- **Platforms:** Google Colab, GitHub, Kaggle  
- **Visualization Tools:** Tableau Public, Power BI  
- **Data Size:** 100K+ orders, 50K+ customers, 120K+ reviews  

## 📊 Key Insights  
- 📦 Top-selling product categories by revenue and volume  
- 🚚 Freight cost vs. delivery delay correlation  
- 💬 Review score trends and patterns  
- 💰 Payment type behavior vs customer satisfaction  

## 📁 Repository Structure

、、、
01_brazil_ecommerce_data_pipeline
│
├── data/
│ ├── olist_raw_data.zip                   # Original Kaggle dataset (all CSVs)
│ └── olist_cleaned_final.zip              # Final cleaned dataset used for analysis
│
├── scripts/
│ ├── onlist_cleaned_dataset.sql           # SQL script for data extraction & cleaning
│ └── onlist_cleaned_dataset.python        # Python script for EDA & processing (Colab)
│
├── dashboard/
│ ├── brazil_ecommerce_dashboard.pbix      # Power BI dashboard file
│ ├── powerbi_dashboard.pbix.png           # Power BI dashboard preview image
│ ├── brazil_ecommerce_dashboard.twbx      # Tableau workbook file
│ └── tableau_dashboard.preview.png        # Tableau dashboard preview image
│
└── README.md                              # Full pipeline and documentation

、、、

## 🔗 GitHub Project  
[Click to view project](https://github.com/ZhengLyu-Data/Lvzheng-Wuhan-Data/tree/main/01_brazil_ecommerce_data_pipeline)

## 🧑‍💻 Author & Project Statement  
This project was independently designed, implemented, and documented by **Zheng Lyu** as part of a professional data engineering portfolio.  
It integrates structured querying, Python preprocessing, and dashboarding to demonstrate a complete retail intelligence pipeline.

## 📬 Contact  
For questions or collaboration opportunities, please connect via LinkedIn:  
[Zheng Lyu](https://www.linkedin.com/in/zheng-lyu-951295323/)
