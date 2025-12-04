WITH 
    calc_sales AS (
        SELECT
            p.product_id,
            CASE
                WHEN purchase_date BETWEEN start_date AND end_date THEN p.price * s.units
                ELSE 0
            END AS total_price,
            CASE
                WHEN purchase_date BETWEEN start_date AND end_date THEN s.units
                ELSE 0
            END AS units
        FROM
            prices p
        LEFT JOIN
            UnitsSold s ON p.product_id = s.product_id
    )
SELECT
    product_id,
    COALESCE(
        ROUND(
            CAST(SUM(total_price) AS FLOAT) / NULLIF(SUM(units), 0),
            2
        ),
        0
    ) AS average_price
FROM 
    calc_sales
GROUP BY
    product_id

--------- OR ---------

SELECT 
    p.product_id,
    ROUND(
        COALESCE(
            SUM(CASE
                WHEN purchase_date BETWEEN start_date AND end_date THEN CAST(p.price AS FLOAT) * s.units
                ELSE 0
            END) /
            NULLIF(SUM(CASE
                WHEN purchase_date BETWEEN start_date AND end_date THEN s.units
                ELSE 0
            END), 0),
        0),
    2)AS average_price
FROM 
    prices p
LEFT JOIN
    UnitsSold s ON p.product_id = s.product_id
GROUP BY
    p.product_id