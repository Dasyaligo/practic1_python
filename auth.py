import json
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

    def export_to_file(self, filename):
        with open(filename, 'w') as file:
            users_data = [{'username': user.username, 'password': user.password, 'role': user.role} for user in self.users]
            json.dump(users_data, file)
        print(f"Данные экспортированы в файл {filename}.")

    def import_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                users_data = json.load(file)
                self.users = [User(user['username'], user['password'], user['role']) for user in users_data]
            print(f"Данные импортированы из файла {filename}.")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла {filename}. Возможно, он поврежден или имеет неверный формат.")
