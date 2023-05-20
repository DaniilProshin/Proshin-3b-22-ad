import random

mas = []
for i in range(10):
    mas.append(random.randint(1, 10))

flag = 0

for i in range(10):
    flag += mas[i]

print(mas)
print(flag)
print(sum(mas))


