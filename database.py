class Database:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars

    def delete_car(self, car_id):
        if 0 <= car_id < len(self.cars):
            del self.cars[car_id]

    def get_cars_by_year(self, year):
        return [car for car in self.cars if car.year == year]
