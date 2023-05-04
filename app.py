from database import SqliteDatabase

db = SqliteDatabase("user_data.db")
db.create_database()


def register_user(login):
    name = input("Enter name ")
    surname = input("Enter surname ")
    password = input("Enter password ")
    db.create_user(name=name, surname=surname, email=login, password=password)
    print("Registered succesfully, now login to get to Your data!")


def add_data(userid):
    data_type = input("Enter data type ")
    attribute = input("Enter data ")
    attribute2 = input("Enter more data ")
    db.create_data(
        type=data_type, attribute=attribute, attribute2=attribute2, user_id=userid
    )
    print("Data added succesfully")


def get_data(userid):
    got_data = db.get_data(userid=userid)
    for data in got_data:
        print(data)


def update_data(userid):
    dataid = int(input("Which line do You want to update? "))
    field = input("Which field do You want to update: type, attribute or attribute2 ")
    value = input("What value do You want to insert? ")
    db.update_data(userid=userid, dataid=dataid, field=field, value=value)


def delete_data(userid):
    dataid = int(input("Which line do You want to delete? "))
    db.delete_data(userid=userid, dataid=dataid)


print("Hi please be patient!")

login = input("Enter Your email ")

user_list = db.get_users()
user_exists = False
for user in user_list:
    if user.email == login:
        pass_correct = False
        while pass_correct is False:
            user_password = input("Enter password ")
            if user.password == user_password:
                print(f"Hi, {user.name}")
                pass_correct = True
        user_exists = True

if user_exists is False:
    print("You are new User, please register")
    register_user(login)


if user_exists is True and pass_correct is True:
    print("You can now access Your data")
    while True:
        current_user = db.get_user_by_email(login)
        selection = input(
            """Type:
        '1' to list Your data, 
        '2' to enter more data, 
        '3' to edit data, 
        '4' to delete line of data.
        Or anything else to exit """
        )
        if selection == "1":
            get_data(userid=current_user.id)
        elif selection == "2":
            add_data(userid=current_user.id)
        elif selection == "3":
            update_data(userid=current_user.id)
        elif selection == "4":
            delete_data(userid=current_user.id)
        else:
            print("Be carefull, now You'll have to login again!")
            break
