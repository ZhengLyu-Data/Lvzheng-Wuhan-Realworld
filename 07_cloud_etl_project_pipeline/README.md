## Overview 项目简介

This project demonstrates a complete cloud-based ETL pipeline using real-world housing data. It includes data cleaning, transformation, analysis, and visualization using PySpark and Python tools. The workflow simulates a typical distributed ETL scenario commonly used in real estate intelligence applications.

本项目基于真实房地产数据，构建了完整的云端 ETL 数据处理流程。涵盖数据清洗、转换、分析及可视化环节，采用 PySpark 与 Python 工具链实现。  流程模拟了分布式环境下的典型 ETL 管道，适用于房地产行业的数据智能应用场景。

## Data Visualization 数据可视化

- Average Price by Region - Average property price across different regions.
  * 展示不同区域的平均房产价格分布

 ![Fault Type Distribution]() 

- Property Count by Year Built - Number of properties grouped by year built.
  * 展示不同建成年份的房产数量统计

![Fault Type Distribution]() 

> All charts are generated using **Seaborn + Matplotlib** to ensure high-quality, customizable visualization output.  
> 所有图表均采用 Seaborn + Matplotlib 绘制，具备高质量与高度自定义能力。

## Data Architecture 数据架构

![pipeline_architecture]()

## Prerequisites 运行依赖

- Python 3.9+
- seaborn
- matplotlib
- PySpark
- Jupyter Notebook or Google Colab

## How to Run This Project 运行方式

1. Clone this repo or download the source files  
   克隆本仓库或下载源码文件

2. Run the scripts in order 按顺序运行脚本：

python clean_data.py
python pipeline.py
python run_pipeline.py

3. View the charts in the project folder  
   查看生成图表和输出结果

## 🎓 Lessons Learned 学习亮点

- Built a real-world ETL pipeline with **cloud-ready logic and distributed processing design**
- Learned to combine **PySpark** and **pandas** for flexible preprocessing and transformation
- Developed multi-step data workflows based on **modular Python script structure**
- Practiced statistical visualization using **Seaborn + Matplotlib**
