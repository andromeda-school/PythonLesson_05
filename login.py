
DATABASE_NAME = "database.txt"

def append_user(login, password):
    if not find_login(login):
        file1 = open(DATABASE_NAME, "a")
        line = "\nlogin : " + login + ", password : " + password
        file1.write(line)
        print(f"Добавлен новый пользователь '{login}'")
        file1.close()
    else:
        print("Этот логин уже занят!")

def read_users():
    file1 = open(DATABASE_NAME, "r")
    arr = file1.readlines()
    login_arr = []
    password_arr = []

    for acc in arr:
        login = acc.split(",")[0].split(":")[1].strip()
        password = acc.split(",")[1].split(":")[1].strip()
        login_arr.append(login)
        password_arr.append(password)

    for i in range(len(login_arr)):
        print(f"User #{i+1} --> {login_arr[i]} : {password_arr[i]} ")

    file1.close()


def find_login(login):
    file1 = open(DATABASE_NAME, "r")
    arr = file1.readlines()
    for acc in arr:
        user_login = acc.split(",")[0].split(":")[1].strip()
        if user_login == login:
            return True
    file1.close()
    return False

def check_password(login, password):
    file1 = open(DATABASE_NAME, "r")
    arr = file1.readlines()
    for acc in arr:
        user_login = acc.split(",")[0].split(":")[1].strip()
        if user_login == login:
            user_password = acc.split(",")[1].split(":")[1].strip()
            if password == user_password:
                print("Успешно! Добро пожаловать!")
                file1.close()
                return True
            else:
                print("Пароль неверный.")
                file1.close()
                return False
    file1.close()
    return False


login = input("Введите логин: ")
while not find_login(login):
    print("Такого пользователя нет в системе.\n")
    login = input("Введите логин: ")

password = input("Введите пароль: ")
while not check_password(login, password):
    password = input("Введите пароль: ")
