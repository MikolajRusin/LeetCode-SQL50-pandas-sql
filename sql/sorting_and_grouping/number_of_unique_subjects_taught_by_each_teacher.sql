/* Write your T-SQL query statement below */
SELECT
    teacher_id,
    COUNT(subject_id) AS cnt
FROM (
    SELECT DISTINCT
        teacher_id,
        subject_id
    FROM 
        teacher
) t1
GROUP BY
    teacher_id