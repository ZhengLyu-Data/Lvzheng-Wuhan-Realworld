## 📊 Global Sales Analysis Dashboard

This project analyzes global retail sales using Python, Tableau, Power BI, and SQL. The goal is to extract insights across regions, categories, and time trends to support business decisions.

## 📁 Dataset

The cleaned dataset contains order-level information including:

Order ID, Date

Region & Country

Product Category & Subcategory

Sales, Profit

File: cleaned_train.csv

## 🔧 Tools Used

# Tool                 # Purpose

# Python               # Data cleaning, CSV generation

# Tableau              # Trend and regional visualization

# Power BI             # KPIs, category analysis dashboard

# SQL (Programiz)      # Structured queries for aggregation

# GitHub               # Portfolio version control & hosting

## 📌 Deliverables

✅ Cleaned dataset cleaned_train.csv

✅ Tableau dashboard: global_sales_analysis_dashboard.png

✅ Power BI dashboard: global_sales_powerbi_dashboard.png

✅ SQL queries: project1_queries.sql + Markdown version

## 🧠 Key Visuals

📈 Tableau Dashboard: Global Sales Overview

Regional Sales Bar Chart

Profit Trend Line Chart

Category Distribution Pie Chart



## 📊 Power BI Dashboard: KPIs & Trends

KPI Cards: Total Sales, Avg Order Value

Bar Chart: Top Product Categories

Pie Chart: Category Distribution



## 🧮 SQL Summary (Run on Programiz)

-- Query: Monthly Sales Trend
SELECT
  SUBSTR(OrderDate, 1, 7) AS Month,
  SUM(TotalSales) AS MonthlySales
FROM cleaned_train
GROUP BY Month
ORDER BY Month;

-- Query: Top 2 Best-Selling Categories
SELECT Product_Category, SUM(TotalSales) AS TotalSales
FROM cleaned_train
GROUP BY Product_Category
ORDER BY TotalSales DESC
LIMIT 2;

## 📝 Resume Bullet (English)

Global Sales Dashboard ProjectCleaned international sales data using Python and designed dashboards in Tableau and Power BI. Created structured SQL queries to analyze sales trends and product performance across categories and regions.

## 📄 Resume Project Description (English)

Global Sales Dashboard ProjectCleaned international sales data using Python and created visual dashboards in Tableau and Power BI. Used SQL to extract monthly sales trends, top-selling product categories, and average order values for executive insights.

## 📎 Author

Zheng Lyu | Data Analyst CandidateGitHub: github.com/ZhengLyu-Data
