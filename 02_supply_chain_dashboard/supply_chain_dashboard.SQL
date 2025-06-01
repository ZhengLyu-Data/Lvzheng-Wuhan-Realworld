-- Create table
CREATE TABLE supply_chain_data (
    OrderID INT,
    Product VARCHAR(100),
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    Source VARCHAR(100),
    Destination VARCHAR(100),
    DistanceKM INT,
    TransportDays INT,
    TransportCost DECIMAL(10,2),
    OrderDate DATE
);

-- Insert mock data
INSERT INTO supply_chain_data VALUES
(1, 'Widget A', 100, 10.50, 'Factory A', 'Warehouse X', 800, 4, 350.00, '2025-01-01'),
(2, 'Widget B', 200, 15.00, 'Factory B', 'Warehouse Y', 1200, 6, 600.00, '2025-01-03'),
(3, 'Widget C', 150, 12.75, 'Factory C', 'Warehouse Z', 950, 5, 450.00, '2025-01-05'),
(4, 'Widget A', 180, 10.50, 'Factory A', 'Warehouse X', 820, 4, 360.00, '2025-01-07'),
(5, 'Widget B', 220, 15.00, 'Factory B', 'Warehouse Y', 1180, 6, 610.00, '2025-01-09');

-- Query 1: Average Transport Days by Product
SELECT 
    Product,
    ROUND(AVG(TransportDays), 2) AS Avg_Transport_Days
FROM supply_chain_data
GROUP BY Product;

-- Query 2: Average Transport Cost by Source
SELECT 
    Source,
    ROUND(AVG(TransportCost), 2) AS Avg_Transport_Cost
FROM supply_chain_data
GROUP BY Source;

-- Query 3: Total Distance by Destination
SELECT 
    Destination,
    SUM(DistanceKM) AS Total_Distance_KM
FROM supply_chain_data
GROUP BY Destination
ORDER BY Total_Distance_KM DESC;
