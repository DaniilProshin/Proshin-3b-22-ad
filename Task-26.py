a = int(input("Введите число: "))
b = int(input("Введите число: "))

flag = 2
mas = []

while flag <= a:
    if a % flag == 0:
        mas.append(flag)
    flag += 1

flag = 2

while flag <= b:
    if b % flag == 0:
        if flag in mas:
            break
    flag += 1
print(f"наименьший общий множитель : {flag}")