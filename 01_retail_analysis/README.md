# 🛍️ Project 01: Retail Sales Analysis

## 📌 Overview
This project presents a complete pipeline for analyzing simulated retail sales data. From data preprocessing to visualization, it demonstrates how retail performance can be tracked and understood using Python and Tableau.

## 📁 Folder Structure
```
01_retail_analysis/
│
├── retail_analysis.ipynb          # Python notebook for data cleaning and processing
├── retail_sales_sample.csv        # Simulated raw dataset
├── cleaned_sales.csv              # Cleaned dataset used in Tableau
├── SalesTrends.png                # Screenshot of Tableau chart 1
├── SalesByCountry.png             # Screenshot of Tableau chart 2
├── SalesByProduct.png             # Screenshot of Tableau chart 3
├── GlobalRetailDashboard.png      # Screenshot of final dashboard
└── README.md                      # Project documentation
```

## 🧹 Data Cleaning
- Removed duplicates and null values
- Converted `OrderDate` to datetime
- Calculated total sales by multiplying `Quantity` and `UnitPrice`

## 📊 Tableau Visualizations
| Chart | Description |
|-------|-------------|
| 📈 **Sales Trends** | Line chart showing monthly sales trends |
| 📊 **Sales by Country** | Colored bar chart comparing total sales by country |
| 🧾 **Sales by Product** | Pie chart summarizing total sales by product |

View the dashboard here: [Global Retail Dashboard](https://public.tableau.com/app/profile/zheng.lyu6601/viz/GlobalRetailAnalysis_17487317429280/GlobalRetailAnalysis)

## 💬 Notebook Language Notice
Due to platform limitations, the notebook filename remains `retail_analysis.ipynb`. The entire content is written in English to maintain consistency with other projects and job application materials.
