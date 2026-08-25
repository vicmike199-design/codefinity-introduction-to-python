# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Combine list into tuples in order
combined_list = list(zip(products, prices, quantities_sold))

# Sort combined list by product name
sorted_products = sorted(combined_list)

# Print each product's values
for name, price, qty in sorted_products:
    print(f"Product: {name}, Price: {price}, Quantity Sold: {qty}")





