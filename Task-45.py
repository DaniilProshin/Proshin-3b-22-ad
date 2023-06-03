name = str(input('Введите имя файла: '))
try:
    with open(name, 'r') as file:
        print(file.read())
except Exception:
    print("Ошибка")
