
class Card:

    def __init__(self, value, index_suit):
        self.cost = value
        self.value = [
            'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'][value-1]
        self.suit = '♥♦♣♠'[index_suit]

    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘')


    def price(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost


cards = []

for i in range(1, 14):
    for j in range(4):
        new_card = Card(i, j)
        new_card.cost = new_card.price()
        cards.append(new_card)
        new_card.show()

