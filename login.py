
DATABASE_NAME = "database.txt"

def append_user(login, password):
    file1 = open(DATABASE_NAME, "a")
    line = "\nlogin : " + login + ", password : " + password
    file1.write(line)
    print(f"Добавлен новый пользователь '{login}'")
    file1.close()

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


read_users()
append_user("robot7", "7777")
append_user("lenka1212", "4545")
read_users()

