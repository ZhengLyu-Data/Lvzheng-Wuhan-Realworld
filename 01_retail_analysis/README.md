## 📁 Project 01: Retail Sales Analysis

This project showcases a simulated end-to-end retail sales analysis pipeline, featuring data cleaning, trend visualization, regional and product-level insights, and a clean, cloud-based workflow. It demonstrates proficiency in Python, SQL, and Tableau.

## 📁 Project Structure
```
01_retail_analysis/
├── retail_sales_sample.csv         # Simulated raw retail sales data
├── cleaned_sales.csv               # Cleaned dataset ready for analysis
├── Notebook                        # Python analysis notebook (Colab-compatible)
├── tableau_screenshot.png          # Dashboard snapshot
└── README.md                       # Project documentation
```
## 📊 Project Overview

This project provides a foundational business insight into sales performance using a simulated retail dataset. The pipeline includes:

- Data cleaning using Python (Pandas)
- Trend visualization over time
- Geographic breakdown by country
- Product category contribution via bar and pie charts
- Dashboard publishing with Tableau Public

## 🧹 Data Cleaning Process

Key steps included:

- Removing duplicates and nulls
- Ensuring valid date formatting
- Creating a `TotalSales` column = `Quantity * UnitPrice`

The resulting dataset `cleaned_sales.csv` was exported and visualized using Tableau.

## 📈 Tableau Dashboard

The interactive dashboard includes:

1. **Monthly Sales Trend** – A line chart showing revenue over time  
2. **Sales by Country** – A bar chart colored by sales volume  
3. **Sales by Product** – A pie chart highlighting contribution by product

🔗 [View Published Tableau Dashboard](https://public.tableau.com/app/profile/zheng.lyu6601/viz/GlobalRetailAnalysis_17487317429280/GlobalRetailAnalysis)

## 💡 Highlights

100% cloud-native: No local setup needed
Strong use of Python + Tableau for end-to-end analysis
Easily expandable for time series forecasting or classification

## 🐍 Notebook Language Notice

The notebook file (Notebook.ipynb) in this project is written entirely in Python, executed via Google Colab in a cloud-based environment. 
All analysis, data cleaning, and visualization preparation were completed using standard Python libraries (such as pandas, matplotlib, etc.). 
This ensures accessibility and reproducibility for reviewers and collaborators without requiring local setup.

## 📌 About This Project

This is **Project 1 of 4** in my data career transition roadmap.  
🔗 [View all my projects on GitHub](https://github.com/ZhengLyu-Data/Lvzheng-Wuhan-Data)
