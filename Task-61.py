def distance(arr):
    x = arr[0]
    y = arr[1]
    return (x**2 + y**2)**0.5


array = [(1, 2), (3, 4), (-1, 5), (6, -3)]

for i in range(len(array)-1):
    for j in range(0, len(array)-1-i):
        if distance(array[j]) > distance(array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]

print(array)
