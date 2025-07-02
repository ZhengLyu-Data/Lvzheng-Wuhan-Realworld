## 📌 中文说明（项目简介）
本项目分析了 10,999 条运输记录，旨在评估供应链的运作效率。通过标准化 SQL 查询和 Metabase 可视化图表，识别交付延迟、运输模式与成本效益的关系，辅助运营优化。适合展示数据查询、分析与可视化结合的完整流程。

## Overview
This project analyzes supply chain efficiency using a cleaned dataset of 10,999 shipment records. It highlights operational bottlenecks, delivery timeliness, and product shipment cost-performance through structured SQL logic and dashboard visualization.

## Data Visualization
** 📝 中文说明：** 本仪表板包括运输方式分布、不同产品重要性下的折扣情况，以及客户评分与运输成本的关系，用于综合评估供应链效率。

The dashboard includes the following charts:

![metabase dashboard image](chart1_mode_of_shipment.png)
![metabase dashboard image](chart2_discount_by_importance.png)
![metabase dashboard image](chart3_rating_vs_cost.png)

## Data Architecture
** 📝 中文说明：** 项目使用 Python 和标准 SQL 构建数据查询逻辑，利用 Metabase 构建前端图表，实现数据驱动的交互式分析系统。

![Data Architecture](supply_chain_data_pipeline_architecture.png)

## Prerequisites
** 📝 中文说明：** 推荐使用 Python 3.10 以上版本，使用 Pandas 进行基础处理，Metabase 进行可视化，也可选用 SQLite 做本地数据管理。

- Python 3.10+
- Pandas / metabase
- SQLite (optional for local storage)
  
## How to Run This Project
** 📝 中文说明：** 本项目不需额外清洗步骤。直接载入已清洗数据，使用 SQL 脚本或 Metabase 构建图表，即可获得可视化结果。

- Step 1: Load data (already cleaned)
- Step 2: Use visualization script or Metabase dashboard builder
- Step 3: Review insights from chart outputs

🧩 Note on SQL Compatibility:
All SQL scripts in this project are designed using standard SQL syntax. While executed with SQLite for simplicity, the same structure is compatible with MySQL or PostgreSQL by changing the database connector and placeholder syntax (`?` → `%s`).

## Lessons Learned
**📝 中文说明：** 本项目发现客户评分与运输成本不总是成正比，不同运输方式下折扣差异显著，运输模式优化对提高交付效率具有重要影响。

- Product cost and customer rating are not always correlated
- Discounts vary more significantly by shipment method than product tier
- Shipment mode optimization directly impacts delivery timeliness
