## Overview / 项目总览

This project explores salary trends in data science roles globally. It highlights differences based on job level, company size, and work flexibility using structured pipeline processing and visual outputs.

**中文说明 (项目简介)**  
本项目分析了全球范围内数据科学岗位的薪资趋势。通过 Python 数据管道处理，结合 Matplotlib 图表可视化，揭示了不同职位级别、公司规模与远程工作比例下的薪资差异。项目展示了清洗 → 分析 → 可视化的完整流程，适合教学演示与求职展示。

## Data Visualization / 数据可视化

- This project uses Matplotlib to visualize the average salary by experience level, the distribution of remote work ratios, and salary variations across different company sizes.  
  * 本项目使用 Matplotlib 绘制图表，展示了平均薪资与职位经验等级、远程办公比例分布、不同公司规模下的薪资差异。

- Below are screenshots of the final visualizations:  
  * 以下为本项目生成的最终可视化图表示例截图：

![plotly dashboard image](Campaign_Histogram.png)  
![plotly dashboard image](Campaign_vs_Euribor_Rate.png)  
![plotly dashboard image](Correlation_Heatmap.png)

## Data Architecture / 数据流程图

- This project uses modular Python scripts for data cleaning and pipeline construction, and generates static visualizations using Matplotlib—demonstrating both an engineering-oriented structure and compatibility with teaching presentations.  
  * 本项目采用模块化 Python 脚本进行数据清洗与管道构建，并通过 Matplotlib 输出静态可视化图像，体现工程结构与教学演示兼容性。

![Data Architecture]()

##  Prerequisites / 环境准备

- Use Python version 3.10 or above.  
  * 推荐使用 Python 3.10 以上版本，确保兼容性和新特性支持。

- Google Colab or local Jupyter environment  
  * 推荐使用 Google Colab 运行，亦支持本地 Jupyter 环境。

- matplotlib  
  * 用于图表绘制的可视化库

- SQLite – for SQL query processing  
  * 用于执行 SQL 查询分析的轻量数据库

- All SQL scripts in this project are written in standard SQL syntax, defaulted to SQLite. To adapt to MySQL or PostgreSQL, adjust connectors and parameter placeholders.  
  * 所有 SQL 脚本基于标准语法，默认使用 SQLite。如需迁移至其他数据库，调整连接方式及参数符号即可。

## How to Run This Project / 如何运行本项目

- 1. Step 1: Load and Clean the raw dataset (`clean_data.py`)  
  * 载入并清洗原始数据，处理缺失值与字段规范
  
- 2. Step 2: Build the analysis pipeline (`pipeline.py`)  
  * 构建分析流程，完成特征处理与分组统计

- 3. Step 3: Execute and visualize (`run_pipeline.py`)  
  * 运行主脚本，生成所有图表与结构化输出

## Lessons Learned / 学习亮点

- Position level significantly influences salary outcomes  
  * 职位等级对薪资水平具有显著影响

- Remote roles show diverse regional patterns  
  * 远程岗位在不同地区的比例分布差异显著

- Company size contributes to salary dispersion  
  * 公司规模影响薪资分布的离散程度

