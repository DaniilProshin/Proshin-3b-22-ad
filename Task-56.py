try:
    file_name = input("Введите названия файла: ")
    with open(file_name, 'r') as file:
        text = file.read()

    lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']
    lst = []
    for word in text.lower().split():
        if not word in lst_no:
            _word = word
            if word[-1] in lst_no:
                _word = _word[:-1]
            if word[0] in lst_no:
                _word = _word[1:]
            lst.append(_word)
    dict_1 = dict()
    for word in lst:
        if word in dict_1.keys():
            dict_1[word] += 1
        else:
            dict_1[word] = 1
    sort_list = []
    for key, items in dict_1.items():
        sort_list.append((items, key))
    sort_list.sort(reverse=True)
    print(sort_list)
except FileNotFoundError:
    print("Файл не найден")

