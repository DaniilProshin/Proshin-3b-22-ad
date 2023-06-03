try:
    file = open('test.txt', 'r')
    print("Файл существует")
    file.close()

except FileNotFoundError as e:
    print(f"Файл не найден: {e.filename}")
