# ============================================================
# Superstore Sales Analysis
# Author: Praveen Raj K
# Tools: Python, pandas, matplotlib, seaborn
# Dataset: Sample Superstore (Kaggle - vivek468)
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load Data ──────────────────────────────────────────────
df = pd.read_csv(
    r"C:\Users\SIVANESH\OneDrive\Desktop\da\DA project materials\Sample - Superstore.csv",
    encoding='latin1'
)
print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ── Chart 1: Profit by Region ───────────────────────────────
# Finding: West leads in profit; Central has the weakest margin (8%)
region_profit = df.groupby('Region')['Profit'].sum().reset_index()
region_profit = region_profit.sort_values('Profit', ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=region_profit, x='Region', y='Profit', palette='Blues_d')
plt.title('Total Profit by Region', fontsize=14)
plt.xlabel('Region')
plt.ylabel('Total Profit ($)')
plt.tight_layout()
plt.savefig('chart1_profit_by_region.png')
plt.close()
print("Chart 1 saved — Profit by Region")

# ── Chart 2: Monthly Sales Trend ────────────────────────────
# Finding: Clear upward growth 2014-2017; seasonal spikes every Sep/Nov/Dec
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

plt.figure(figsize=(14, 5))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'],
         color='steelblue', linewidth=2, marker='o', markersize=3)
plt.title('Monthly Sales Trend (2014-2017)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('chart2_monthly_sales_trend.png')
plt.close()
print("Chart 2 saved — Monthly Sales Trend")

# ── Chart 3: Profit by Sub-Category ─────────────────────────
# Finding: Tables (-$17K) and Bookcases (-$3.5K) actively lose money
sub_profit = df.groupby('Sub-Category')['Profit'].sum().reset_index()
sub_profit = sub_profit.sort_values('Profit', ascending=True)
colors = ['red' if x < 0 else 'steelblue' for x in sub_profit['Profit']]

plt.figure(figsize=(12, 6))
plt.barh(sub_profit['Sub-Category'], sub_profit['Profit'], color=colors)
plt.title('Profit by Sub-Category (Red = Loss)', fontsize=14)
plt.xlabel('Total Profit ($)')
plt.ylabel('Sub-Category')
plt.axvline(x=0, color='black', linewidth=0.8)
plt.tight_layout()
plt.savefig('chart3_subcategory_profit.png')
plt.close()
print("Chart 3 saved — Sub-Category Profit")

# ── Chart 4: Discount Rate vs Average Profit ─────────────────
# Finding: Discounts above 20% consistently cause losses
discount_profit = df.groupby('Discount')['Profit'].mean().reset_index()

plt.figure(figsize=(10, 5))
plt.scatter(discount_profit['Discount'], discount_profit['Profit'],
            color='steelblue', alpha=0.7, s=80)
plt.axhline(y=0, color='red', linewidth=1, linestyle='--', label='Break-even line')
plt.title('Discount Rate vs Average Profit', fontsize=14)
plt.xlabel('Discount Rate')
plt.ylabel('Average Profit ($)')
plt.legend()
plt.tight_layout()
plt.savefig('chart4_discount_vs_profit.png')
plt.close()
print("Chart 4 saved — Discount vs Profit")

print("\nAll 4 charts saved successfully!")