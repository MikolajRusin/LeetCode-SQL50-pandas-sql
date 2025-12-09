SELECT
    r.contest_id,
    ROUND(
        CAST(COUNT(r.user_id) AS FLOAT) / (SELECT COUNT(DISTINCT user_id) FROM users) * 100, 
        2
    ) AS percentage
FROM
    register r
GROUP BY
    r.contest_id
ORDER BY 
    percentage DESC, contest_id ASC