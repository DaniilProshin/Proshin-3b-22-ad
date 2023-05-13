class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def info(self):
        print(f"Кошка по имени {self.name}, {self.age} лет, цвет {self.color}")


cat1 = Cat("Barsik", 5, "White")
cat1.info()
