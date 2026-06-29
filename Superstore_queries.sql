-- Superstore Sales Analysis
-- Author: Praveen Raj K
-- Tool: MySQL Workbench

USE superstore;

-- Query 1: Total row count
SELECT COUNT(*) FROM orders;

-- Query 2: Top 10 products by total sales
SELECT `Product Name`, 
       ROUND(SUM(Sales), 2) AS total_sales
FROM orders
GROUP BY `Product Name`
ORDER BY total_sales DESC
LIMIT 10;

-- Query 3: Profit by Region with margin %
SELECT Region,
       ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit,
       ROUND((SUM(Profit)/SUM(Sales))*100, 2) AS profit_margin_pct
FROM orders
GROUP BY Region
ORDER BY total_profit DESC;

-- Query 4: Sub-Category profit (shows loss-makers)
SELECT `Sub-Category`,
       ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY `Sub-Category`
ORDER BY total_profit ASC;

-- Query 5: Discount impact on profit
SELECT 
    CASE 
        WHEN Discount = 0 THEN '0% - No Discount'
        WHEN Discount <= 0.2 THEN '1-20% Discount'
        WHEN Discount <= 0.4 THEN '21-40% Discount'
        ELSE 'Above 40% Discount'
    END AS discount_range,
    COUNT(*) AS total_orders,
    ROUND(AVG(Profit), 2) AS avg_profit
FROM orders
GROUP BY discount_range
ORDER BY avg_profit DESC;

-- Query 6: Customer Segment performance
SELECT Segment,
       COUNT(DISTINCT `Customer ID`) AS total_customers,
       ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit,
       ROUND((SUM(Profit)/SUM(Sales))*100, 2) AS profit_margin_pct
FROM orders
GROUP BY Segment
ORDER BY total_profit DESC;

-- Query 7: Monthly sales trend
SELECT 
    DATE_FORMAT(STR_TO_DATE(`Order Date`, '%m/%d/%Y'), '%Y-%m') AS month,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit
FROM orders
GROUP BY month
ORDER BY month;

-- Query 8: Top 5 most profitable states
SELECT State,
       ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit,
       ROUND((SUM(Profit)/SUM(Sales))*100, 2) AS profit_margin_pct
FROM orders
GROUP BY State
ORDER BY total_profit DESC
LIMIT 5;