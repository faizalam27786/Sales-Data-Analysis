import pandas as pd
import seaborn as sns

# File path in C:\Pythonscripts
file_path = "C:/Pythonscripts/sales_data_large.csv"
data = pd.read_csv(file_path)

# Display dataset overview
print("\n==================== DATA OVERVIEW ====================")
print(f"▶ Total Records: {data.shape[0]} | Total Features: {data.shape[1]}")
print("\n▶ Column Data Types:")
print(data.dtypes.to_string())
print("\n▶ Sample Records:")
print(data.head().to_string())

# Handle missing values
data.dropna(inplace=True)

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Remove duplicate entries
data.drop_duplicates(inplace=True)

# Display key statistics for numerical columns
numeric_columns = data.select_dtypes(include=['number'])
print("\n==================== DESCRIPTIVE STATISTICS ====================")
print(numeric_columns.describe().round(2).to_string())

# Identify top 5 products by total revenue
top_products = data.groupby('Product')['Revenue'].sum().nlargest(5)
print("\n==================== TOP 5 PRODUCTS BY REVENUE ====================")
print(top_products.to_string())

# Analyze revenue distribution by category
category_revenue = data.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("\n==================== REVENUE DISTRIBUTION BY CATEGORY ====================")
print(category_revenue.to_string())

# Save the processed data
data.to_csv("C:/Pythonscripts/cleaned_sales_data.csv", index=False)
print("\n✅ PROCESS COMPLETED: Data has been successfully cleaned, analyzed, and saved.")