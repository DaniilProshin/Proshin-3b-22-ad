class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def info(self):
        print(f"Сотрудник {self.name}, {self.age} лет, зарплата - {self.salary} рублей")


employee1 = Employee("Vladimir", 25, 25000)
employee1.info()
