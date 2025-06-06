-- Step 1: Create raw table
DROP TABLE IF EXISTS olist_raw;

CREATE TABLE olist_raw (
    order_id TEXT,
    customer_id TEXT,
    order_status TEXT,
    order_purchase_timestamp TEXT,
    order_delivered_customer_date TEXT,
    customer_city TEXT,
    customer_state TEXT,
    payment_type TEXT,
    payment_value REAL,
    review_score INTEGER,
    product_id TEXT,
    product_category_name_english TEXT,
    price REAL,
    freight_value REAL,
    seller_id TEXT,
    seller_city TEXT,
    seller_state TEXT
);

-- Step 2: Insert sample data (cleaned ASCII only)
INSERT INTO olist_raw VALUES
('O1001', 'C1001', 'delivered', '2018-01-01', '2018-01-04', 'Sao Paulo', 'SP', 'credit_card', 120.5, 5, 'P1001', 'electronics', 100.0, 20.5, 'S1001', 'Sao Paulo', 'SP'),
('O1002', 'C1002', 'shipped', '2018-01-05', NULL, 'Rio de Janeiro', 'RJ', 'voucher', 80.0, 4, 'P1002', 'books', 70.0, 10.0, 'S1002', 'Campinas', 'SP'),
('O1003', 'C1003', 'delivered', '2018-02-01', '2018-02-05', 'Belo Horizonte', 'MG', 'boleto', 200.0, 3, 'P1003', 'clothing', 180.0, 20.0, 'S1003', 'Recife', 'PE');

-- Step 3: Cleaned output
SELECT
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_delivered_customer_date,
    customer_city,
    customer_state,
    payment_type,
    payment_value,
    review_score,
    product_id,
    product_category_name_english,
    price,
    freight_value,
    seller_id,
    seller_city,
    seller_state,
    substr(order_purchase_timestamp, 1, 7) AS purchase_month,
    julianday(order_delivered_customer_date) - julianday(order_purchase_timestamp) AS delivery_days
FROM olist_raw
WHERE
    order_id IS NOT NULL AND
    customer_id IS NOT NULL AND
    order_status IS NOT NULL AND
    order_purchase_timestamp IS NOT NULL AND
    order_delivered_customer_date IS NOT NULL AND
    payment_value > 0 AND
    price > 0 AND
    freight_value >= 0;
