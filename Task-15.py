class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def info(self):
        print(f"{self.brand} - {self.model}, {self.year} release, {self.price} dollars")


car1 = Car("BMW", "M5", 2013, 15000)
car1.info()
