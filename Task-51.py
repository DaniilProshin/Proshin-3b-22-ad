from math import gcd

array1 = [24, 36, 48, 60]
array2 = [12, 18, 24, 36]

result = array1[0]

for num in array1[1:]:
    result = gcd(result, num)

for num in array2:
    result = gcd(result, num)

print("Наибольший общий делитель:", result)
