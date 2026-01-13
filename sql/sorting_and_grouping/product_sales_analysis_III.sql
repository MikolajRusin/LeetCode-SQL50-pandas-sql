WITH first_year AS (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM sales
    GROUP BY product_id
)

SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM sales s
INNER JOIN first_year fy ON s.product_id = fy.product_id AND s.year = fy.first_year

--- OR ---

SELECT
    product_id,
    year as first_year,
    quantity,
    price
FROM (
    SELECT
        s.*,
        MIN(year) OVER(PARTITION BY product_id) AS first_year
    FROM sales s
) t1
WHERE year = first_year