class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self. balance = balance

    def refill(self, amount):
        self.balance += amount
        print(self.balance)

    def takeoff(self, amount):
        if self.balance - amount < 0:
            print("Not enough money")
        else:
            self.balance -= amount
            print(self.balance)


account1 = BankAccount('Tom', '55555', 3500)
account1.refill(500)
account1.takeoff(4500)
account1.takeoff(3000)

