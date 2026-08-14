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
# Display all products.
def show():
    products = load("data/products.json")
    for i in products:
        print(i["id"],i["name"],i["category"],i["price"],i["stock"])
# Search for a product by name.
def search_name():
    products = load("data/products.json")
    name = input("Enter product name: ")
    for i in products:
        if name.lower() in i["name"].lower():
            print(i["id"],i["name"],i["category"],i["price"],i["stock"])
        else:
            print("Product not found!")
# Search for products by category.
def search_category():
    products = load("data/products.json")
    category = input("Enter product category: ")
    for i in products:
        if category.lower() in i["category"].lower():
            print(i["id"],i["name"],i["category"],i["price"],i["stock"])
        else:
            print("Product not found!")
# Delete a product from the store.
def delete():
    flag = False
    products = load("data/products.json")
    product_id = int(input("Enter product ID: "))
    for i in products:
        if product_id == i["id"]:
            flag = True
        if flag:
            products.remove(i)
            print("Product deleted successfully!")
            break
    if not flag:
        print("Product not found!")
    save("data/products.json",products)
# Update an existing product.
def update():
    products = load("data/products.json")
    product_id = int(input("Enter product ID: "))
    flag = False
    for i in products:
        if product_id == i["id"]:
            flag = True
            break
    if flag:
        name = input("Enter product name: ")
        i["name"] = name
        category = input("Enter product category: ")
        i["category"] = category
        price = int(input("Enter product price: "))
        i["price"] = price
        stock = int(input("Enter product stock: "))
        i["stock"] = stock
        print("Product updated successfully!")
    else:
        print("Product not found!")
    save("data/products.json",products)
# Sort products by price.
def sort_price():
    products = load("data/products.json")
    products_sort = sorted(products,key=lambda i : i["price"])
    for i in products_sort:
        print(i["id"],i["name"],i["category"],i["price"],i["stock"])
# Sort products by stock.
def sort_stock():
    products = load("data/products.json")
    products_sort = sorted(products,key=lambda i : i["stock"])
    for i in products_sort:
        print(i["id"],i["name"],i["category"],i["price"],i["stock"])
# Filter products that are in stock.
def filter_products():
    products = load("data/products.json")
    products_filter = list(filter(lambda i : i["stock"]>0,products))
    for i in products_filter:
        print(i["id"],i["name"],i["category"],i["price"],i["stock"])
# Calculate the total inventory value of each product.
def inventory_value():
    products = load("data/products.json")
    value = list(map(lambda i : (i["name"] , i["price"] * i["stock"]), products))
    for i in value:
        print(i[0],i[1])
