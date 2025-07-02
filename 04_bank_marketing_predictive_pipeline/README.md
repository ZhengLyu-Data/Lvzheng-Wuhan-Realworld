## 中文说明（项目简介）
本项目基于葡萄牙银行营销数据，分析不同客户特征与联络方式对营销订阅成效的影响。通过 Python 数据处理与可视化，识别哪些用户群体对营销活动响应更积极，有助于银行精准营销策略制定。适合教学演示或面向商业分析岗位的项目展示。

## Overview
This project analyzes customer responses to a marketing campaign by a Portuguese bank. The goal is to identify which customer attributes and contact methods are associated with higher subscription rates.

**Dataset**: [Bank Marketing Dataset](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing), originally published on Kaggle.

##  Data Visualization
** 📝 中文说明：** 项目使用 Matplotlib 绘图展示了不同联络方式、客户年龄分布与教育程度在营销响应上的影响差异。

![matplotlib dashboard image](chart1_subscription_by_contact_type.png)
![matplotlib dashboard image](chart2_age_distribution_by_subscruption_status.png)
![matplotlib dashboard image](chart3_subscription_rate_by_education_level.png)

## Data Architecture
** 📝 中文说明：** 本项目构建了清洗 → 分析 → 输出的结构化数据管道，结合逻辑判断与可视化模型，为银行客户行为建模提供参考。

![Data Architecture](bank_marketing_predictive_architecture.png)

## Prerequisites
** 📝 中文说明：** 请准备 Python 环境（建议 3.10+），安装 pandas 与 matplotlib，如需执行 SQL 分析可选用 SQLite 环境。

- Python 3.10+
- pandas / matplotlib
- SQLite (optional for intermediate storage)

## How to Run This Project
** 📝 中文说明：** 本项目共含三个 Python 模块，运行顺序为：数据清洗 → 数据管道构建 → 输出分析图表，可用于教学与项目演示。

- Step 1: Clean the dataset
python clean_data.py

- Step 2: Build the pipeline
python pipeline.py

- Step 3: Run the full analysis
python run_pipeline.py

- Step 4: View visual outputs (matplotlib)

🧩 Note on SQL Compatibility:
All SQL scripts in this project are designed using standard SQL syntax. While executed with SQLite for simplicity, the same structure is compatible with MySQL or PostgreSQL by changing the database connector and placeholder syntax (`?` → `%s`).

## 🎓 Lessons Learned
** 📝 中文说明：** 本项目揭示了营销联络方式对转化率有显著影响，且客户年龄段与教育程度之间存在明显的响应偏好，可辅助优化目标人群筛选策略。

- Contact method plays a role in campaign success
- Younger and older demographics have distinct subscription patterns
- Education level correlates with campaign responsiveness
