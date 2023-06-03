n = int(input("Введите количество элементов в списке: "))
list1 = []
for i in range(n):
    a = int(input(f"Введите {i}-ый элемент: "))
    list1.append(a)
print(list1)


min_1 = min_2 = float('inf')
for value in list1:
    if value < min_1:
        min_1, min_2 = value, min_1
    elif value < min_2:
        min_2 = value

print(min_1)
print(min_2)
