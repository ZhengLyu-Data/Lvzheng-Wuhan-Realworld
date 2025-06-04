DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS supply_chain;

CREATE TABLE orders (
    order_id TEXT,
  	carrier_code TEXT,
    shipping_cost REAL,
    shipping_distance INTEGER,
    shipping_time INTEGER
);

CREATE TABLE supply_chain (
    product_id TEXT,
    product_name TEXT,
    product_type TEXT,
    order_date TEXT,
    units_sold INTEGER,
    shipping_carrier TEXT,
    shipping_cost REAL,
    shipping_time REAL
);

INSERT INTO orders (order_id, carrier_code, shipping_cost, shipping_distance, shipping_time) VALUES
('ORD001', 'Carrier A', 120.5, 450, 3),
('ORD002', 'Carrier B', 200.0, 800, 5),
('ORD003', 'Carrier C', 150.0, 650, 6),
('ORD004', 'Carrier A', 100.0, 400, 2),
('ORD005', 'Carrier B', 180.0, 750, 4),
('ORD006', 'Carrier C', 140.0, 600, 6);


INSERT INTO supply_chain (product_id, product_name, product_type, order_date, units_sold, shipping_carrier, shipping_cost, shipping_time) VALUES
('P001', 'Widget A', 'Electronics', '2024-01-01', 100, 'UPS', 250, 3.5),
('P002', 'Widget B', 'Furniture', '2024-01-02', 60, 'FedEx', 180, 4),
('P003', 'Widget C', 'Electronics', '2024-01-03', 75, 'DHL', 200, 2.5),
('P004', 'USB-C Hub', 'Accessories', '2023-01-20', 90, 'FedEx', 2.2, 3),
('P005', 'Monitor', 'Electronics', '2023-01-25', 80, 'UPS', 4.5, 4),
('P006', 'Office Chair', 'Furniture', '2023-02-06', 75, 'DHL', 6.0, 5);

SELECT 
    sc.product_id,
    sc.product_name,
    sc.product_type,
    sc.units_sold,
    sc.shipping_carrier,
    sc.shipping_cost,
    sc.shipping_time,
    o.shipping_distance
FROM supply_chain sc
JOIN orders o
  ON sc.shipping_carrier = 
     CASE 
         WHEN o.carrier_code = 'Carrier A' THEN 'DHL'
         WHEN o.carrier_code = 'Carrier B' THEN 'FedEx'
         WHEN o.carrier_code = 'Carrier C' THEN 'UPS'
     END;
