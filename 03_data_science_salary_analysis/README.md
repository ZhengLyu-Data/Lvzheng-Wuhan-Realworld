
## 📊 Supply Chain Efficiency Dashboard

This project analyzes supply chain and logistics transaction data to uncover delivery performance patterns, cost structures, and customer behavior. It combines Python, SQL, Tableau, and Power BI to perform real-world data cleaning, operational insights extraction, and dashboard building. The project is tailored for showcasing technical competency in data roles such as analyst or BI developer.

---

## 🗂️ Project Structure

```
03_data_science_salary_analysis/
├── data/
│   ├── data_science_salaries_raw.csv                   # Original raw dataset
│   └── data_science_salaries_cleaned.csv               # Cleaned dataset used for analysis
├── scripts/
│   ├── data_science_dataset.sql                        # SQL Data extraction & transformation script
│   └── data_science_dataset.python                     # Python data cleaning script
├── dashboard/
│   ├── data_science_salary_dashboard.pbix              # Power BI dashboard file
│   ├── data_science_salary_dashboard.pbix.png          # Power BI dashboard preview image
│   ├── data_science_salary_dashboard.twbx              # Tableau workbook
│   └── data_science_salary_dashboard.preview.png       # Tableau dashboard screenshot
└── README.md
```

---

## 🧹 Data Cleaning

Performed in both SQL (SQLite) and Python (pandas):

- Removed missing or invalid entries
- Renamed columns for consistency
- Verified value ranges for all key metrics
- Final cleaned file: `data_science_salaries_cleaned.csv`

---

## 🔍 Key Insights

- 🚚 Shipment via ship is the most common mode (over 67%)
- 🏭 High importance products receive greater average discounts
- 📈 Higher customer ratings correlate with increased product costs
- 📞 Rating 2 customers require the least customer care interaction

---

## 📈 Power BI Dashboard

📁 File: `data_science_salary_dashboard.pbix`  
📷 Preview:  
![Power BI Dashboard Preview](data_science_salary_dashboard.pbix.png)

**Includes:**

- Top 15 Highest-Paid Data Roles (bar chart)
- Salary vs. Remote Ratio by Company Size (scatter chart)
- Top 10 countries by Average Data Salary (line chart)

> Open `.pbix` using Power BI Desktop to explore the interactive visuals.

---

## 📊 Tableau Dashboard

📁 File: `data_science_salary_dashboard.twbx`  
📷 Preview:  
![Tableau Dashboard Preview](data_science_salary.preview.png)

**Includes:**

- Shipment count by transport mode (bar chart)
- Average product cost by warehouse block (bar chart)
- Average customer care calls by customer rating (bar chart)

> Open `.twbx` using Tableau Public (free) or Tableau Desktop 2022.1+.

---

## 🛠️ Tools Used

- Python (pandas, CSV)
- SQL (SQLite)
- Tableau Public
- Microsoft Power BI

---

## 📬 Contact

Feel free to live Tableau/Power BI links or collaboration requests, feel free to reach out via likendin https://www.linkedin.com/in/zheng-lyu-951295323/.
