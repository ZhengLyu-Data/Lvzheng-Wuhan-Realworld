

## Overview
This project analyzes customer responses to a marketing campaign by a Portuguese bank. The goal is to identify which customer attributes and contact methods are associated with higher subscription rates.

**Dataset**: [Bank Marketing Dataset](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing), originally published on Kaggle.

##  Data Visualization

![matplotlib dashboard image](chart1_subscription_by_contact_type.png)
![matplotlib dashboard image](chart2_age_distribution_by_subscruption_status.png)
![matplotlib dashboard image](chart3_subscription_rate_by_education_level.png)

## Data Architecture
![Data Architecture](bank_marketing_predictive_architecture.png)

## Prerequisites
- Python 3.10+
- pandas / matplotlib
- SQLite (optional for intermediate storage)

## How to Run This Project
```bash
# Step 1: Clean the dataset
python clean_data.py

# Step 2: Build the pipeline
python pipeline.py

# Step 3: Run the full analysis
python run_pipeline.py

# Step 4: View visual outputs (matplotlib)
```

## 🎓 Lessons Learned
- Contact method plays a role in campaign success
- Younger and older demographics have distinct subscription patterns
- Education level correlates with campaign responsiveness

## 📬 Contact
For questions or collaboration: linkedin & Twitter
