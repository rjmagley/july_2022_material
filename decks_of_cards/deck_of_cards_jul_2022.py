from random import randint

# OOP create some class(es) represent a standard 52-card deck
# aces through kings, four standard suits (hearts, diamonds, spades, clubs)

class Card():

    def __init__(self, suit, value):

        # data for individual cards
        self.suit = suit
        self.value = value # numeric value

        if value == 1:
            self.rank = 'Ace'
        elif value == 11:
            self.rank = 'Jack'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 13:
            self.rank = 'King'
        else:
            self.rank = str(value) # description/proper name

        # could do this, but harder to read for less skilled programmers
        # rank_conversion = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        # if value in rank_conversion:
        #     self.rank = rank_conversion[value]
        # else:
        #     self.rank = str(value)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"{self.suit[0]}{self.value}"


class Deck():

    def __init__(self):

        # what properties does a deck of cards have?
        
        # contents - a list of cards
        # cards COULD be dictionaries
        self.contents = []

        # I could specify suits and values as parameters to the deck
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        for suit in suits:
            for value in values:
                self.contents.append(Card(suit, value))

        # after creating cards, shuffle deck
        self.shuffle_deck()

    def shuffle_deck(self):
        # we really should do a Fisher-Yates
        # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def draw_card(self):

        if len(deck.contents) != 0:
            return deck.contents.pop()
        else:
            return None

        # if not deck.contents:
        #     return None
        # return deck.contents.pop()




deck = Deck()

player_a = []
player_b = []

for i in range(0, 51):
    player_a.append(deck.draw_card())
    player_b.append(deck.draw_card())

print(player_a)