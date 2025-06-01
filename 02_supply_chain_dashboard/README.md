# 📦 02 Supply Chain Dashboard

This project demonstrates a full data analysis pipeline for a simulated supply chain dataset. It covers data cleaning in Python, SQL querying for business insights, and a professional dashboard created in Tableau. This project showcases my ability to work across multiple platforms and tools commonly used in data roles.

---

## 🔧 Tools Used

- **Python (Google Colab)** – Data cleaning and preprocessing  
- **SQL (SQL Fiddle)** – Query logic verification and aggregation  
- **Tableau Public** – Interactive dashboard and visual storytelling  
- **GitHub** – Project version control and portfolio publishing

---

## 📁 Project Structure

02_supply_chain_dashboard/
├── supply_chain_sample.csv # Original raw data
├── cleaned_supply_chain.csv # Cleaned dataset for visualization
├── Notebook.ipynb # Python (Colab) cleaning script
├── supply_chain_dashboard.sql # Final SQL analysis queries
├── tableau_screenshot.png # Dashboard screenshot
└── README.md # Project documentation

---

## 📊 Tableau Dashboard

🔗 [View Dashboard on Tableau Public](https://public.tableau.com/app/profile/zheng.lyu6601/viz/SupplyChainDashboard_17487579608020/SupplyChainDashboard)

### Dashboard Includes:
1. 📈 **Monthly Order Trend**
2. 📦 **Top-Selling Products by Revenue**
3. 🌍 **Orders by Region**

---

## 🧪 SQL Analysis Example

```sql
SELECT Product, SUM(Quantity * UnitPrice) AS TotalRevenue
FROM supply_chain_data
GROUP BY Product
ORDER BY TotalRevenue DESC;
✅ Full SQL queries are available in the supply_chain_dashboard.sql file.

📓 Notebook Format Notice
The data cleaning was performed in Google Colab, and the notebook file is saved as supply_chain_dashboard.ipynb. It is compatible with any Jupyter-based environment.

💡 Key Takeaways
Cleaned raw supply chain data and handled missing or invalid entries

Used SQL to derive product- and region-level insights

Built a multi-visualization Tableau dashboard

Practiced a real-world workflow involving cross-platform integration

📌 About This Project
This is Project 2 of 4 in my data career transition roadmap.
🔗 View all my projects on GitHub

💡 Highlights

Cross-tool workflow: Python + SQL + Tableau
Cloud-based query execution (SQL Fiddle)
Emphasis on delivery efficiency and cost insights

🐍 Notebook Language Notice

The notebook file (Notebook.ipynb) in this project is written entirely in Python, executed via Google Colab in a cloud-based environment. 
All analysis, data cleaning, and visualization preparation were completed using standard Python libraries (such as pandas, matplotlib, etc.). 
This ensures accessibility and reproducibility for reviewers and collaborators without requiring local setup.


