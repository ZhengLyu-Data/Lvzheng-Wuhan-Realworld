-- Total orders, total revenue, and total items sold
SELECT
  COUNT(DISTINCT c1) AS total_orders,
  SUM(c4) AS total_revenue,
  SUM(c5) AS total_items_sold
FROM order_items_cleaned;

-- Top 10 product categories by revenue
SELECT
  c2 AS product_category,
  SUM(c4) AS category_revenue
FROM order_items_cleaned
GROUP BY c2
ORDER BY category_revenue DESC
LIMIT 10;

-- Monthly revenue and order trends
SELECT
  strftime('%Y-%m', c3) AS month,
  COUNT(DISTINCT c1) AS monthly_orders,
  SUM(c4) AS monthly_revenue
FROM order_items_cleaned
GROUP BY month
ORDER BY month;

-- Top 10 customers by total spending
SELECT
  c6 AS customer_id,
  COUNT(DISTINCT c1) AS orders_count,
  SUM(c4) AS total_spent
FROM order_items_cleaned
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
