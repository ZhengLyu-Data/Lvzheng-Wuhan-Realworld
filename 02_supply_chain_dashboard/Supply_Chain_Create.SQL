-- Create table
CREATE TABLE supply_chain_data (
    Order_ID VARCHAR(20),
    Product VARCHAR(100),
    Origin VARCHAR(100),
    Destination VARCHAR(100),
    Distance_KM INT,
    Transport_Method VARCHAR(50),
    Delivery_Time_Days INT,
    Transport_Cost DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO supply_chain_data VALUES
('SC001', 'Refrigerator', 'Shanghai', 'Beijing', 1200, 'Rail', 2, 350.00),
('SC002', 'Washing Machine', 'Guangzhou', 'Shanghai', 1300, 'Truck', 3, 420.00),
('SC003', 'Air Conditioner', 'Chengdu', 'Shenzhen', 1600, 'Air', 1, 880.00),
('SC004', 'Television', 'Nanjing', 'Hangzhou', 800, 'Truck', 2, 200.00),
('SC005', 'Microwave', 'Xi\'an', 'Wuhan', 900, 'Rail', 2, 310.00);

-- Check the data
SELECT * FROM supply_chain_data;
