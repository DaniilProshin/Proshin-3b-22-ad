a = [1, 2, 3, 4, 5]
flag = 0
for i in range(len(a)):
    if len(a) > i and a[i] == 3:
        a.pop(flag)
    flag += 1
print(a)
