## Overview
This project explores salary trends in data science roles globally. It highlights differences based on job level, company size, and work flexibility using structured pipeline processing and visual outputs.

## Data Visualization

![matplotlib dashboard image](chart1_average_salary_by_experience_level.png)
![matplotlib dashboard image](chart2_remote_work_ratio_distribution.png)
![matplotlib dashboard image](chart3_salary_distribution_by_company_size.png)

## Data Architecture
![Data Architecture](data_salary_insight_pipeline_architecture.png)

## Prerequisites
- Python 3.10+
- pandas / matplotlib
- SQLite (optional for local storage)

## How to Run This Project
```bash
# Step 1: Clean the raw dataset
python clean_data.py

# Step 2: Build the analysis pipeline
python pipeline.py

# Step 3: Execute the pipeline
python run_pipeline.py

# Step 4: Review the output visuals (matplotlib charts)
```

## 🎓 Lessons Learned
- Position level has significant impact on salary
- Remote jobs have diversified distribution by region
- Company size affects salary dispersion

## 📬 Contact
For questions or feedback: Linkedin & Twitter 
