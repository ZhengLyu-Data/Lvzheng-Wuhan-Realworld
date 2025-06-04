## 💳 Bank Marketing Analysis Dashboard

This project analyzes bank marketing campaign data to understand subscription behavior across customer segments. It includes performance metrics by job, education, age group, and campaign effectiveness using multi-tool integration.

## 📁 Dataset

Original File: project4_bank_dataset.csv

Cleaned Combined File: cleaned_project4_combined_dataset.csv

Individual Analytic Tables:

table1_subscription_by_job.csv

table2_loan_impact_on_subscription.csv

table3_campaign_effectiveness.csv

table4_education_vs_subscription.csv

table5_age_group_distribution.csv

table6_monthly_subscription_trend.csv

## 🔧 Tools Used

Tool                 Purpose

Python              Data cleaning, transformation, CSV generation

Tableau             Dashboard visualization for key metrics

Power BI            Multi-page campaign performance and segmentation view

SQL                 Aggregation queries and segment analysis

GitHub              Project versioning and portfolio hosting

## 📌 Deliverables

✅ Cleaned and merged CSV output (6 tables + 1 combined)

✅ Tableau dashboard screenshot: bank_marketing_dashboard_tableau.png

✅ Power BI dashboard screenshot: bank_marketing_dashboard_powerbi.png

✅ SQL script: project4_sql_queries.sql

## 📈 Tableau Dashboard

Title: Bank Marketing Analytics Dashboard

Subscription Rate by Job & Education

Monthly Trend of Campaign Results

Age & Loan Impact Visual Summary

## 📊 Power BI Dashboard

Three analytical pages:

Campaign Performance Overview

Demographic Impact (Age, Education, Loan)

Time-based Subscription Trend

## 🧮 SQL Sample

-- Subscription by Job
SELECT job, 
       ROUND(SUM(CASE WHEN y = 'yes' THEN 1 ELSE 0 END)*1.0 / COUNT(*), 2) AS subscribed_ratio
FROM bank_data
GROUP BY job;

-- Loan Impact on Subscription
SELECT loan, y, COUNT(*) AS count
FROM bank_data
GROUP BY loan, y;

-- Monthly Trend (ordered by month)
SELECT month, y, COUNT(*) AS count
FROM bank_data
GROUP BY month, y
ORDER BY 
  CASE month
    WHEN 'jan' THEN 1
    WHEN 'feb' THEN 2
    WHEN 'mar' THEN 3
    WHEN 'apr' THEN 4
    WHEN 'may' THEN 5
    WHEN 'jun' THEN 6
    WHEN 'jul' THEN 7
    WHEN 'aug' THEN 8
    WHEN 'sep' THEN 9
    WHEN 'oct' THEN 10
    WHEN 'nov' THEN 11
    WHEN 'dec' THEN 12
    ELSE 13
  END;

## 📄 Resume Project Description (English)

Bank Marketing Campaign ProjectBuilt an end-to-end data analytics solution integrating Python, SQL, Tableau, and Power BI to evaluate customer behavior in subscription-based banking campaigns. Delivered insights across job types, education levels, loan status, and age groups to support strategic marketing efforts.

## 📎 Author

Zheng Lyu | Data Analyst CandidateGitHub: github.com/ZhengLyu-Data

