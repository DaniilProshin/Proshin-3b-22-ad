class CardProduct:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def decrease_quantity(self, amount):
        if amount > 0:
            if self.quantity >= amount:
                self.quantity -= amount
                print(f"Количество товара: {self.quantity}")
            else:
                print(f"Товара меньше {amount}")
                print(f"Количество товара: {self.quantity}")
        else:
            print("Количество уменьшаемого товара должно быть положительным")

    def change_price(self, amount):
        if self.price >= -amount:
            self.price += amount
            print(f"Стоимость товара: {self.price}")
        else:
            print("Стоимость товара не может быть отрицательной")
            print(f"Стоимость товара: {self.price}")


product1 = CardProduct("Iphone", 1000, 25)
product1.decrease_quantity(15)
product1.change_price(2000)
