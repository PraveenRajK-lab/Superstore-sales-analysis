# Superstore Sales Analysis

**Tools Used:** Excel | MySQL | Python (pandas, matplotlib, seaborn)
**Dataset:** Sample Superstore — 9,994 orders (2014–2017)

## Objective
Analyse sales and profit data from a US retail superstore to identify
underperforming products, regions, and the impact of discounting on
overall profitability.

## Process
1. **Excel** — Cleaned the raw dataset (removed duplicates, fixed date
   formats, added a calculated shipping delay column) and built Pivot
   Tables to get an initial view of performance by Region and Category.
2. **MySQL** — Imported the cleaned data and ran 8 queries to dig deeper
   into product, region, discount, and customer segment performance.
3. **Python** — Used pandas to recreate and extend the SQL analysis, and
   built 4 charts with matplotlib/seaborn to visualise the key findings.

## Key Findings

| # | Finding |
|---|---------|
| 1 | West region leads in total profit ($106K, 14.9% margin); Central has the weakest margin (8.1%) despite similar sales volume |
| 2 | Tables sub-category loses **-$17,725** despite generating $206K in sales — the single biggest drag on profitability |
| 3 | Discounts above 20% consistently result in average losses; discounts above 40% average a **-$111** loss per order |
| 4 | Home Office is the smallest customer segment but has the highest profit margin (14.05%) |
| 5 | Sales peak every September, November and December across all four years — a clear seasonal pattern |
| 6 | New York and Michigan are the most profit-efficient states (23–32% margin), ahead of California despite lower sales volume |

## Charts

### Profit by Region
![Profit by Region](chart1_profit_by_region.png)

### Monthly Sales Trend (2014–2017)
![Monthly Sales Trend](chart2_monthly_sales_trend.png)

### Profit by Sub-Category (Red = Loss)
![Sub-Category Profit](chart3_subcategory_profit.png)

### Discount Rate vs Average Profit
![Discount vs Profit](chart4_discount_vs_profit.png)

## Files in this Repository

| File | Description |
|------|-------------|
| `super store analysis in Excel.xlsx` | Cleaned dataset with Pivot Tables and charts |
| `Superstore_queries.sql` | 8 SQL queries used for analysis (MySQL) |
| `superstore_analysis.py` | Python script — loads data, generates all 4 charts |
| `chart1_profit_by_region.png` | Region-wise profit comparison |
| `chart2_monthly_sales_trend.png` | Monthly sales trend across 4 years |
| `chart3_subcategory_profit.png` | Profit/loss by product sub-category |
| `chart4_discount_vs_profit.png` | Relationship between discount rate and average profit |

## Skills Demonstrated
- **Excel:** Data cleaning, duplicate removal, calculated columns, Pivot Tables
- **SQL:** Aggregations, GROUP BY, CASE statements, date functions, multi-table style analysis
- **Python:** Data manipulation with pandas, data visualisation with matplotlib and seaborn

## Author
**Praveen Raj K**
[LinkedIn](https://linkedin.com/in/praveenrajk010371) | praveenraj.kaniraj@gmail.com
