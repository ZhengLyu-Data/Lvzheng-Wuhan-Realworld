## 📊 Brazil E-Commerce Sales Intelligence

This project analyzes real-world e-commerce data from Brazil (Olist) using SQL, Python, Tableau, and Power BI.  
It demonstrates data cleaning, transformation, and insightful visualization to showcase business performance and customer behavior.

---

## 📁 Project Structure

```
01_brazil_e-commerce_sales_intelligence/
├── data/
│   ├── olist_raw_data.zip                # Merged raw data
│   └── olist_cleaned_final.zip           # Cleaned dataset used for analysis
├── scripts/
│   ├── clean_data.sql                    # SQL data cleaning script
│   └── clean_data.py                     # Python data cleaning script
├── dashboard/
│   ├── powerbi_dashboard.pbix            # Power BI dashboard file
│   ├── powerbi_dashboard.pbix.png        # Power BI dashboard preview image
│   ├── tableau_dashboard_link.txt        # Tableau Public URL
│   └── tableau_dashboard_preview.png     # Tableau dashboard screenshot
└── README.md
```

---

## 🧼 Data Cleaning

Two cleaning pipelines were implemented:

- ✅ `clean_data.sql`: SQL version for relational environments
- ✅ `clean_data.py`: Python script using pandas

Cleaning steps included:

- Filtering null or invalid values
- Joining multiple tables
- Creating `purchase_month` and `delivery_days` fields
- Preparing the final dataset for BI tools

---

## 📦 Data Files

- `olist_raw_data.zip`: contains the merged raw file `onlist_merged_raw.csv`
- `olist_cleaned_final.zip`: the final cleaned dataset used for Tableau and Power BI

Note: Files are compressed due to GitHub size limits.

---

## 📊 Visualizations

### ✅ Tableau Dashboard

> **Brazil E-Commerce Sales Intelligence**  
🔗 [View on Tableau Public](https://public.tableau.com/app/profile/zheng.lyu6601/viz/BrazilE-CommerceSalesIntelligence/BrazilE-CommerceSalesIntelligence)

**Includes:**
- Monthly Sales Trend
- Top Product Categories by Sales
- Review Score Distribution

📷 Preview:  
![Tableau Dashboard Preview](dashboard/tableau_dashboard_preview.png)

---

### ✅ Power BI Dashboard

> File: `powerbi_dashboard.pbix`

**Includes:**
- Monthly Sales Trend
- Top 12 Product Categories by Sales
- Review Score Distribution

📷 Preview:  
![Power BI Dashboard Preview](dashboard/powerbi_dashboard.pbix.png)

---

## ✅ Tools Used

- SQL (SQLite / SQLFiddle)
- Python (pandas, CSV)
- Tableau Public
- Power BI Desktop

---

## 🏁 Outcome

This project demonstrates practical data analysis and visualization skills based on a real e-commerce dataset.  
It is designed for portfolio use and job interviews targeting roles in:

- Data Analysis
- Business Intelligence
- Entry-Level Data Science
