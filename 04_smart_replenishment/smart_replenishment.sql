CREATE TABLE replenishment_data (
  ProductID VARCHAR(10),
  ProductName VARCHAR(50),
  Store VARCHAR(20),
  Date DATE,
  UnitsSold INT,
  CurrentStock INT,
  ReorderPoint INT,
  LeadTimeDays INT
);

INSERT INTO replenishment_data VALUES
('P001', 'Widget A', 'Store1', '2024-01-01', 10, 50, 20, 3),
('P002', 'Widget B', 'Store1', '2024-01-01', 5, 40, 15, 2),
('P003', 'Widget C', 'Store2', '2024-01-01', 8, 30, 10, 4),
('P001', 'Widget A', 'Store2', '2024-01-02', 7, 45, 20, 3),
('P004', 'Widget D', 'Store1', '2024-01-02', 3, 20, 10, 5),
('P005', 'Widget E', 'Store1', '2024-01-03', 9, 25, 12, 4);

-- 1. Total units sold per product
SELECT ProductName, SUM(UnitsSold) AS TotalUnitsSold
FROM replenishment_data
GROUP BY ProductName;

-- 2. Products that need to be reordered
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

-- 5. Products with highest stock gap
SELECT ProductID, ProductName, (ReorderPoint - CurrentStock) AS StockGap
FROM replenishment_data
WHERE CurrentStock < ReorderPoint
ORDER BY StockGap DESC;
