import pandas as pd
import numpy as np

# 1. Data Ingestion (Loading raw e-commerce sales data)
data = {
    'OrderID': [101, 102, 103, 104, 104, 105, 106, 107],
    'CustomerID': [501, 502, np.nan, 504, 504, 505, 506, 507],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Monitor', 'Headphones', 'Laptop', 'Smartwatch'],
    'Quantity': [1, 2, 1, -5, 2, np.nan, 1, 3],
    'PriceEach': [1200, 25, 75, 300, 300, 150, 1200, np.nan],
    'OrderDate': ['2026-01-15', '2026-01-16', '2026-01-16', '2026-01-17', '2026-01-17', '2026-01-18', '2026-01-19', '2026-01-20']
}
df = pd.DataFrame(data)
print("--- Raw Data Loaded ---")
print(df)

# 2. Data Cleaning & Preprocessing
df = df.drop_duplicates()
df['Quantity'] = df['Quantity'].apply(lambda x: abs(x) if pd.notnull(x) else x)
df['CustomerID'] = df['CustomerID'].fillna(0).astype(int)
df['Quantity'] = df['Quantity'].fillna(1).astype(int)
df['PriceEach'] = df['PriceEach'].fillna(df['PriceEach'].median())
df['TotalSales'] = df['Quantity'] * df['PriceEach']
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

print("\n--- Cleaned & Preprocessed Data ---")
print(df)

df.to_csv('cleaned_ecommerce_data.csv', index=False)
print("\nSuccessfully saved to 'cleaned_ecommerce_data.csv'!")
