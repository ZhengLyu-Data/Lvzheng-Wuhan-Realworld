## Overview

This project analyzes global data science salaries using real-world job data from Kaggle. The goal is to explore how salary varies by experience level, job title, and company location. The project demonstrates a full pipeline from raw data cleaning to structured insights.

## Data Visualization

Below are final visualizations generated in tabelau/ Power BI:

Power BI Dashboard

![Power BI dashboard image](data_science_salary_dashboard.pbix.png)

Tableau Dashboard

![Tableau dashboard image](data_science_salary_dashboard.twbx.png)

## Data Architecture


## Prerequisites

Before running this project, ensure the following are installed or available:

- Python 3.x (or Google Colab)
- Required libraries:
  - `pandas`
  - `numpy`

## How to Run This Project

- Upload the original dataset `data_science_salaries_raw.csv`
- Run the data cleaning script to generate `data_science_salaries_cleaned.csv`
- Run the analysis pipeline: bash python run_pipeline.py
- You will see the following results:

Salary by experience

Top-paying job titles

High-paying company locations

Download cleaned dataset for reuse or dashboarding

## 🎓 Lessons Learned

- Field naming standardization is key to reproducible workflows
- Mapping and grouping enables fast aggregation insights
- Python script modularization makes project easier to maintain
- Simple .groupby() operations can already deliver business value

## Contact
Feel free to reach out for collaboration or questions: LinkedIn: Zheng Lyu GitHub: ZhengLyu-Data
