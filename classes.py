class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(f'Monster energy = {self.energy}')

    def get_damage(self, amount):
        self.health -= amount

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')


monster1 = Monster(10, 20)
monster2 = Monster(health=50, energy=100)

print(monster1.health)
print(monster2.health)