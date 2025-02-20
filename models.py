class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.model} ({self.year}) - ${self.price}"
