-- Banking Customer Churn Analytics
-- 01 - Customer Churn Analysis

-- 1. Overall customer metrics
SELECT
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    COUNT(*) - SUM(churn) AS retained_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers;


-- 2. Customer distribution by country
SELECT
    country,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    COUNT(*) - SUM(churn) AS retained_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY country
ORDER BY churn_rate_percentage DESC;


-- 3. Churn by gender
SELECT
    gender,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY gender
ORDER BY churn_rate_percentage DESC;


-- 4. Churn by active membership
SELECT
    active_member,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY active_member
ORDER BY active_member DESC;


-- 5. Churn by number of products
SELECT
    products_number,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY products_number
ORDER BY products_number;


-- 6. Churn by credit card ownership
SELECT
    credit_card,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY credit_card
ORDER BY credit_card DESC;


-- 7. Customer balance segments
SELECT
    CASE
        WHEN balance = 0 THEN 'Zero Balance'
        WHEN balance < 50000 THEN 'Below 50K'
        WHEN balance < 100000 THEN '50K-100K'
        WHEN balance < 150000 THEN '100K-150K'
        ELSE '150K+'
    END AS balance_segment,
    COUNT(*) AS total_customers,
    SUM(churn) AS churned_customers,
    ROUND(100.0 * SUM(churn) / COUNT(*), 2) AS churn_rate_percentage
FROM customers
GROUP BY balance_segment
ORDER BY
    CASE balance_segment
        WHEN 'Zero Balance' THEN 1
        WHEN 'Below 50K' THEN 2
        WHEN '50K-100K' THEN 3
        WHEN '100K-150K' THEN 4
        WHEN '150K+' THEN 5
    END;