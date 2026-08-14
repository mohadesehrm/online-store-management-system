from utils import save,load
# Add a new user.
def add_user():
    users = load("data/users.json")
    users_id = int(input("Enter user id: "))
    for i in users:
        if i["id"] == users_id:
            print("This id already exists!")
            return
    name = input("Enter user name: ")
    phone = input("Enter user phone: ")
    city = input("Enter user city: ")
    vip = input("Enter user vip: ")
    user = {
        "id":users_id,
        "name":name,
        "phone":phone,
        "city":city,
        "vip":vip
    }
    users.append(user)
    save("data/users.json",users)