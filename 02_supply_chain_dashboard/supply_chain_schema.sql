
-- supply_chain_schema.sql

CREATE TABLE supply_orders (
    OrderID INT,
    OrderDate DATE,
    Supplier VARCHAR(50),
    Product VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(10, 2)
);

-- 示例插入数据
INSERT INTO supply_orders (OrderID, OrderDate, Supplier, Product, Quantity, UnitPrice) VALUES
(1, '2023-01-01', 'Supplier A', 'Product A', 100, 12.50),
(2, '2023-01-05', 'Supplier B', 'Product B', 50, 18.75),
(3, '2023-02-10', 'Supplier A', 'Product A', 200, 12.50),
(4, '2023-02-15', 'Supplier C', 'Product C', 75, 9.99),
(5, '2023-03-01', 'Supplier B', 'Product B', 120, 18.00);
