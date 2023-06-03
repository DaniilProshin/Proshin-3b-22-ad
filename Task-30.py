mas_a = set('aeiouy')
mas_b = set('bcdfghjklmnpqrstvwxz')
str1 = input('Введите строку на английском: ')
flag1 = 0
flag2 = 0
for i in range(len(str1)):
    if str1[i] in mas_a:
        flag1 += 1
    if str1[i] in mas_b:
        flag2 += 1
print(f"В вашей строке {flag1} гласных и {flag2} согласных")
