## Overview

This project analyzes a real-world bank marketing dataset to identify which customer segments are more likely to respond positively to marketing campaigns. The pipeline includes data cleaning, feature standardization, and statistical aggregation using Python. Final insights are visualized using Tableau and Power BI dashboards.

### Data Visualization

Final insights are displayed via interactive dashboards in Tableau and Power BI:

![Tableau Dashboard](dashboard/tableau_bank_response.png)  
![Power BI Dashboard](bank_marketing_customer_behavior.pbix.png)

### Data Architecture

![Data Architecture](dashboard/data_architecture.png)

## Prerequisites

Before running the project, ensure the following:

- Python 3.x installed (or use Google Colab)
- Required libraries: `pandas`
- Place `bank_marketing_raw.csv` into the root directory

---

# How to Run This Project

You can either run the pipeline locally or in Colab.

- Upload the raw dataset file:  
   `bank_marketing_raw.csv`

- Clean the data:
   ```python
   from clean_data import clean_bank_data
   df_cleaned = clean_bank_data("bank_marketing_raw.csv")

- Run the analysis:
 from pipeline import analyze_marketing_data
 results = analyze_marketing_data(df_cleaned)
 Save the cleaned file:

 df_cleaned.to_csv("bank_marketing_cleaned.csv", index=False)
 (Optional) Download file in Colab:

 from google.colab import files
 files.download("bank_marketing_cleaned.csv")

## Lessons Learned

Using .groupby() and .value_counts() enables quick distribution analysis across dimensions
Standardizing field names in early steps reduces downstream errors
Visual segmentation by customer traits improves marketing targeting decisions
Python’s modular scripting makes the entire pipeline reusable and extendable

## Contact
For any questions, feel free to connect: LinkedIn: Zheng Lyu GitHub: ZhengLyu-Data
