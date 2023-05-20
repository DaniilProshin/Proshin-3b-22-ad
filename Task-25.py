num = int(input("Введите число: "))
a = 2
flag = 0
while num > a:
    if num % a == 0:
        flag += 1
        break
    a += 1
if flag:
    print("Число не простое")
else:
    print("Число простое")
