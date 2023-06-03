num = int(input("Введите число для вывода заданного количества чисел ряда Фибоначчи: "))
a = 0
b = 1
while num:
    print(a, end=" ")
    a, b = b, a + b
    num -= 1

