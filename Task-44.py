try:
    with open('test.txt', 'r') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print('Файл не найден')