from utils import load,save
# Add a new product to the store.
def add():
    products = load("data/products.json")
    product_id = int(input("Enter product ID: "))
    for i in products:
        if i["id"] == product_id:
            print("This id already exists!")
            return
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    if price < 0:
        print("Price cannot be negative!")
        return
    stock = int(input("Enter product stock: "))
    if stock < 0:
        print("Stock cannot be negative!")
        return
    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(product)
    save("data/products.json", products)
