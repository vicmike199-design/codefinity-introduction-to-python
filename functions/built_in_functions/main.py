# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

# For loop to iterate through products between key and list items
for product_name, values in products.items():
    # Converts price into float
    price = float(values[0])
    # Converts quanity sold as int
    quantity_sold = int(values[1])
    # Multiply price and quantity of each product
    total_sales = price * quantity_sold
    # Append total sales to total sales list
    total_sales_list.append(total_sales)
    # Sum of all sales
    total_sum = sum(total_sales_list)
    # Get min and max sales values
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
    # Print total sales for each product
    print(f"Total sales for {product_name}: ${total_sales:.2f}")
    # Print total, min, and max sales
    print(f"Total sum of all sales: ${total_sales}")
    print(f"Minimum sales: ${min_sales}")
    print(f"Maximum sales: ${max_sales}")
    



