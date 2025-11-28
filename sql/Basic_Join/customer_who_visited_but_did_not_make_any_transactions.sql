SELECT
    t1.customer_id,
    COUNT(t1.visit_id) AS count_no_trans
FROM
    visits t1
LEFT JOIN
    transactions t2 ON t1.visit_id = t2.visit_id
WHERE
    t2.transaction_id IS NULL
GROUP BY 
    t1.customer_id