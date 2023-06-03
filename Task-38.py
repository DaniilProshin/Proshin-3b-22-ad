try:
    with open('text.txt', 'r') as file:
        text = file.read()
    print(text)
except FileNotFoundError as e:
    print(f"Файл не найден: {e.filename}")
