# Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) as average_price
FROM UnitsSold u
RIGHT JOIN Prices p ON p.product_id = u.product_id AND p.start_date <= u.purchase_date AND p.end_date >= u.purchase_date
GROUP BY product_id; 