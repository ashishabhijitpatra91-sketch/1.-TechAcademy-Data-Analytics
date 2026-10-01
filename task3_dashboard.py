import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('cleaned_ecommerce_data.csv')
except FileNotFoundError:
    print("Error: Please run task1_data_cleaning.py first to generate the dataset!")
    exit()

# Plotting Sales per Product
plt.figure(figsize=(10, 5))
product_sales = df.groupby('Product')['TotalSales'].sum().sort_values()
product_sales.plot(kind='barh', color='skyblue', edgecolor='black')

plt.title('Key Performance Indicator (KPI): Revenue by Product', fontsize=14)
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Product Name', fontsize=12)
plt.tight_layout()

# Save chart as image
plt.savefig('kpi_dashboard_visualization.png')
print("KPI Chart saved successfully as 'kpi_dashboard_visualization.png'!")
plt.show()
