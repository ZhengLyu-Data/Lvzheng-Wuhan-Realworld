## Data Engineering Project Portfolio 数据工程项目组合
This repository showcases five real-world data engineering projects. Each project demonstrates practical skills in data cleaning, SQL pipeline construction, visualization, and scalable architecture.

** 中文说明 (系列简介) ** 本仓库包含五个基于真实数据的实战数据工程项目，涵盖数据清洗、SQL 查询、可视化构建与管道设计。所有项目可在 Google Colab / Azure 等平台运行，适合用于求职展示、教学演示或研究应用。

## Projects 项目

- The following are five real-world data engineering projects showcasing data cleaning, SQL analysis, and visualization. They are designed to support teaching, interviews, and portfolio presentation.
    * 以下为五个真实世界数据工程项目的主题与所用工具，涵盖数据清洗、SQL 分析与可视化展示，支持教学、面试与作品集展示。

| 项目编号 | 项目名称 | 项目简介（中英文） | 使用工具 |
|----------|-----------|----------------------|------------|
| 01 | E-commerce Behavior Pipeline<br>电商行为数据流程分析 | Customer purchase patterns from UCI dataset<br>基于 UCI 数据集分析用户购买行为与电商销售模式 | Python, SQL (SQLite), Tableau, Power BI |
| 02 | Supply Chain Efficiency Dashboard<br>供应链效率指标仪表板 | Transport vs discount vs cost KPIs<br>分析运输方式、折扣与成本之间的效率匹配关系 | Python, SQL (SQLite), Metabase |
| 03 | Data Science Salary Analysis<br>数据科学薪资分析 | Worldwide salary distribution for DS roles<br>分析全球不同数据职位的薪资分布与地区差异 | Python, SQL (SQLite), Matplotlib |
| 04 | Bank Marketing Dataset<br>银行营销行为分析 | Marketing call effectiveness analysis<br>探索电话营销活动中客户响应率与关键特征的关联 | Python, SQL (SQLite), Plotly |
| 05 | Amazon Sentiment NLP<br>亚马逊评论情感分析 | Sentiment classification on product reviews<br>通过情感分析方法对亚马逊评论进行分类与可视化展示 | Python, Seaborn, Wordcloud |

    
## Technical Highlights 技术亮点

- All projects in this repository follow a modular structure, combining Python scripts with standard SQL queries and various visualization tools (Tableau, Power BI, Metabase, matplotlib) to demonstrate complete data engineering and analysis workflows. They are suitable for teaching, portfolio presentation, and job applications.
    * 本仓库的项目均采用模块化结构，结合 Python 脚本与标准 SQL 查询，配合多种可视化工具（Tableau、Power BI、Metabase、matplotlib），展示完整数据工程与分析流程，适用于教学、作品集与岗位申请。
- Modular pipeline structure: `clean_data.py → pipeline.py → run_pipeline.py`
    * 模块化流水线结构：`clean_data.py → pipeline.py → run_pipeline.py`
- Unified SQL logic (SQLite-first, MySQL/PostgreSQL-compatible)
    * 统一 SQL 结构（以 SQLite 编写，兼容 MySQL/PostgreSQL）
- Python-driven analysis pipeline (pandas, matplotlib, textblob, etc.)
    * 全项目使用 Python 进行数据处理与分析（pandas、matplotlib、textblob 等）
- Visualization tools: Tableau, Power BI, Metabase, Seaborn, plotly, Wordcloud
    * 可视化工具多样（Tableau / Power BI / Metabase / Seaborn / plotly / Wordcloud 等）
- Engineering-style architecture diagrams
    * 工程化架构图展示项目流程与模块关系 
- Fully executable on cloud platforms (Google Colab / Azure)
    * 所有项目支持在 Google Colab / Azure 上运行与展示 
- This project can be executed both on Google Colab and local Jupyter Notebook.
    * 所有脚本支持在 Google Colab 中直接运行，同时也兼容本地 Jupyter Notebook 环境。只需确保 Python 3.x 与相关库已正确安装，即可在本地复现全部流程与输出结果。
