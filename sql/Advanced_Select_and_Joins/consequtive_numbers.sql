SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        LEAD(num, 1) OVER(ORDER BY id) AS prev_num_1,
        LEAD(num, 2) OVER(ORDER BY id) AS prev_num_2
    FROM Logs
) t1
WHERE 
    num = prev_num_1
    AND num = prev_num_2