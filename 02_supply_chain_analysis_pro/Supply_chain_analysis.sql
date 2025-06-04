DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    order_id TEXT,
    carrier_code TEXT,
    shipping_cost REAL,
    shipping_distance INTEGER,
    shipping_time INTEGER
);
INSERT INTO orders (order_id, carrier_code, shipping_cost, shipping_distance, shipping_time) VALUES
('ORD001', 'Carrier A', 120.5, 450, 3),
('ORD002', 'Carrier B', 200.0, 800, 5),
('ORD003', 'Carrier C', 150.0, 650, 6),
('ORD004', 'Carrier A', 100.0, 400, 2),
('ORD005', 'Carrier B', 180.0, 750, 4),
('ORD006', 'Carrier C', 140.0, 600, 6);
SELECT
    order_id,
    CASE 
        WHEN carrier_code = 'Carrier A' THEN 'DHL'
        WHEN carrier_code = 'Carrier B' THEN 'FedEx'
        WHEN carrier_code = 'Carrier C' THEN 'UPS'
        ELSE carrier_code
    END AS shipping_carrier,
    shipping_cost,
    shipping_distance,
    shipping_time
FROM orders;
