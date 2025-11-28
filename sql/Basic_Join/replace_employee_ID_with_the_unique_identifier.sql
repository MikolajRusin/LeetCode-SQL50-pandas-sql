SELECT
    t2.unique_id,
    t1.name
FROM
    employees t1
LEFT JOIN 
    employeeuni t2 ON t1.id = t2.id