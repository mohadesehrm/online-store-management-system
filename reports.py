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
# Display out-of-stock products.
def out_of_stock_products():
    for product in products:
        if product["stock"] == 0:
            print(f"ID: {product["id"]}\nName: {product["name"]}")
            print("________________________")
# Count orders for each user.
def orders_by_user():
    order_count = {}
    for order in orders:
        user_id = order["user_id"]
        if user_id in order_count:
            order_count[user_id] += 1
        else:
            order_count[user_id] = 1
    for user_id, count in order_count.items():
        print(f"User ID: {user_id}\nOrders: {count}")
        print("________________________")
# Calculate the average order value.
def average_order_value():
    total = 0
    for order in orders:
        total += order["total"]
    average = total / len(orders)
    print("Average order value:", average)
# Display the most expensive order.
def highest_order():
    maxx = orders[0]
    for order in orders:
        if order["total"] > maxx["total"]:
            maxx = order
    print(f"ID: {maxx["id"]}\nUSER_ID: {maxx["user_id"]}\nPRODUCTS: {maxx["products"]}\nTOTAL: {maxx["total"]}")
# Display the cheapest order.
def lowest_order():
    minn = orders[0]
    for order in orders:
        if order["total"] < minn["total"]:
            minn = order
    print(f"ID: {minn["id"]}\nUSER_ID: {minn["user_id"]}\nPRODUCTS: {minn["products"]}\nTOTAL: {minn["total"]}")
# Calculate the total quantity of products sold.
def total_products_sold():
    cnt = 0
    for order in orders:
        for product in order["products"]:
            cnt += product["quantity"]
    print("Total products sold:", cnt)
# Count products in each category.
def products_by_category():
    categories = {}
    for product in products:
        category = product["category"]
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1
    for category, count in categories.items():
        print(f"Category: {category}\nProducts: {count}")
        print("________________________")