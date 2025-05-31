# Write your MySQL query statement below
SELECT DATE_FORMAT(T.trans_date, '%Y-%m') AS month,
T.country, COUNT(T.id) AS trans_count,
SUM(2 - T.state) AS approved_count,
SUM(T.amount) AS trans_total_amount,  
SUM((2 - T.state) * T.amount) AS approved_total_amount
FROM Transactions T
GROUP BY month, country