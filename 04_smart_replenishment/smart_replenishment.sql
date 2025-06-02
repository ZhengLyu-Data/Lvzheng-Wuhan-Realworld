-- 📄 SQL File: replenishment_analysis.sql

-- 1. Total units sold per product
SELECT ProductName, SUM(UnitsSold) AS TotalUnitsSold
FROM replenishment_data
GROUP BY ProductName;

-- 2. Products that need to be reordered (CurrentStock < ReorderPoint)
SELECT ProductID, ProductName, CurrentStock, ReorderPoint
FROM replenishment_data
WHERE CurrentStock < ReorderPoint;

-- 3. Average lead time by store
SELECT Store, AVG(LeadTimeDays) AS AvgLeadTime
FROM replenishment_data
GROUP BY Store;

-- 4. Daily sales summary per store
SELECT Store, Date, SUM(UnitsSold) AS UnitsSold
FROM replenishment_data
GROUP BY Store, Date
ORDER BY Date ASC;

-- 5. Products with highest stock gap (derived)
SELECT ProductID, ProductName, (ReorderPoint - CurrentStock) AS StockGap
FROM replenishment_data
WHERE CurrentStock < ReorderPoint
ORDER BY StockGap DESC;