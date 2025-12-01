SELECT
    m.name
FROM
    employee e
INNER JOIN
    employee m ON e.managerId = m.id
GROUP BY
    m.id, m.name
HAVING
    COUNT(m.id) >= 5