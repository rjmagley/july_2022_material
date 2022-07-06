from random import randint

class Card():
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        if value == 1:
            self.rank = 'Ace'
        elif value == 11:
            self.rank = 'Jack'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 13:
            self.rank = 'King'
        else:
            self.rank = str(value)

    def __repr__(self):
        return(f'{self.suit[0]}{self.value}')

    def __str__(self):
        return(f'{self.rank} of {self.suit}s')

class Deck():
    def __init__(self):
        self.contents = []
        self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        suits = ['heart', 'diamond', 'club', 'spade']
        for value in values:
            for suit in suits:
                self.contents.append(Card(value, suit))
        # self.contents = [Card(suit, value) for suit in suits for value in values]

    def shuffle_deck(self):
        # new_deck = []
        # for i in range(0, len(self.contents)):
        #     x = randint(0, len(self.contents) - 1)
        #     card = self.contents.pop(x)
        #     new_deck.append(card)
        # self.contents = new_deck
        for i in range(0, 52):
            x = randint(0, 51)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]


    

x = Deck()
print(x.contents)
print(x.contents[0])
print(x.contents[0].rank)
number_input = int(input('Your number [1 - 52 please]: ')) - 1
print(f'Your card is: {x.contents[number_input]}')