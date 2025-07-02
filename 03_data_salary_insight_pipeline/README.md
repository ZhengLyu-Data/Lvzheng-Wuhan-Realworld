## 中文说明（项目简介）
本项目分析了全球范围内数据科学岗位的薪资趋势。通过 Python 数据管道处理，结合 Matplotlib 图表可视化，揭示了不同职位级别、公司规模与远程工作比例下的薪资差异。项目展示了清洗 → 分析 → 可视化的完整流程，适合教学演示与求职展示。

## Overview
This project explores salary trends in data science roles globally. It highlights differences based on job level, company size, and work flexibility using structured pipeline processing and visual outputs.

## Data Visualization
** 📝 中文说明：** 本项目使用 Matplotlib 绘制图表，展示了平均薪资与职位经验等级、远程办公比例分布、不同公司规模下的薪资差异。

![matplotlib dashboard image](chart1_average_salary_by_experience_level.png)
![matplotlib dashboard image](chart2_remote_work_ratio_distribution.png)
![matplotlib dashboard image](chart3_salary_distribution_by_company_size.png)

## Data Architecture
** 📝 中文说明：** 本项目采用模块化 Python 脚本进行数据清洗与管道构建，并通过 Matplotlib 输出静态可视化图像，体现工程结构与教学演示兼容性。

![Data Architecture](data_salary_insight_pipeline_architecture.png)

## Prerequisites
** 📝 中文说明：** 请使用 Python 3.10 或以上版本，项目依赖 Pandas 和 Matplotlib。若需使用 SQL 脚本分析，可选用 SQLite 环境。

- Python 3.10+
- pandas / matplotlib
- SQLite (optional for local storage)

## How to Run This Project
** 📝 中文说明：** 依次运行三个 Python 脚本，先进行数据清洗，再构建分析流程，最终输出图像。建议使用 VS Code 或 Colab 执行查看。

- Step 1: Clean the raw dataset
python clean_data.py

- Step 2: Build the analysis pipeline
python pipeline.py

- Step 3: Execute the pipeline
python run_pipeline.py

- Step 4: Review the output visuals (matplotlib charts)

🧩 Note on SQL Compatibility:
All SQL scripts in this project are designed using standard SQL syntax. While executed with SQLite for simplicity, the same structure is compatible with MySQL or PostgreSQL by changing the database connector and placeholder syntax (`?` → `%s`).

## Lessons Learned
** 📝 中文说明：** 本项目发现职位等级对薪资影响显著，远程办公趋势因地区而异，公司规模对薪资离散度也有重要影响。
- Position level has significant impact on salary
- Remote jobs have diversified distribution by region
- Company size affects salary dispersion
