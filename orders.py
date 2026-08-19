from utils import load,save
# Add a new order.
products = load("data/products.json")
users = load("data/users.json")
orders = load("data/orders.json")
def add_order():
    order_id = int(input("Enter order id: "))
    for i in orders:
        if i["id"] == order_id:
            print("This id already exists!")
            return
    user_id = int(input("Enter order user id: "))
    flag_user = False
    for i in users:
        if i["id"] == user_id:
            flag_user = True
    if not flag_user:
        print("User not found!")
        return
    product_cnt = int(input("Enter cnt of product: "))
    product_lst = []
    for i in range(0,product_cnt):
        product_id = int(input("Enter order product id: "))
        flag_product = False
        for i in products:
            if i["id"] == product_id:
                flag_product = True
        if not flag_product:
            print("Product not found!")
            return
        quantity = int(input("Enter product quantity: "))
        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return
        # Update product stock after ordering.
        for product in products:
            if product["id"] == product_id:
                if product["stock"] < quantity:
                    print("Not enough stock!")
                    return
                product["stock"] -= quantity
                break    
        productd = {
            "product_id":product_id,
            "quantity":quantity
        }
        product_lst.append(productd)
        total = 0
        for productd in product_lst:
            for product in products:
                if product["id"] == productd["product_id"]:
                    total += product["price"] * productd["quantity"]
                    break
        order = {
        "id":order_id,
        "user_id":user_id,
        "products":product_lst,
        "total": total
        }
    orders.append(order)
    save("data/products.json", products)
    save("data/orders.json",orders)
# Display all orders.
def show_orders():
    for i in orders:
        print(f"ID: {i["id"]}\nUSER_ID: {i["user_id"]}\nPRODUCTS: {i["products"]}\nTOTAL: {i["total"]}")
        print("_________________________________________________")
# Search for an order by ID.
def search_order():
    order_id = int(input("Enter order ID: "))
    for i in orders:
        if i["id"] == order_id:
            print(f"ID: {i["id"]}\nUSER_ID: {i["user_id"]}\nPRODUCTS: {i["products"]}\nTOTAL: {i["total"]}")
            return
    print("Order not found!")
# Delete an order by ID.
def delete_order():
    order_id = int(input("Enter order ID: "))
    for order in orders:
        if order["id"] == order_id:
            for item in order["products"]:
                for product in products:
                    if product["id"] == item["product_id"]:
                        product["stock"] += item["quantity"]
                        break
            orders.remove(order)
            save("data/products.json", products)
            save("data/orders.json", orders)
            print("Order deleted successfully!")
            return
    print("Order not found!")
# Update an order product quantity.
def update_order():
    order_id = int(input("Enter order ID: "))
    for order in orders:
        if order["id"] == order_id:
            product_id = int(input("Enter product ID: "))
            for product in order["products"]:
                if product["product_id"] == product_id:
                    quantity = int(input("Enter new quantity: "))
                    if quantity <= 0:
                        print("Quantity must be greater than zero!")
                        return
                    product["quantity"] = quantity
                    save("data/orders.json", orders)
                    print("Order updated successfully!")
                    return
            print("Product not found in this order!")
            return
    print("Order not found!")
# Display orders of a specific user.
def show_user_orders():
    user_id = int(input("Enter user ID: "))
    flag = False
    for i in orders:
        if i["user_id"] == user_id:
            print(f"ID: {i["id"]}\nUSER_ID: {i["user_id"]}\nPRODUCTS: {i["products"]}\nTOTAL: {i["total"]}")
            print("_________________________________________________")
            flag = True
    if not flag:
        print("No orders found for this user!")
# Display orders containing a specific product.
def show_product_orders():
    product_id = int(input("Enter product ID: "))
    flag = False
    for i in orders:
        for product in i["products"]:
            if product["product_id"] == product_id:
                print(i)
                flag = True
                break
    if not flag:
        print("No orders found for this product!")
# Display orders above a specific total price.
def filter_orders_by_price():
    price = int(input("Enter minimum order price: "))
    for i in orders:
        if i["total"] >= price:
            print(i)
# Sort orders by total price.
def sort_orders_by_price():
    sorted_orders = sorted(orders, key=lambda i: i["total"])
    for i in sorted_orders:
        print(i)
# Sort orders by total product quantity.
def sort_orders_by_quantity():
    sorted_orders = sorted(orders,key=lambda i: sum(product["quantity"] for product in i["products"]))
    for i in sorted_orders:
        print(i)
# Calculate total sales.
def total_sales():
    total = 0
    for i in orders:
        total += i["total"]
    print("Total sales:", total)