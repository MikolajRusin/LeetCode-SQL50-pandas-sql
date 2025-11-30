SELECT
    machine_id,
    ROUND(AVG(run_time), 3) AS processing_time
FROM (
    SELECT
        machine_id,
        MAX(timestamp) - MIN(timestamp) AS run_time
    FROM 
        activity
    GROUP BY 
        machine_id, process_id
) t1
GROUP BY machine_id

------------ OR ------------

WITH 
    start_machines AS (
        SELECT
            machine_id,
            process_id,
            timestamp AS start_time
        FROM
            activity
        WHERE
            activity_type = 'start'
    ),
    end_machines AS (
        SELECT
            machine_id,
            process_id,
            timestamp AS end_time
        FROM
            activity
        WHERE
            activity_type = 'end'
    ),
    machine_run_time AS (
        SELECT
            s.machine_id,
            e.end_time - s.start_time AS run_time
        FROM 
            start_machines s
        LEFT JOIN
            end_machines e ON s.machine_id = e.machine_id AND s.process_id = e.process_id
    )

SELECT 
    machine_id,
    ROUND(AVG(run_time), 3) AS processing_time
FROM 
    machine_run_time
GROUP BY 
    machine_id