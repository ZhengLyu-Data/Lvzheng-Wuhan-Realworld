
-- supplier_analysis.sql

-- 计算每个供应商的总订单数量与平均单价
SELECT
    Supplier,
    SUM(Quantity) AS TotalQuantity,
    ROUND(AVG(UnitPrice), 2) AS AverageUnitPrice
FROM supply_orders
GROUP BY Supplier
ORDER BY TotalQuantity DESC;
