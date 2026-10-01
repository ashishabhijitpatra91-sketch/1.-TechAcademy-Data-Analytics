import pandas as pd

# Load cleaned data
try:
    df = pd.read_csv('cleaned_ecommerce_data.csv')
except FileNotFoundError:
    print("Error: Please run task1_data_cleaning.py first to generate the dataset!")
    exit()

print("--- Statistical Summary ---")
print(df.describe())

# 1. Product wise total sales
product_sales = df.groupby('Product')['TotalSales'].sum().sort_values(ascending=False)
print("\n--- Product-wise Revenue ---")
print(product_sales)

# 2. Average Order Value (AOV)
aov = df['TotalSales'].mean()
print(f"\nAverage Order Value: ${aov:.2f}")

# 3. Total Unique Customers count
unique_customers = df['CustomerID'].nunique()
print(f"Total Unique Customers: {unique_customers}")
