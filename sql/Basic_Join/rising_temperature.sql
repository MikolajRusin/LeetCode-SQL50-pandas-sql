SELECT
    id
FROM (
    SELECT
        id,
        recordDate,
        temperature,
        LAG(temperature, 1) OVER(ORDER BY recordDate) AS prev_temp,
        LAG(recordDate, 1) OVER(ORDER BY recordDate) AS prev_day
    FROM weather
) t1
WHERE
    temperature > prev_temp
    AND DATEDIFF(day, prev_day, recordDate) = 1