## 📦 Supply Chain Product & Shipping Dashboard

This project analyzes supply chain performance using real-world simulation data. The focus is on product sales, shipping efficiency, cost analysis, and logistics metrics across categories and carriers.

## 📁 Dataset

The project uses cleaned data sourced from Kaggle, exported into six separate tables:

product_summary.csv

shipping_summary.csv

distance_cost_analysis.csv

top_products_by_volume.csv

shipping_time_per_carrier.csv

product_category_distribution.csv

Original file: Clean_supply_chain.xlsx

## 🔧 Tools Used

Tool

Purpose

Python

Data cleaning, CSV segmentation

Tableau

Visual dashboard (multi-chart product insights)

Power BI

Carrier analysis, KPI reports

SQL

Aggregation queries (shipping cost, performance)

GitHub

Version control and portfolio publishing

## 📌 Deliverables

✅ Cleaned and split dataset (6 CSVs)

✅ Tableau dashboard: supply_chain_dashboard_tableau.png

✅ Power BI dashboard: supply_chain_dashboard_powerbi.png

✅ SQL queries: project2_queries.sql + Markdown version

📈 Tableau Dashboard

Dashboard Title: Supply Chain Product & Shipping Insights

Product Volume & Type (Bar & Donut Charts)

Shipping Carrier Time & Cost

Scatter Plot for Distance vs Cost

## 📊 Power BI Dashboard

Three analytical pages:

Product KPIs & Category Trend

Shipping Carrier Time & Cost

Logistics Efficiency by Mode & Route

## 🧮 SQL Sample

-- Join shipping carrier mapping from orders and supply chain
SELECT 
    sc.product_id,
    sc.product_name,
    sc.product_type,
    sc.units_sold,
    sc.shipping_carrier,
    sc.shipping_cost,
    sc.shipping_time,
    o.shipping_distance
FROM supply_chain sc
JOIN orders o
  ON sc.shipping_carrier = 
     CASE 
         WHEN o.carrier_code = 'Carrier A' THEN 'DHL'
         WHEN o.carrier_code = 'Carrier B' THEN 'FedEx'
         WHEN o.carrier_code = 'Carrier C' THEN 'UPS'
     END;

-- Cost Efficiency by Route
SELECT 
    routes, 
    ROUND(AVG(shipping_costs / shipping_distance), 2) AS cost_per_km
FROM shipping_summary
GROUP BY routes;

-- Cost Efficiency by Route
SELECT routes, ROUND(AVG(shipping_costs / shipping_distance), 2) AS cost_per_km
FROM shipping_summary
GROUP BY routes;

## 📝 Resume Bullet (English)

Supply Chain Dashboard ProjectBuilt end-to-end analytics workflow for supply chain performance using Python, SQL, Tableau, and Power BI. Segmented and visualized real-world shipping and sales data across multiple dimensions to reveal carrier efficiency, product trends, and logistics costs.

## 📄 Resume Project Description (English)

Supply Chain Analytics ProjectUsed Python to preprocess and split Kaggle-based supply chain data. Executed SQL joins to map carriers to shipment details and calculated route-level cost efficiencies. Built multi-layered dashboards in Tableau and Power BI to visualize category-level sales, shipping time, and logistics performance.

## 📎 Author

Zheng Lyu | Data Analyst CandidateGitHub: github.com/ZhengLyu-Data

