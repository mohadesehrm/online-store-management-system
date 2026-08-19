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
    # Display the order management menu.
def order_menu():
    print("---------------------ORDER MANAGEMENT---------------------")
    print("1. Add Order")
    print("2. Show Orders")
    print("3. Search Order")
    print("4. Delete Order")
    print("5. Update Order")
    print("6. Orders by User")
    print("7. Orders by Product")
    print("8. Filter Orders by Price")
    print("9. Sort Orders by Price")
    print("10. Sort Orders by Quantity")
    print("11. Total Sales")
    print("12. Back")
    print("----------------------------------------------------------")
# Display the reports menu.
def report_menu():
    print("-------------------------REPORTS--------------------------")
    print("1. Best-Selling Products")
    print("2. Revenue by User")
    print("3. Total Revenue")
    print("4. Low-Stock Products")
    print("5. Out-of-Stock Products")
    print("6. Orders by User")
    print("7. Average Order Value")
    print("8. Highest Order")
    print("9. Lowest Order")
    print("10. Total Products Sold")
    print("11. Products by Category")
    print("12. Back")
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
        while True:
            user_menu()
            user_choice = input("Enter your choice: ")
            if user_choice == "1" or user_choice == "۱":
                users.add_user()
            elif user_choice == "2" or user_choice == "۲":
                users.show_users()
            elif user_choice == "3" or user_choice == "۳":
                users.search_user()
            elif user_choice == "4" or user_choice == "۴":
                users.delete_user()
            elif user_choice == "5" or user_choice == "۵":
                users.update_user()
            elif user_choice == "6" or user_choice == "۶":
                users.show_vip_users()
            elif user_choice == "7" or user_choice == "۷":
                break
            else:
                print("Invalid choice!")
    elif choice == "3" or choice == "۳":
        if order_choice == "1" or order_choice == "۱":
            orders.add_order()
        elif order_choice == "2" or order_choice == "۲":
            orders.show_orders()
        elif order_choice == "3" or order_choice == "۳":
            orders.search_order()
        elif order_choice == "4" or order_choice == "۴":
            orders.delete_order()
        elif order_choice == "5" or order_choice == "۵":
            orders.update_order()
        elif order_choice == "6" or order_choice == "۶":
            orders.show_user_orders()
        elif order_choice == "7" or order_choice == "۷":
            orders.show_product_orders()
        elif order_choice == "8" or order_choice == "۸":
            orders.filter_orders_by_price()
        elif order_choice == "9" or order_choice == "۹":
            orders.sort_orders_by_price()
        elif order_choice == "10" or order_choice == "۱۰":
            orders.sort_orders_by_quantity()
        elif order_choice == "11" or order_choice == "۱۱":
            orders.total_sales()
        elif order_choice == "12" or order_choice == "۱۲":
            break
        else:
            print("Invalid choice!")
    elif choice == "4" or choice == "۴":
        while True:
            report_menu()
            report_choice = input("Enter your choice: ")
            if report_choice == "1" or report_choice == "۱":
                reports.best_selling_products()
            elif report_choice == "2" or report_choice == "۲":
                reports.revenue_by_user()
            elif report_choice == "3" or report_choice == "۳":
                reports.total_revenue()
            elif report_choice == "4" or report_choice == "۴":
                reports.low_stock_products()
            elif report_choice == "5" or report_choice == "۵":
                reports.out_of_stock_products()
            elif report_choice == "6" or report_choice == "۶":
                reports.orders_by_user()
            elif report_choice == "7" or report_choice == "۷":
                reports.average_order_value()
            elif report_choice == "8" or report_choice == "۸":
                reports.highest_order()
            elif report_choice == "9" or report_choice == "۹":
                reports.lowest_order()
            elif report_choice == "10" or report_choice == "۱۰":
                reports.total_products_sold()
            elif report_choice == "11" or report_choice == "۱۱":
                reports.products_by_category()
            elif report_choice == "12" or report_choice == "۱۲":
                break
            else:
                print("Invalid choice!")
    elif choice == "5" or choice == "۵":
        print("Exit!")
        break
    else:
        print("Invalid choice!")