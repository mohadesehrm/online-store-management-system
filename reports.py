from utils import load
orders = load("data/orders.json")
products = load("data/products.json")
# Display the best-selling products.
def best_selling_products():
    sales = {}
    for order in orders:
        for product in order["products"]:
            product_id = product["product_id"]
            quantity = product["quantity"]
            if product_id in sales:
                sales[product_id] += quantity
            else:
                sales[product_id] = quantity
    sorted_sales = sorted(sales.items(),key=lambda i: i[1],reverse=True)
    for product_id, quantity in sorted_sales:
        print(f"Product ID: {product_id}\nSold: {quantity}")
# Calculate total revenue for each user.
def revenue_by_user():
    revenue = {}
    for order in orders:
        user_id = order["user_id"]
        total = order["total"]
        if user_id in revenue:
            revenue[user_id] += total
        else:
            revenue[user_id] = total
    for user_id, total in revenue.items():
        print(f"User ID:{ user_id}\n Revenue: {total}")
        print("________________________________")
# Calculate total store revenue.
def total_revenue():
    total = 0
    for order in orders:
        total += order["total"]
    print("Total revenue:", total)
# Display products with low stock.
def low_stock_products():
    for product in products:
        if product["stock"] <= 5:
            print(f"ID: {product["id"]}\nName: {product["name"]}\nStock: {product["stock"]}")
            print("________________________")