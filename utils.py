import json

def import_data(db):
    filename = input("Введите имя файла для импорта: ")
    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data:
            car = car(item['model'], item['year'], item['price'])
            db.add_car(car)
    print("Данные импортированы.")

def export_data(db):
    filename = input("Введите имя файла для экспорта: ")
    data = [{"model": car.model, "year": car.year, "price": car.price} for car in db.get_cars()]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Данные экспортированы.")
