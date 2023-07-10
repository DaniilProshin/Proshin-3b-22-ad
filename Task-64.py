class Bank:
    def __init__(self):
        self.clients = {}
        self.id = '001'
        self.transactions = []

    def add_client(self, name):
        if name not in self.clients:
            self.clients[name] = {"id": self.id, 'accounts': {}}
            self.id = "{:03d}".format(int(self.id) + 1)
        else:
            print("Ошибка: Клиент c таким именем уже существует")

    def open_account(self, name, balance=0):
        if name in self.clients:
            self.clients[name]['accounts'][self.clients[name]['id']+'-'
                                           +"{:03d}".format(len(self.clients[name]['accounts'].keys()) + 1)] = balance
        else:
            print("Ошибка: Клиент не найден. Добавьте клиента в базу")

    def transaction(self, name, acc, name_to, acc_to, dep):
        if name in self.clients:
            if name_to in self.clients:
                if acc in self.clients[name]['accounts'].keys():
                    if acc_to in self.clients[name_to]['accounts'].keys():
                        if dep <= self.clients[name]['accounts'][acc]:
                            self.clients[name]['accounts'][acc] -= dep
                            self.clients[name_to]['accounts'][acc_to] += dep
                            self.transactions.append((acc, acc_to, dep))
                        else:
                            print(f"Ошибка: У клиента {name} недостаточно средств на счету {acc}")
                            print(f"Запрашиваемая сумма = {dep}, Средств на счету = {self.clients[name]['accounts'][acc]}")
                    else:
                        print(f"Ошибка: счет {acc_to} Клиента {name_to} не найден ")
                else:
                    print(f"Ошибка: счет {acc} Клиента {name} не найден ")
            else:
                print(f"Ошибка: Клиент {name_to} кому совершается перевод не найден")
        else:
            print(f"Ошибка: Клиент {name} не найден")


sber = Bank()
sber.add_client('Иванов')
sber.open_account('Иванов', 500)
sber.open_account('Иванов', 500)
sber.add_client("Петров")
sber.open_account('Петров', 500)
sber.transaction('Петров', '002-001', 'Иванов', '001-002' , 500)
print(sber.clients)
print(sber.transactions)
