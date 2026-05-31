select *from sales_data

-- Top profitable products
SELECT product_name,
       SUM(gross_profit) AS total_profit
FROM sales_data
GROUP BY product_name
ORDER BY total_profit DESC;


-- High Sale But Low Margin
SELECT product_name,
       SUM(sales) AS revenue,
       AVG(gross_margin_percent) AS avg_margin
FROM sales_data
GROUP BY product_name
HAVING AVG(gross_margin_percent) < 20
ORDER BY revenue DESC;

-- Division Performance
SELECT division,
       SUM(sales) AS total_sales,
       SUM(gross_profit) AS total_profit,
       AVG(gross_margin_percent) AS avg_margin
FROM sales_data
GROUP BY division;


-- Problem Statements

-- 1. Which Product Lines Deliver the Highest Gross Margin?

SELECT
    product_name,
    
    ROUND(
        AVG("gross_margin_percent")::numeric,
        2
    ) AS avg_gross_margin

FROM sales_data

GROUP BY product_name

ORDER BY avg_gross_margin DESC;


-- 2. Whether High-Sales Products Are Actually Profitable?
SELECT
    division,

    ROUND(SUM(sales)::numeric,2) AS total_sales,

    ROUND(SUM(gross_profit)::numeric,2) AS total_profit,

    ROUND(
        AVG("gross_margin_percent")::numeric,
        2
    ) AS avg_margin

FROM sales_data

GROUP BY division

ORDER BY total_profit DESC;


-- 3. FIND HIGH-SALES LOW-MARGIN PRODUCTS
SELECT
    product_name,

    ROUND(SUM(sales)::numeric,2) AS total_sales,

    ROUND(
        AVG("gross_margin_percent")::numeric,
        2
    ) AS avg_margin

FROM sales_data

GROUP BY product_name

HAVING
    SUM(sales) >
    (
        SELECT AVG(sales)
        FROM sales_data
    )

AND
    AVG("gross_margin_percent") < 40

ORDER BY total_sales DESC;

-- 4. How Profitability Varies Across Product Divisions?
SELECT
    division,

    ROUND(SUM(sales)::numeric,2) AS total_sales,

    ROUND(SUM(gross_profit)::numeric,2) AS total_profit,

    ROUND(
        AVG("gross_margin_percent")::numeric,
        2
    ) AS avg_margin,

    SUM(units) AS total_units

FROM sales_data

GROUP BY division

ORDER BY total_profit DESC;


-- 5.Which Products Represent Margin Risk?
SELECT
    product_name,

    ROUND(SUM(sales)::numeric,2) AS total_sales,

    ROUND(SUM(cost)::numeric,2) AS total_cost,

    ROUND(SUM(gross_profit)::numeric,2) AS total_profit,

    ROUND(
        AVG("gross_margin_percent")::numeric,
        2
    ) AS avg_margin

FROM sales_data

GROUP BY product_name

HAVING
    AVG("gross_margin_percent") < 40

ORDER BY avg_margin ASC;


