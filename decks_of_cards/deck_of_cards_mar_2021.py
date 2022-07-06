# 52 card deck
# used for games like... poker
# everyone involved is a human

import random

class Card():
    # card values: 1 through 13
    # card rank: ace, two, three, etc... queen, king.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value == 1:
            self.rank = "Ace"
        elif value == 11:
            self.rank = "Jack"
        elif value == 12:
            self.rank = "Queen"
        elif value == 13:
            self.rank = "King"
        else:
            self.rank = str(value)

    def __repr__(self):
        return f"{self.suit[0]}{self.value}"

    def __str__(self):
        return f"{self.rank} of {self.suit}s"
        

class Deck():

    def __init__(self):
        self.contents = []
        #cards consist of suit and value
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for value in self.values:
            for suit in self.suits:
                card = Card(suit, value)
                self.contents.append(card)
        self.shuffle()

    def shuffle(self):
        # random.shuffle(self.contents)
        # maybe someday do Fischer-Yates?
        for i in range(0, len(self.contents)):
            x = random.randint(0, 51)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal(self):
        return self.contents.pop(0)
    
    def burn(self):
        self.contents.pop(0)


        

deck = Deck()
# print(len(x.contents)) # should be 52
# print(x.contents)
# print(x.contents[0])

player1 = []
player2 = []
player3 = []

players = [player1, player2, player3]
for player in players:
    player.append(deck.deal())
for player in players:
    player.append(deck.deal())
    print(player)

deck.burn()

community = []
community.append(deck.deal())
community.append(deck.deal())
community.append(deck.deal())