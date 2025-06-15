DROP TABLE IF EXISTS retail_cleaned;

CREATE TABLE retail_cleaned (
    Invoice VARCHAR(20),
    StockCode VARCHAR(20),
    Description VARCHAR(255),
    Quantity INT,
    InvoiceDate DATETIME,
    Price DECIMAL(10,2),
    CustomerID VARCHAR(20),
    Country VARCHAR(50)
);

INSERT INTO retail_cleaned (Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country)
VALUES
('536365', '85123A', 'WHITE HANGING HEART T-LIGHT HOLDER', 6, '2010-12-01 08:26:00', 2.55, '17850', 'United Kingdom'),
('536365', '71053', 'WHITE METAL LANTERN', 6, '2010-12-01 08:26:00', 3.39, '17850', 'United Kingdom'),
('536366', '84406B', 'CREAM CUPID HEARTS COAT HANGER', 8, '2010-12-01 08:28:00', 2.75, '17850', 'United Kingdom'),
('536367', '84406G', 'KNITTED UNION FLAG HOT WATER BOTTLE', 6, '2010-12-01 08:34:00', 3.39, '13047', 'United Kingdom'),
('536368', '85123A', 'WHITE HANGING HEART T-LIGHT HOLDER', 6, '2010-12-01 08:35:00', 2.55, '12583', 'France');

SELECT 
  DATE_FORMAT(InvoiceDate, '%Y-%m') AS Month,
  ROUND(SUM(Quantity * Price), 2) AS TotalRevenue
FROM retail_cleaned
GROUP BY Month
ORDER BY Month;

SELECT 
  Description,
  SUM(Quantity) AS TotalSold
FROM retail_cleaned
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 5;
