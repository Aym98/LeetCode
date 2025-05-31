# Write your MySQL query statement below
SELECT E1.name FROM Employee E1
JOIN (
    SELECT managerId, Count(id) AS reports FROM Employee
    GROUP BY managerId
    HAVING reports > 4
) E2
ON E2.managerId = E1.id