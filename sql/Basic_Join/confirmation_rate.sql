with 
    counts AS (
        SELECT 
            user_id,
            [confirmed] AS confirmed,
            [timeout] AS timeout
        FROM (
            SELECT 
                user_id, 
                time_stamp, 
                action 
            FROM 
                Confirmations
        ) AS src
        PIVOT
        (
            COUNT(time_stamp)
            FOR action IN ([confirmed], [timeout])
        ) AS pvt
    )

SELECT 
    s.user_id,
    ROUND(COALESCE(CAST(confirmed AS FLOAT) / (confirmed + timeout), 0), 2) AS confirmation_rate
FROM 
    signups s
LEFT JOIN
    counts c ON s.user_id = c.user_id
