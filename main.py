from auth import Authentication
from models import Car, User
from database import Database
import utils

def main():
    auth = Authentication()
    db = Database()

    while True:
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            user = auth.login()
            if user:
                manage_data(user, db)
        elif choice == "2":
            auth.register()
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def manage_data(user, db):
    while True:
        print("1. Добавить автомобиль")
        print("2. Просмотреть автомобили")
        print("3. Удалить автомобиль")
        print("4. Сортировать автомобили")
        print("5. Фильтровать автомобили")
        print("6. Импортировать данные")
        print("7. Экспортировать данные")
        print("8. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            add_car(user, db)
        elif choice == "2":
            view_cars(db)
        elif choice == "3":
            delete_car(user, db)
        elif choice == "4":
            sort_cars(db)
        elif choice == "5":
            filter_cars(db)
        elif choice == "6":
            utils.import_data(db)
        elif choice == "7":
            utils.export_data(db)
        elif choice == "8":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def add_car(user, db):
    if user.role == "admin":
        model = input("Введите модель автомобиля: ")
        year = input("Введите год выпуска: ")
        price = input("Введите цену: ")
        car = Car(model, year, price)
        db.add_car(car)
        print("Автомобиль добавлен.")
    else:
        print("У вас нет прав для добавления автомобиля.")

def view_cars(db):
    cars = db.get_cars()
    for car in cars:
        print(car)

def delete_car(user, db):
    if user.role == "admin":
        car_id = input("Введите ID автомобиля для удаления: ")
        db.delete_car(car_id)
        print("Автомобиль удален.")
    else:
        print("У вас нет прав для удаления автомобиля.")

def sort_cars(db):
    cars = db.get_cars()
    sorted_cars = sorted(cars, key=lambda x: x.year)
    for car in sorted_cars:
        print(car)

def filter_cars(db):
    year = input("Введите год для фильтрации: ")
    cars = db.get_cars_by_year(year)
    for car in cars:
        print(car)

if __name__ == "__main__":
    main()
