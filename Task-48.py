a = [5, 7, 11, 13, 15, 20, 25]
flag1 = 0
flag2 = 0
for i in range(len(a)):
    if a[i] > 10:
        flag1 += a[i]
        flag2 += 1
print(flag1 / flag2)