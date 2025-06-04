# 🚚 Project 02: Supply Chain Dashboard

## 📌 Overview
This project analyzes a simulated supply chain dataset, demonstrating key skills in data preprocessing, SQL analytics, and business dashboard design using Python, SQL Fiddle, and Tableau.

## 📁 Folder Structure
```
02_supply_chain_dashboard/
│
├── supply_chain_dashboard.ipynb     # Python notebook for data cleaning and preparation in Google Colab
├── supply_chain_sample.csv          # Simulated raw dataset
├── cleaned_supply_chain.csv         # Cleaned dataset used in Tableau
├── supply_chain_dashboard.sql       # Combined SQL queries used for analysis (SQL Fiddle-compatible)
├── SupplyChainDashboard.png         # Screenshot of final dashboard
└── README.md                        # Project documentation
```

## 🧹 Data Cleaning
- Removed nulls and duplicates
- Renamed and standardized field names
- Calculated metrics like `InventoryTurnover`, `DeliveryRate`, etc.

## 🧮 SQL Queries
SQL queries were executed on [SQL Fiddle](https://sqlfiddle.com) to simulate warehouse-level analytics. All queries are provided in `supply_chain_dashboard.sql`.

## 📊 Tableau Visualizations
| Chart | Description |
|-------|-------------|
| 📦 **Inventory Levels** | Monthly stock levels by product |
| 🚚 **Fulfillment Rates** | On-time delivery rate across vendors |
| 🏭 **Supplier Performance** | Horizontal bars comparing supplier efficiency |

View the dashboard here: [Supply Chain Dashboard](https://public.tableau.com/app/profile/zheng.lyu6601/viz/SupplyChainDashboard_17487579608020/SupplyChainDashboard) 📌 The dashboard was created and published using Tableau Public.

## 💬 Notebook Language Notice
The notebook file `supply_chain_dashboard.ipynb` is fully written in English for consistency with professional standards.
