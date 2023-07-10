def palindrom(a):
    a_size = len(a) // 2
    for i in range(a_size):
        if a[i] != a[-1-i]:
            return False
    return True

a = [1, 2, 3, 2, 1]
if palindrom(a):
    print('Является палиндромом')
else:
    print('Не является палиндромом')