## 中文说明（项目简介）
本项目基于 UCI Online Retail II 数据集，分析线上客户的购买行为。通过 Python 进行数据清洗与处理，结合 Power BI 和 Tableau 构建交互式可视化仪表板，帮助识别高价值客户、热销产品及购买模式。项目展示了完整的数据工程与业务分析流程，适用于教学演示或求职作品集展示。

## Overview

This project analyzes online customer purchasing behavior using the UCI Online Retail II dataset. The goal is to identify top customers, evaluate product performance over time, and visualize purchasing patterns using Power BI. The pipeline includes data cleaning with Python and interactive dashboard creation.

## Data Visualization
** 📝 中文说明：** 本部分展示了使用 Power BI 和 Tableau 构建的客户购买行为分析图表，涵盖用户分布、退货频率与时间趋势等核心维度。

Power BI Dashboard

![Power BI dashboard image](ecommerce_customer_behavior.pbix.png)

Tableau Dashboard

![tableau dashboard image](ecommerce_behavior_dashboard.twbx.png)

## Data Architecture
** 📝 中文说明：** 项目使用 Python 进行预处理，构建清洗数据集，并通过 Power BI 可视化客户行为路径，适合非技术用户交互分析。

![data architecture image](ecommerce_behavior_pipeline_architecture.png)

We chose Power BI for interactive visualization and Python for efficient data wrangling. This architecture allows non-technical users to filter and explore insights while maintaining a reproducible backend pipeline.

## Prerequisites
** 📝 中文说明：** 本项目可在本地或 Colab 环境中运行，需提前安装 Python 与必要的库，并准备好数据文件和 Power BI 软件用于可视化操作。

Before running the project, ensure the following:

- 1.Python 3.x installed or use Google Colab
  * 安装 Python 3.x，或直接使用 Google Colab 免安装运行 
- 2.Install pandas, numpy, and openpyxl
  * 安装所需 Python 库：pandas、numpy、openpyxl  
- 3.Power BI Desktop installed (for .pbix file viewing)
  * 安装 Power BI Desktop（用于打开 .pbix 可视化文件） 
- 4.Place online_retail_II.xlsx into the data/ directory
  * 确保原始数据文件放在 `data/` 目录下（文件名为 `online_retail_II.xlsx`）

## How to Run This Project
** 📝 中文说明：** 可在本地或 Google Colab 运行 Python 预处理脚本，再用 Power BI 和 Tableau 打开仪表板进行交互展示。

Run the preprocessing script:

1. python and SQL scripts/preprocessing.py
   The script will output:
   - 执行数据清洗脚本，生成清洗后的数据文件：`data/ecommerce_cleaned.csv`

3. Cleaned CSV: data/ecommerce_cleaned.csv
   Open dashboard/ecommerce_behavior in Power BI Desktop and Tableau, Interact with filters and visuals on the dashboard
   - 使用 Power BI 和 Tableau 打开仪表板，体验交互式筛选、可视化与数据探索
     
🧩 Note on SQL Compatibility:
All SQL scripts in this project are designed using standard SQL syntax. While executed with SQLite for simplicity, the same structure is compatible with MySQL or PostgreSQL by changing the database connector and placeholder syntax (`?` → `%s`).
** 📝 中文说明：** 所有 SQL 脚本基于标准语法编写，当前以 SQLite 运行为主，如需移植到 MySQL/PostgreSQL，仅需修改数据库连接方式及参数占位符格式（如 `?` → `%s`）。

## Lessons Learned
** 📝 中文说明：** 数据维度需合理聚合，字段太多会降低图表可读性。预处理环节可以极大提升最终仪表板加载速度。

- Invoice and Description fields contain too many unique values; require summarization
 * 发票号与产品描述字段具有高基数，建议进行预聚合处理 
- Power BI visuals require field aggregation (e.g., sum, count) to be meaningful
 * 在 Power BI 中需使用聚合函数（如 SUM、COUNT）以生成可读图表 
- Visual filtering helps highlight high-value users and product seasonality
 * 使用筛选器可以识别高价值客户及产品的季节性趋势
- Pre-aggregating in Python reduces dashboard load time significantly
 * 在 Python 中提前聚合数据可显著提升仪表板加载效率与交互性能
