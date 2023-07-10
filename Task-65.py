class GameCharacter:
    def __init__(self, name, lvl, health, damage, defence):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.damage = damage
        self.defence = defence

    def lvl_up(self):
        print(f"Уровень {self.name} увеличен 1")
        print(f"Был lvl: {self.lvl}; Стал lvl: {self.lvl + 1}")
        print(f"Было HP: {self.health}; Стало HP: {1.1 * self.health}")
        print(f"Был damage: {self.damage}; Стал damage: {1.1 * self.damage}")
        self.lvl += 1
        self.health *= 1.1
        self.damage *= 1.1

    def get_damage(self, amount):
        self.health -= max(0, amount - self.defence)


def battle(character1, character2):
    print(f"{character1.name} VS {character2.name}")
    flag = 1
    while flag < 4:
        print(f"{flag} Раунд")
        character1.get_damage(character2.damage)
        print(f"{character1.name} получает урон {character2.damage} от "
              f"{character2.name} (Заблокировано {character1.defence})")
        print(f"{character1.name} HP осталось: {character1.health}")
        character2.get_damage(character1.damage)
        print(f"{character2.name} получает урон {character1.damage} от "
              f"{character1.name} (Заблокировано {character2.defence})")
        print(f"{character2.name} HP осталось: {character2.health}")
        if flag < 3:
            flag = result_round(character1, character2, flag)
        flag += 1
        if flag < 4:
            character1.lvl_up()
            character2.lvl_up()
    result_battle(character1, character2)


def result_round(character1, character2, flag):
    if character1.health <= 0:
        return 4
    elif character2.health <= 0:
        return 4
    elif character1.health == character2.health:
        print(f"В {flag} раунде ничья")
        return flag
    elif character1.health > character2.health:
        print(f"В {flag} раунде победил {character1.name}")
        return flag
    else:
        print(f"В {flag} раунде победил {character2.name}")
        return flag


def result_battle(character1, character2):
    if character1.health == character2.health:
        print(f"В Битве {character1.name} VS {character2.name} НИЧЬЯ")
    elif character1.health > character2.health:
        print(f"В Битве {character1.name} VS {character2.name} Победил {character1.name}")
    else:
        print(f"В Битве {character1.name} VS {character2.name} Победил {character2.name}")


zeus = GameCharacter("Zeus", 2, 150, 20, 5)
mars = GameCharacter("Mars", 3, 120, 15, 3)
battle(zeus, mars)
