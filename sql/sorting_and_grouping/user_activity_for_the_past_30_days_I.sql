DECLARE @end_date DATE = '2019-07-27'
DECLARE @start_date DATE = DATEADD(day, -29, @end_date)

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    activity
WHERE 
    activity_date BETWEEN @start_date AND @end_date
GROUP BY
    activity_date