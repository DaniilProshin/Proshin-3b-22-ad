str1 = input("Введите строку: ")
str1 = str1.lower()
d = {}
for i in range(len(str1)):
    if str1[i] == " ":
        continue
    if str1[i] in d.keys():
        d[str1[i]] += 1
    else:
        d[str1[i]] = 1

print(d)
