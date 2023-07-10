def sum_numbers(N):
        total_sum = sum(range(1, N + 1))
        print(f"Сумма чисел от 1 до {N} : {total_sum}")


try:
    N = int(input("Введите целое число N: "))
    sum_numbers(N)
except ValueError:
    print("Введено не целое число")

