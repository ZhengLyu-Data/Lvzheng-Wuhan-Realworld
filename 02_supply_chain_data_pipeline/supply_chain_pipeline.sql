-- 🧱 Project: Supply Chain Efficiency Dashboard 

/* ---------- Optional: drop & create views for reuse ---------- */
DROP VIEW IF EXISTS v_weekly_total_sales;
DROP VIEW IF EXISTS v_store_yoy_avg;
DROP VIEW IF EXISTS v_store_dept_lift;

CREATE VIEW v_weekly_total_sales AS
SELECT
  week_start,
  SUM(weekly_sales) AS total_sales
FROM walmart_weekly_clean
GROUP BY week_start;

CREATE VIEW v_store_yoy_avg AS
SELECT
  store,
  AVG(yoy_growth) AS avg_yoy_growth,
  COUNT(*)        AS n_weeks
FROM walmart_weekly_clean
GROUP BY store;

CREATE VIEW v_store_dept_lift AS
SELECT
  store,
  dept,
  AVG( (weekly_sales - sales_ma_4) / NULLIF(sales_ma_4, 0) ) AS avg_lift,
  COUNT(*) AS n_weeks
FROM walmart_weekly_clean
GROUP BY store, dept;

/* ---------- Query 1: Weekly total sales trend (for a line chart) ---------- */
SELECT
  week_start,
  total_sales
FROM v_weekly_total_sales
ORDER BY week_start;

/* ---------- Query 2: Store YoY growth — Top 10 (filter small samples) ---------- */
SELECT
  store,
  avg_yoy_growth
FROM v_store_yoy_avg
WHERE n_weeks > 10
ORDER BY avg_yoy_growth DESC
LIMIT 10;

/* ---------- Query 3: Dept lift vs 4-week MA — Top 20 (store-dept combos) ---------- */
SELECT
  store,
  dept,
  avg_lift
FROM v_store_dept_lift
WHERE n_weeks > 10
ORDER BY avg_lift DESC
LIMIT 20;
