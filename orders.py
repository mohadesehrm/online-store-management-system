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
        if quantity>0:
            flag_quantity=True
        productd = {
            "product_id":product_id,
            "quantity":quantity
        }
        product_lst.append(productd)
        order = {
        "id":order_id,
        "user_id":user_id,
        "products":product_lst,
        "total": 12000
        }
    orders.append(order)
    save("data/orders.json",orders)
# Display all orders.
def show_orders():
    for i in orders:
        print(i["id"],i["user_id"],i["products"],i["total"])