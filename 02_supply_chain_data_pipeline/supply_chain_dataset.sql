-- 🧱 Project: Supply Chain Efficiency Dashboard 

-- ✅ Step 1: Create table structure
DROP TABLE IF EXISTS supply_chain;
CREATE TABLE supply_chain (
    id INTEGER PRIMARY KEY,
    warehouse_block TEXT,
    mode_of_shipment TEXT,
    customer_care_calls INTEGER,
    customer_rating INTEGER,
    product_cost INTEGER,
    prior_purchases INTEGER,
    product_importance TEXT,
    gender TEXT,
    discount INTEGER,
    weight_grams INTEGER,
    on_time_delivery INTEGER
);

-- ✅ Step 2: Insert sample records
INSERT INTO supply_chain VALUES
(1, 'D', 'Flight', 4, 2, 177, 3, 'low', 'F', 44, 1233, 1),
(2, 'F', 'Flight', 4, 5, 216, 2, 'low', 'M', 59, 3088, 1),
(3, 'A', 'Flight', 2, 2, 183, 4, 'low', 'M', 48, 3374, 1),
(4, 'B', 'Flight', 3, 3, 176, 4, 'medium', 'M', 10, 1177, 0),
(5, 'C', 'Flight', 2, 2, 184, 3, 'medium', 'F', 46, 2484, 0),
(6, 'F', 'Ship',   4, 4, 200, 5, 'high', 'F', 5, 3210, 1),
(7, 'A', 'Ship',   3, 3, 220, 3, 'medium', 'M', 20, 2800, 0),
(8, 'B', 'Road',   5, 5, 140, 2, 'low', 'F', 35, 1500, 1),
(9, 'D', 'Road',   4, 1, 130, 1, 'low', 'M', 60, 1400, 0),
(10,'C', 'Ship',   3, 2, 190, 4, 'medium', 'F', 25, 2100, 1);

-- ✅ Step 3: Analysis 1 - Shipment delay rate by shipment mode
SELECT 
    mode_of_shipment,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN on_time_delivery = 0 THEN 1 ELSE 0 END) AS delayed_orders,
    ROUND(
        CAST(SUM(CASE WHEN on_time_delivery = 0 THEN 1 ELSE 0 END) AS FLOAT) 
        / COUNT(*), 2
    ) AS delay_rate
FROM supply_chain
GROUP BY mode_of_shipment
ORDER BY delay_rate DESC;

-- ✅ Step 4: Analysis 2 - Shipment volume by warehouse and mode
SELECT 
    warehouse_block,
    mode_of_shipment,
    COUNT(*) AS shipment_count
FROM supply_chain
GROUP BY warehouse_block, mode_of_shipment
ORDER BY shipment_count DESC;

-- ✅ Step 5: Analysis 3 - Delay rate by discount range
SELECT 
    CASE 
        WHEN discount < 10 THEN 'Low (<10)'
        WHEN discount BETWEEN 10 AND 30 THEN 'Medium (10-30)'
        WHEN discount > 30 THEN 'High (>30)'
    END AS discount_range,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN on_time_delivery = 0 THEN 1 ELSE 0 END) AS delayed_orders,
    ROUND(
        CAST(SUM(CASE WHEN on_time_delivery = 0 THEN 1 ELSE 0 END) AS FLOAT) 
        / COUNT(*), 2
    ) AS delay_rate
FROM supply_chain
GROUP BY discount_range
ORDER BY delay_rate DESC;

-- ✅ Step 6: Analysis 4 - Average care calls by customer rating
SELECT 
    customer_rating,
    AVG(customer_care_calls) AS avg_care_calls,
    COUNT(*) AS customer_count
FROM supply_chain
GROUP BY customer_rating
ORDER BY customer_rating ASC;
