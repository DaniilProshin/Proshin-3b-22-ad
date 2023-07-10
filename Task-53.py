class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.works = self.load_from_file()

    def add_work(self, work):
        self.works.append(work)
        with open(self.filename, 'w') as file:
            for work in self.works:
                file.write(work)
                file.write('\n')

    def remove_work(self, work):
        if work in self.works:
            self.works.remove(work)
            with open(self.filename, 'w') as file:
                for work in self.works:
                    file.write(work)
                    file.write('\n')
        else:
            print("Данное дело не найдено в списке дел")

    def print_list(self):
        print("Список домашних дел:")
        for item in self.works:
            print(item)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read().splitlines()
        except FileNotFoundError:
            return []

todo_list = TodoList("todo.txt")
todo_list.print_list()

todo_list.add_work("Погулять с собакой")
todo_list.add_work("Сделать ДЗ")
todo_list.add_work("Убраться в доме")
todo_list.print_list()

todo_list.remove_work("Помыть посуду")
todo_list.remove_work("Убраться в доме")
todo_list.print_list()
