from random import randint

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        if self.value == 1:
            self.rank = 'Ace'
        elif self.value == 11:
            self.rank = 'Jack'
        elif self.value == 12:
            self.rank = 'Queen'
        elif self.value == 13:
            self.rank = 'King'
        else:
            self.rank = str(self.value)
 
    # this could go in the init method too
    # leaving it seperate to demonstrate property decorator
    @property
    def color(self):
        # good time to use enums - enumerated values
        if self.suit == 'heart' or self.suit == 'diamond':
            return 'red'
        else:
            return 'black'

    def __str__(self):

        return f"{self.rank} of {self.suit}s"

    def __repr__(self):
        return f"{self.suit[0:2]}{self.value}"

class Deck():

    def __init__(self, suits = ['heart', 'diamond', 'club', 'spade'], values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]):
        # a deck is made up of individual cards
        # cards have suits and values
        
        self.suits = suits
        self.values = values
        self.contents = []

        for suit in suits:
            for value in values:
                # we could do this:
                # x = Card(suit, value)
                # self.contents.append(x)
                # but this is better:
                self.contents.append(Card(suit, value))
        self.shuffle_deck()

    def shuffle_deck(self):
        # we should do a Fisher-Yates
        # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        # but we'll be lazy for now
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]





new_deck = Deck()
print(f"The top card is: {new_deck.contents[0]}")
print(f"The top card's color is: {new_deck.contents[0].color}")
print(new_deck.contents)
