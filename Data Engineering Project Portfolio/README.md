## Data Engineering Project Portfolio 数据工程项目组合
This repository showcases six real-world data engineering projects. Each project demonstrates practical skills in data cleaning, SQL pipeline construction, data visualization, and scalable architecture design. Projects can be executed on Google Colab, Jupyter Notebook, Azure, and various SQL platforms (e.g., Azure SQL, SQL Server, PostgreSQL), making them ideal for job portfolios, instructional demos, and research applications.

** 中文说明 (系列简介) ** 本仓库展示了六个基于真实数据的实战数据工程项目，涵盖数据清洗、SQL 管道构建、数据可视化以及可扩展架构设计。项目可在 Google Colab、Jupyter Notebook、Azure 以及多种 SQL 平台（如 Azure SQL、SQL Server、PostgreSQL）上运行，适用于求职展示、教学演示与研究实践。

## Projects 项目

- The following are six real-world data engineering projects showcasing data cleaning, SQL analysis, and visualization. They are designed to support teaching, interviews, and portfolio presentation.
    * 以下为六个真实世界数据工程项目的主题与所用工具，涵盖数据清洗、SQL 分析与可视化展示，支持面试与作品集展示。

| 项目编号 | 项目名称 | 项目简介（中英文） | 使用工具 |
|----------|-----------|----------------------|------------|
| 01 | US Target E-commerce Behavior Pipeline<br>美国塔吉特电商行为数据流程分析 | Customer purchase patterns from UCI dataset<br>基于美国塔吉特数据集分析用户购买行为与电商销售模式 | Python, SQL, Tableau, Power BI |
| 02 | Wamlart Supply Chain Efficiency Dashboard<br>沃尔玛供应链效率指标仪表板 | Transport vs discount vs cost KPIs<br>分析运输方式、折扣与成本之间的效率匹配关系 | Python, SQL, Metabase |
| 03 | Data Science Salary Analysis<br>数据科学职业薪资分析 | Worldwide salary distribution for DS roles<br>分析全球不同数据职位的薪资分布与地区差异 | Python, SQL, Matplotlib |
| 04 | Amazon Sentiment NLP<br>亚马逊评论情感分析 | Sentiment classification on product reviews<br>通过情感分析方法对亚马逊评论进行分类与可视化展示 | Python, Seaborn, Wordcloud |
| 05 | NASA Spark IoT Sensor Pipeline<br>美国NASA物联网传感器故障检测流程 | Fault detection and classification based on industrial sensor logs<br>基于工业传感器数据的故障检测与分类分析流程 | Python, PySpark, Seaborn, Matplotlib |
| 06 | Cloud ETL Project Pipeline<br>云端数据处理与 ETL 管道构建项目 | Cloud-based ETL pipeline for structured real estate transactions<br>基于云平台的房地产结构化交易数据清洗与分析流程 | Python，PySpark，seaborn, Matplotlib |
    
## Technical Highlights 技术亮点

- All projects in this repository follow a modular pipeline structure, combining Python scripts with SQL queries and multiple visualization tools.
  * 本仓库所有实战项目均采用模块化数据流程结构，结合 Python 脚本、SQL 查询和多种可视化工具。
- The typical Python script structure is: clean_data.py → pipeline.py → run_pipeline.py.
  * Python 脚本结构统一为：clean_data.py → pipeline.py → run_pipeline.py。
- SQL logic is written in a SQLite-first format, compatible with MySQL and PostgreSQL.
  * SQL 查询采用 SQLite 优先 编写，兼容 MySQL 和 PostgreSQL。
- Python is used for all data processing and analysis tasks, with libraries including pandas, matplotlib, textblob, and more.
  * 所有数据处理与分析均使用 Python 工具链，常用库包括 pandas、matplotlib、textblob 等。
- Visualization tools include Tableau, Power BI, Metabase, Seaborn, Plotly, Apache Spark and WordCloud.
  * 可视化工具涵盖 Tableau、Power BI、Metabase、Seaborn、Plotly、Apache Spark、WordCloud 等。
- Each project includes an engineering-style architecture diagram to illustrate workflows and module relationships.
  * 每个项目都配备工程化架构图，用于展示流程与模块之间的关系。
- All scripts are executable both on Google Colab and in local Jupyter Notebook environments.
  * 所有脚本均可在 Google Colab 和本地 Jupyter Notebook 环境中运行。
- All datasets are sourced from real-world Kaggle datasets, enhancing the credibility and teaching value of each project.
  * 所有数据均来自 Kaggle 真实世界数据集，增强项目的可信度与教学展示价值。
- Projects are suitable for job applications, portfolio demonstration, and real-world data process presentation.
  * 实战项目适用于求职展示、作品集构建及真实业务流程展示。
- One project demonstrates cloud-based ETL pipeline construction using PySpark and scalable deployment.
  * 其中一个项目展示了基于 PySpark 的云端 ETL 管道构建与可扩展部署能力。
- All Python visualizations in Project 6 and 7 are created using both Seaborn and Matplotlib to ensure customizable, publication-quality plots.
  * 项目 6 和项目 7 中所有 Python 图表均结合 Seaborn 与 Matplotlib 实现，兼顾美观性与高度自定义能力。
- All projects emphasize reproducibility, modularity, and real-world applicability.
  * 所有项目均强调可复现性、模块化与真实场景适应能力。
