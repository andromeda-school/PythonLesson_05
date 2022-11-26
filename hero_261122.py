
class Hero:

    def __init__(self, name, power, attack):
        self.name = name
        self.power = power
        self.attack = attack    # 10 - 100
        print("------------------------------")
        print(f"Создан новый герой '{name}'")
        print(f"Способность: {power}")
        print(f"Сила атаки: [{attack}/100]")
        print("------------------------------")


sonic = Hero("Соник", "Сверхскорость", 35)
hulk = Hero("Халк", "Сверхсила", 90)
batman = Hero("Бэтмен", "Технологии и Ум", 70)