class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}  Age: {self.age}")


bob = Person("Bob", 37)
bob.info()
