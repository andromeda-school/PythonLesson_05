import time


class Monster:

    def __init__(self, name, h, p):
        print("Создан новый монстр с именем", name)
        self.name = name
        self.health = h
        self.power = p

    def attack(self):
        print("Монстр атаковал с силой", self.power)

    def get_damage(self, amount):
        self.health -= amount
        print(f"Монстр получил урон ({amount})")
        print("Оставшееся здоровье", self.health)


class Hero:

    def __init__(self, name, h, p):
        print("Создан новый герой с именем", name)
        self.name = name
        self.health = h
        self.power = p

    def attack(self):
        print("Герой атаковал с силой", self.power)

    def get_damage(self, amount):
        self.health -= (amount/4)
        print(f"Герой отразил удар (урон {amount/4})")
        print("Оставшееся здоровье", self.health)



dracula = Monster(name='Дракула', h=2000, p=200)
knight = Hero(name='Артур', h=100, p=150)

print(f'Дракула: {dracula.health}, {dracula.power}')
print(f'Герой: {knight.health}, {knight.power}')

time.sleep(3)

while knight.health > 0 and dracula.health > 0:
    # Ход героя
    knight.attack()
    dracula.get_damage(knight.power)
    # Ход монстра
    dracula.attack()
    knight.get_damage(dracula.power)
    print("-------------------------------")
    time.sleep(1)