import random
import time


class Computer:

    def __init__(self, name, processor, memory, cost):
        self.name = name
        self.processor = processor
        self.memory = memory
        self.cost = cost
        print("-----------------------------------")
        print(f"Новый компьютер '{name}'.")
        print(f"Процессор : {processor}")
        print(f"Память : {memory} gb")
        print(f"Цена : {cost}р")
        print("-----------------------------------")

    def change_memory(self, new_memory):
        self.memory = new_memory
        print(f"Заменена память {self.name}.")
        print(f"Новая память : {self.memory} gb")

    def install(self):
        print(f"Установка системы '{self.name}'")
        proc = 0
        while proc < 100:
            print(f"Установка системы '{self.name}' ({proc}%)")
            proc = proc + random.randrange(10)
            time.sleep(0.2)
        print("Установка завершена!")


computer1 = Computer("DEXP Aquilon O271", "Intel Core i5-11400F", 512, 103800)
computer2 = Computer("HP ProDesk 400 G6 DM", "Intel Core i3-5454", 256, 45900)
computer3 = Computer("ZET Gaming NEO M026 ", "Intel Core i9-13500F", 1024, 123900)
computer4 = Computer("ПК Lenovo Legion T5 26IOB6", "AMD A4-4050R", 512, 70500)

computer3.install()
