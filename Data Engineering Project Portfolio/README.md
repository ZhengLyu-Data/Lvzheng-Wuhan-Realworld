## Data Engineering Project Portfolio 数据工程项目组合
This repository showcases five real-world data engineering projects. Each project demonstrates practical skills in data cleaning, SQL pipeline construction, visualization, and scalable architecture.

** 中文说明 (系列简介) ** 本仓库包含五个基于真实数据的实战数据工程项目，涵盖数据清洗、SQL 查询、可视化构建与管道设计。所有项目可在 Google Colab / Azure 等平台运行，适合用于求职展示、教学演示或研究应用。

## Projects 项目

- The following are five real-world data engineering projects showcasing data cleaning, SQL analysis, and visualization. They are designed to support teaching, interviews, and portfolio presentation.
    * 以下为五个真实世界数据工程项目的主题与所用工具，涵盖数据清洗、SQL 分析与可视化展示，支持教学、面试与作品集展示。

| 项目编号 | 项目名称 | 项目简介（中英文） | 使用工具 |
|----------|-----------|----------------------|------------|
| 01 | E-commerce Behavior Pipeline<br>电商行为数据流程分析 | Customer purchase patterns from UCI dataset<br>基于 UCI 数据集分析用户购买行为与电商销售模式 | Python, SQL, Tableau, Power BI |
| 02 | Supply Chain Efficiency Dashboard<br>供应链效率指标仪表板 | Transport vs discount vs cost KPIs<br>分析运输方式、折扣与成本之间的效率匹配关系 | Python, SQL, Metabase |
| 03 | Data Science Salary Analysis<br>数据科学薪资分析 | Worldwide salary distribution for DS roles<br>分析全球不同数据职位的薪资分布与地区差异 | Python, SQL, Matplotlib |
| 04 | Bank Marketing Dataset<br>银行营销行为分析 | Predictive Modeling for Bank Term Deposit Campaigns<br>预测客户是否会响应定期存款营销活动 | Python, SQL, Plotly |
| 05 | Amazon Sentiment NLP<br>亚马逊评论情感分析 | Sentiment classification on product reviews<br>通过情感分析方法对亚马逊评论进行分类与可视化展示 | Python, Seaborn, Wordcloud |

    
## Technical Highlights 技术亮点

- All projects in this repository follow a modular pipeline structure, combining Python scripts with SQL queries and multiple visualization tools.
  * 本仓库所有实战项目均采用模块化数据流程结构，结合 Python 脚本、SQL 查询和多种可视化工具。
- The typical Python script structure is: clean_data.py → pipeline.py → run_pipeline.py.
  * Python 脚本结构统一为：clean_data.py → pipeline.py → run_pipeline.py。
- SQL logic is written in a SQLite-first format, compatible with MySQL and PostgreSQL.
  * SQL 查询采用 SQLite 优先 编写，兼容 MySQL 和 PostgreSQL。
- Python is used for all data processing and analysis tasks, with libraries including pandas, matplotlib, textblob, and more.
  * 所有数据处理与分析均使用 Python 工具链，常用库包括 pandas、matplotlib、textblob 等。
- Visualization tools include Tableau, Power BI, Metabase, Seaborn, Plotly, and WordCloud.
  * 可视化工具涵盖 Tableau、Power BI、Metabase、Seaborn、Plotly、WordCloud 等。
- Each project includes an engineering-style architecture diagram to illustrate workflows and module relationships.
  * 每个项目都配备工程化架构图，用于展示流程与模块之间的关系。
- All scripts are executable both on Google Colab and in local Jupyter Notebook environments.
  * 所有脚本均可在 Google Colab 和本地 Jupyter Notebook 环境中运行。
- All datasets are sourced from real-world Kaggle datasets, enhancing the credibility and teaching value of each project.
  * 所有数据均来自 Kaggle 真实世界数据集，增强项目的可信度与教学展示价值。
- Projects are suitable for job applications, portfolio demonstration, and real-world data process presentation.
  * 实战项目适用于求职展示、作品集构建及真实业务流程展示。
