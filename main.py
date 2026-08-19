import products, users, orders, reports
# Display the main menu.
def main_menu():
    print("--------------ONLINE STORE MANAGEMENT SYSTEM--------------")
    print("1. Product Management\n2. User Management\n3. Order Management\n4. Reports\n5. Exit")
    print("----------------------------------------------------------")
while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice == "1" or choice == "۱":
        print("Product Management")
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
