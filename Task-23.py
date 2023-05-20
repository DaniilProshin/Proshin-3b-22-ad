mas = [i for i in range(10)]
flag = int(input('Введите число: '))

print(mas)
print(flag)
if flag in mas:
    print("Число найдено в массиве")
else:
    print("Число не найдено в массиве")