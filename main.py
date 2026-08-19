import products, users, orders, reports
# Display the main menu.
def main_menu():
    print("--------------ONLINE STORE MANAGEMENT SYSTEM--------------")
    print("1. Product Management\n2. User Management\n3. Order Management\n4. Reports\n5. Exit")
    print("----------------------------------------------------------")
    # Display the product management menu.
def product_menu():
    print("--------------ONLINE STORE MANAGEMENT SYSTEM--------------")
    print("--------------------PRODUCT MANAGEMENT--------------------")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Search by Name")
    print("4. Search by Category")
    print("5. Delete Product")
    print("6. Update Product")
    print("7. Sort by Price")
    print("8. Sort by Stock")
    print("9. Filter In-Stock Products")
    print("10. Inventory Value")
    print("11. Check Stock")
    print("12. Back")
    print("----------------------------------------------------------")
# Display the user management menu.
def user_menu():
    print("----------------------USER MANAGEMENT---------------------")
    print("1. Add User")
    print("2. Show Users")
    print("3. Search User")
    print("4. Delete User")
    print("5. Update User")
    print("6. Show VIP Users")
    print("7. Back")
    print("----------------------------------------------------------")
while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == "1" or choice == "۱":
        while True:
            product_menu()
            product_choice = input("Enter your choice: ")
            if product_choice == "1" or product_choice == "۱":
                products.add_product()
            elif product_choice == "2" or product_choice == "۲":
                products.show_product()
            elif product_choice == "3" or product_choice == "۳":
                products.search_name()
            elif product_choice == "4" or product_choice == "۴":
                products.search_category()
            elif product_choice == "5" or product_choice == "۵":
                products.delete_product()
            elif product_choice == "6" or product_choice == "۶":
                products.update_product()
            elif product_choice == "7" or product_choice == "۷":
                products.sort_price()
            elif product_choice == "8" or product_choice == "۸":
                products.sort_stock()
            elif product_choice == "9" or product_choice == "۹":
                products.filter_products()
            elif product_choice == "10" or product_choice == "۱۰":
                products.inventory_value()
            elif product_choice == "11" or product_choice == "۱۱":
                products.check_stock()
            elif product_choice == "12" or product_choice == "۱۲":
                break
            else:
                print("Invalid choice!")
    elif choice == "2" or choice == "۲":
        print("User Management")
    elif choice == "3" or choice == "۳":
        print("Order Management")
    elif choice == "4" or choice == "۴":
        print("Reports")
    elif choice == "5" or choice == "۵":
        print("Exit!")
        break
    else:
        print("Invalid choice!")
