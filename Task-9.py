class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        print(self.length * self.width)


rectangle1 = Rectangle(5, 6)
print(rectangle1.length, rectangle1.width)
rectangle1.square()




