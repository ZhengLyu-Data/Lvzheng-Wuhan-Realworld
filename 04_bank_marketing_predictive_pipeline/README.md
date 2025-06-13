## 🏦 Bank Marketing Predictive Pipeline

## 📦 Project Overview  
This project uses a real-world dataset from a Portuguese banking institution (via Kaggle) to build a predictive analytics pipeline.  
It combines data cleaning, feature engineering, and visual exploration to understand which customer profiles are most likely to respond to marketing campaigns.

## 🎯 Business Objective  
To support marketing teams in optimizing targeting strategies by identifying the characteristics of customers most likely to subscribe to a term deposit product.

## 🧱 Data Pipeline Architecture  
- **Data Source:** Bank Marketing Dataset (Kaggle)  
- **Python Processing:** Cleaning, encoding, feature engineering, response flagging (Google Colab)  
- **Modeling Layer:** Logistic regression (optional, for binary prediction)  
- **Visualization Layer:**  
  - Tableau: Campaign outcomes by job, age group, education  
  - Power BI: Customer profiles vs response ratio, contact method analysis

## 🧰 Tech Stack  
- **Languages:** Python (pandas, matplotlib, seaborn)  
- **Platforms:** Google Colab, GitHub, Kaggle  
- **Visualization Tools:** Tableau Public, Power BI  
- **Data Size:** 45K+ customer records, 17 features including job, age, contact type, campaign outcome

## 📊 Key Insights  
- ☎️ Contact type (cellular vs telephone) impacts subscription success  
- 🎓 Higher education and white-collar roles show stronger campaign responses  
- 🔁 Multiple contact attempts increase likelihood of customer conversion  

---

## 📁 Repository Structure

```
04_bank_marketing_predictive_pipeline/
├── data/
│ ├── bank_marketing_raw.csv                          # Original dataset from Kaggle
│ ├── bank_marketing_cleaned.csv                      # Cleaned dataset used for analysis
│ └── bank_additional_name.txt                        # optional reference only
├── scripts/
│ ├── bank_marketing_dataset.sql                      # SQL script for data extraction & cleaning
│ └── bank_marketing_dataset.python                   # Python notebook for preprocessing & insights
├── dashboard/
│ ├── bank_marketing_customer_behavior.pbix           # Power BI dashboard
│ ├── bank_marketing_customer_behavior.pbix.png       # Power BI dashboard preview image
│ ├── bank_marketing_customer_explorer.twbx           # Tableau workbook
│ └── bank_marketing_customer_explorer.twbx.png       # Tableau dashboard preview image
└── README.md                                         # Full pipeline and documentation
```

---


## 🔗 GitHub Project  
[Click to view project](github.com/ZhengLyu-Data/Lvzheng-Wuhan-Data/tree/main/04_bank_marketing_predictive_pipeline)

## 🧑‍💻 Author & Project Statement  
This project was independently developed by **Zheng Lyu** to demonstrate predictive modeling and response segmentation using marketing data.  
It reflects practical business applications of customer profiling and campaign targeting with BI dashboards.

## 📬 Contact  
For questions or collaboration opportunities, please connect via LinkedIn: [Zheng Lyu](https://www.linkedin.com/in/zheng-lyu-951295323/)
