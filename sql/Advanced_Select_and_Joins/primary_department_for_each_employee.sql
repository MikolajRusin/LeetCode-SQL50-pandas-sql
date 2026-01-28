SELECT
    employee_id,
    department_id
FROM (
    SELECT
        *,
        COUNT(*) OVER(PARTITION BY employee_id) AS n_deps
    FROM Employee
) t1
WHERE
    primary_flag = 'Y'
    OR n_deps = 1