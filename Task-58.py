def sort_array(arr):

    arr.sort()
    return(tuple(arr))


array = [5, 1, 10, 3, 7]


array = sort_array(array)
print(type(array), array)
