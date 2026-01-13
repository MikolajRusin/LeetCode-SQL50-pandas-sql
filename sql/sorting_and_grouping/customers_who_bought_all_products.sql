SELECT
    customer_id
FROM customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM product)

--- OR ---

WITH bought_n_unique_products AS (
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) AS n_products
    FROM customer
    GROUP BY customer_id
)

SELECT
    customer_id
FROM bought_n_unique_products
WHERE n_products = (SELECT COUNT(DISTINCT product_key) FROM product)