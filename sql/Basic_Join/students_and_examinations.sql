WITH 
    students_subjects AS (
        SELECT
            *
        FROM 
            students
        CROSS JOIN subjects
    ),
    n_time_attended AS (
        SELECT
            *,
            COUNT(*) AS attended_exams
        FROM 
            examinations
        GROUP BY 
            student_id, subject_name
    )

SELECT 
    t1.student_id,
    t1.student_name,
    t1.subject_name,
    COALESCE(t2.attended_exams, 0) AS attended_exams
FROM 
    students_subjects t1
LEFT JOIN 
    n_time_attended t2 ON t1.student_id = t2.student_id AND t1.subject_name = t2.subject_name
ORDER BY 
    student_id, subject_name