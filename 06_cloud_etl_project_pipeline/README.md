## Overview 项目总览

This project analyzes Netflix viewing activity logs to uncover patterns in user engagement, peak viewing times, and device usage trends. It follows a structured ETL pipeline using PySpark for large-scale data cleaning, transformation, and aggregation, and leverages Seaborn and Matplotlib for visual exploration of the results.

** 中文说明（项目简介）** 本项目基于 Netflix 云端观看日志数据，分析用户观看时长分布、活跃时段趋势以及不同设备类型的使用偏好。项目使用 PySpark 完成大规模数据清洗与特征提取，并结合 Seaborn 与 Matplotlib 进行可视化分析，形成结构化输出与洞察结果。

## Data Visualization 数据可视化

- This project uses Seaborn and Matplotlib to visualize Netflix viewing patterns, including: Top watched titles by total viewing time，Hourly viewing trends showing peak activity hours，Weekly patterns highlighting day-of-week preferences
  * 本项目利用 Seaborn 与 Matplotlib 绘制 Netflix 用户观看行为的可视化图表，包括：按总观看时长排序的热门影片，每小时观看趋势，揭示活跃高峰时段，按星期分布的观看偏好

Below are screenshots of the final visualizations:
以下为本项目生成的最终可视化图表示例截图：

![matplotlib dashboard image]()
![matplotlib dashboard image]()
![matplotlib dashboard image]()

## Data Architecture 数据流程图

This project applies modular PySpark scripts for data cleaning, enrichment, and aggregation, then produces visual analytics using Seaborn and Matplotlib—highlighting an engineering-oriented workflow with scalable big data processing.

本项目采用模块化 PySpark 脚本完成数据清洗、特征丰富与聚合分析，并使用 Seaborn 与 Matplotlib 生成可视化结果，体现了工程化数据处理与可扩展的大数据分析能力。


## Prerequisites 环境准备

- Python 3.10+ — Required for running all scripts
  * 运行全部脚本需 Python 3.10 及以上版本

- PySpark — For distributed data processing
  * 用于分布式数据处理的 PySpark

- Seaborn & Matplotlib — For visualization
  * 用于绘图的 Seaborn 与 Matplotlib

- Google Colab or local Jupyter environment
  * 推荐使用 Google Colab 或本地 Jupyter Notebook 执行

- This project can run entirely in Google Colab or a properly configured local environment with PySpark installed.
  * 本项目可在 Google Colab 全部运行，或在本地安装并配置 PySpark 后执行

## How to Run This Project 如何运行本项目

- Run the three Python scripts in sequence:
  * 依次运行三个 Python 脚本：

- Data Cleaning — clean_data.py Cleans raw Netflix viewing logs, standardizes column names, converts timestamps, and calculates total viewing minutes.
  * 清洗原始 Netflix 观看日志，标准化列名，转换时间戳，并计算总观看分钟数。

- Data Pipeline — pipeline.py Adds derived columns (date, hour, weekday), performs grouping & aggregation for top titles, hourly patterns, and weekday distributions.
  * 添加派生字段（日期、小时、星期），并进行分组与聚合分析。

- Run Pipeline — run_pipeline.py Generates the three final visualizations (Top Titles, Hourly Trends, Weekday Patterns) and saves them as PNG files.
  * 生成三张最终可视化图（热门影片、小时趋势、星期分布），并保存为 PNG 文件。

## Lessons Learned 学习亮点

- Evening hours are the consistent peak viewing period for Netflix users, regardless of the day of the week.
  * Netflix 用户无论工作日还是周末，晚间时段均为观看高峰。

- Binge-watching drives the majority of total watch time for certain titles.
  * 连续刷剧行为显著增加部分节目的总观看时长。

- Device usage trends suggest content consumption patterns differ between weekdays and weekends.
  * 设备使用趋势显示，工作日与周末的内容消费方式存在差异。

- Cross-device viewing patterns reveal that mobile devices dominate short sessions, while TVs and desktops are preferred for longer viewing durations.
  * 跨设备观看模式显示，移动设备更适合短时观看，而电视与桌面端更适合长时间观看。
