from models import User

class Authentication:
    def __init__(self):
        self.users = []

    def register(self):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        role = input("Введите роль (user/admin): ")
        user = User(username, password, role)
        self.users.append(user)
        print("Пользователь зарегистрирован.")

    def login(self):
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        for user in self.users:
            if user.username == username and user.password == password:
                print("Авторизация успешна.")
                return user
        print("Неверное имя пользователя или пароль.")
        return None
