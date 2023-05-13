class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def info(self):
        print(f"Name: {self.name};  Breed: {self.breed};  Age: {self.age}")


dog1 = Dog("Tom", "Labrador", 7)
dog1.info()
