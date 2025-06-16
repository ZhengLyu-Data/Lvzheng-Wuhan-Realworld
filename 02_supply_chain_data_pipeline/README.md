## Overview

This project analyzes a retail supply chain dataset to extract insights about shipping mode, cost structure, and delivery performance. It includes data cleaning, statistical analysis in Python, and interactive dashboards built with Power BI and Tableau.

## Data Visualization

## Power BI Dashboard

- Product Cost by Shipping Mode (Bar Chart)
- Discount by Product Importance (Ribbon Chart)
- Customer Rating vs Product Cost (Line Chart)

## Tableau Dashboard

- Distribution of Product Cost by Shipment Mode (Bar)
- Average Discount vs Product Importance (Bar)
- Top 10 Products by Total Revenue (Bar)

![Power BI dashboard image](supply_chain_dashboard.pbix.png)  
![Tableau](dashboard/tableau_dashboard.png)

---

## Data Architecture

![Architecture Diagram](dashboard/supply_chain_architecture.png)

---

## Prerequisites

Before running the analysis:

- Python 3.x (or Google Colab)
- Install required libraries:
  ```bash
  pip install pandas
- Place supply_chain_raw.csv in your working directory

## How to Run This Project
Clean the raw dataset:

- from clean_data import clean_supply_chain_data
- df_clean = clean_supply_chain_data("supply_chain_raw.csv")
- df_clean.to_csv("supply_chain_cleaned_by_python.csv", index=False)
- Run the analysis:

- from pipeline import process_data
- df = pd.read_csv("supply_chain_cleaned_by_python.csv")
- results = process_data(df)
- View insights:

results["avg_cost_by_mode"]

results["avg_discount_by_importance"]

results["correlation_rating_cost"]

Open Power BI or Tableau to visualize the final results using the cleaned CSV.

## Lessons Learned
Data normalization is crucial for cross-platform dashboard integration

Customer rating is weakly correlated with product cost in this dataset

Ribbon chart helps better visualize importance-driven discount patterns

Power BI and Tableau complement each other in flexibility and precision

## Contact
Created by Zheng Lyu

View all projects: ZhengLyu-Data GitHub
