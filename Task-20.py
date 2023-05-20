import random

mas = []
for i in range(10):
    mas.append(int(random.random()*100))
print(mas)
flag_min, flag_max = 101, 0

for i in range(10):
    if mas[i] > flag_max:
        flag_max = mas[i]
    if flag_min > mas[i]:
        flag_min = mas[i]

print(flag_max)
print(flag_min)
print(max(mas))
print(min(mas))
