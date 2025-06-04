-- Drop the table if it exists
DROP TABLE IF EXISTS cleaned_train;

-- Create table
CREATE TABLE cleaned_train (
    OrderID TEXT,
    OrderDate TEXT,
    Product_Category TEXT,
    Region TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    TotalSales REAL
);

-- Insert sample rows
INSERT INTO cleaned_train VALUES 
('ORD001', '2023-01-01', 'Electronics', 'North', 5, 100.0, 500.0),
('ORD002', '2023-01-02', 'Apparel', 'South', 3, 50.0, 150.0),
('ORD003', '2023-01-03', 'Grocery', 'East', 10, 20.0, 200.0),
('ORD004', '2023-01-04', 'Electronics', 'West', 2, 120.0, 240.0),
('ORD005', '2023-01-05', 'Apparel', 'North', 4, 60.0, 240.0);

-- Query 1: Total sales by region
SELECT Region, SUM(TotalSales) AS TotalRegionSales
FROM cleaned_train
GROUP BY Region;

-- Query 2: Average unit price by product category
SELECT Product_Category, AVG(UnitPrice) AS AvgPrice
FROM cleaned_train
GROUP BY Product_Category;

-- Query 3: Total quantity sold per product category
SELECT Product_Category, SUM(Quantity) AS TotalQty
FROM cleaned_train
GROUP BY Product_Category;

-- Query 4: Monthly sales trend
SELECT 
  SUBSTR(OrderDate, 1, 7) AS Month,
  SUM(TotalSales) AS MonthlySales
FROM cleaned_train
GROUP BY Month
ORDER BY Month;

-- Query 5: Top 2 best-selling product categories
SELECT Product_Category, SUM(TotalSales) AS TotalSales
FROM cleaned_train
GROUP BY Product_Category
ORDER BY TotalSales DESC
LIMIT 2;

-- Query 6: Average order value
SELECT 
  COUNT(OrderID) AS OrderCount,
  ROUND(SUM(TotalSales)/COUNT(OrderID), 2) AS AvgOrderValue
FROM cleaned_train;
