try:
    numbers = input("Введите список целых чисел, разделенных запятыми: ")
    numbers_list = [int(num) for num in numbers.split(',')]
    min_numbers = min(numbers_list)
    print(f' Минимальное число в списке: {min_numbers}')
except ValueError:
    print('Введены не целые числа')
