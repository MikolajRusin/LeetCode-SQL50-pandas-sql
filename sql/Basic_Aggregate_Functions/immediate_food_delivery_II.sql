WITH 
    customer_nth_order AS (
        SELECT
            customer_id,
            order_date,
            RANK() OVER(PARTITION BY customer_id ORDER BY order_date) as nth_order
        FROM delivery
    ),
    immediate_first_order AS (
        SELECT
            t1.customer_id,
            t1.order_date,
            t1.customer_pref_delivery_date
        FROM delivery t1
        INNER JOIN customer_nth_order t2 ON t1.customer_id = t2.customer_id AND t1.customer_pref_delivery_date = t2.order_date
        WHERE t2.nth_order = 1
    )

SELECT
    ROUND(
        ((SELECT COUNT(DISTINCT customer_id) FROM immediate_first_order) * 1.0 / (SELECT COUNT(DISTINCT customer_id) FROM customer_nth_order WHERE nth_order = 1)) * 100, 
        2) as immediate_percentage