is_Login = False
Database = {
    "name": "Sijan",
    "cast": "Shrestha",
    "age": 18,
    "id": 20,
    "password": "czon25",
    "email": "czon@gmail.com"
}
show={
    "name":"ram",
    "caste":"any",
    "address":"pokhara",
    "clz":"united"
    
}
def Register():
    database = {
        "name": input("Enter name: "),
        "cast": input("Enter caste: "),
        "age": input("Enter age: "),
        "id": input("Enter id: "),
        "password": input("Enter password: "),
        "email": input("Enter email: "),
    }
    return database

registered_user = Register()


if Database == registered_user:
    def update_global():
     global is_Login 
    is_Login=True
    print(is_Login)
    update_global()
    print("Values match")
    print(show)
    
else:
    print(is_Login)
    print("Wrong person")
