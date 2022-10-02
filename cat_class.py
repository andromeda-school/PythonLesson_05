class Fish:

    def __init__(self, name, amount):
        self.name = name
        print("Создана рыба ", name)
        self.amount = amount

    def info(self):
        print(f"{self.name} лежит, пищевая ценность: {self.amount}")


class Cat:

    def __init__(self, name, h, l):
        self.name = name
        self.health = h
        self.live = l
        print("Создана новая кошка с именем ", self.name)

    def eating(self, eat_fish):
        print(f"{self.name} кушает")
        self.health += eat_fish.amount
        if (self.health > 35):
            print(f"{self.name} наелся. Количество жизней увеличилось.")
            self.live += 1
            self.health = 20
        if (self.health < 0):
            print("Отравился или голод")
            self.live -= 1
        print(f"Здоровье стало ({self.health})")

    def info(self):
        print(f"Здоровье: {self.health}")
        print(f"Жизней: {self.live}")


persik = Cat('Персик', 20, 6)
fish_1 = Fish("Треска", 10)
fish_2 = Fish("Форель", 130)
fish_3 = Fish("Тухлый Карась", -15)

persik.info()
persik.eating(fish_1)
persik.info()
persik.eating(fish_2)
persik.info()
persik.eating(fish_3)
persik.info()
persik.eating(fish_3)
persik.info()
persik.eating(fish_3)
persik.info()
persik.eating(fish_3)
persik.info()


