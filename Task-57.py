import os

def search1(Dir, fileExt):
    flag = 0
    fileDir = os.listdir(Dir)
    for i in fileDir:
        if i.endswith(fileExt):
            flag += 1
        if os.path.isdir(f"{Dir}\{i}"):
            flag += search1(f"{Dir}\{i}", fileExt)
    return flag


flag = 0
Dir = input("Введите путь к директории: ")
try:
    fileDir = os.listdir(Dir)
    fileExt = input("Введите расширение: ")
    files = search1(Dir, fileExt)
    print(f"Список файлов с заданным расширением {fileExt}: {files}")

except FileNotFoundError:
    print("Директория не найдена")

except NotADirectoryError:
    print("Директория не найдена")