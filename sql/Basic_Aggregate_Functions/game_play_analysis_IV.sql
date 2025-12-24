WITH 
    retained_players AS (
        SELECT
            player_id,
            event_date,
            LAG(DATEADD(DAY, 1, event_date)) OVER(PARTITION BY player_id ORDER BY event_date) AS should_next_login,
            RANK() OVER(PARTITION BY player_id ORDER BY event_date) AS nth_login
        FROM
            activity
    )

SELECT 
    ROUND(
        (
            SELECT 
                COUNT(DISTINCT player_id) 
            FROM retained_players
            WHERE nth_login = 2 AND should_next_login = event_date
        ) * 1.0
        /
        (
            SELECT 
                COUNT(DISTINCT player_id) 
            FROM retained_players
        ),
        2
    ) AS fraction