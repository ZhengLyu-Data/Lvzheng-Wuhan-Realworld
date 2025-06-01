📁 Project 02: Supply Chain Dashboard

📝 Project Overview
This project focuses on building a supply chain dashboard based on delivery records. It visualizes key logistics metrics and explores cost vs. performance tradeoffs.

🛠️ Tools Used
Google Colab – Data cleaning and preparation

SQL Fiddle (MySQL) – Cloud-based SQL analysis

Tableau Public – Dashboard creation

GitHub – Version control and publishing

📊 Dataset Fields
Order ID

Origin and Destination

Transport Method

Distance (km)

Delivery Time (days)

Transport Cost (USD)

🧹 Data Preparation (Python)
Handled missing values and duplicates

Normalized column names

Exported cleaned dataset for further SQL/Tableau use

🔍 SQL Analysis (via SQL Fiddle)
Created table and inserted sample data

Ran queries to analyze:

Average delivery time per method

Top 3 most expensive delivery routes

Longest distances by origin

📄 Filename: Supply_Chain_Dashboard.sql

📈 Tableau Visualizations
Delivery Time by Method

Cost vs Distance

Origin-Destination Frequency

🔗 📊 View Tableau Dashboard

📁 Repository Structure
bash

02_supply_chain_dashboard/
├── supply_chain_dashboard.ipynb   # Data cleaning and export in Python
├── cleaned_supply_chain.csv       # Final cleaned dataset
├── Supply_Chain_Dashboard.sql     # Full SQL logic
├── tableau_screenshot.png         # Dashboard preview image
└── README.md                      # This documentation

💡 Highlights
Cross-tool workflow: Python + SQL + Tableau

Cloud-based query execution (SQL Fiddle)

Emphasis on delivery efficiency and cost insights
