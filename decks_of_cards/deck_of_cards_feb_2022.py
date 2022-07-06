from random import randint

class Card():

    def __init__(self, value, suit):

        self.value = value
        self.suit = suit

        if self.suit == 'hearts' or self.suit == 'diamonds':
            self.color = 'red'
        else:
            self.color = 'black'

        if (value == 1):
            self.rank = 'Ace'
        elif (value == 11):
            self.rank = 'Jack'
        elif (value == 12):
            self.rank = 'Queen'
        elif (value == 13):
            self.rank = 'King' 
        else:
            self.rank = value

    # def color(self):
    #     if self.suit == 'hearts' or self.suit == 'diamonds':
    #         return('red')
    #     else:
    #         return('black')

    def __repr__(self):
        return f"{self.suit[0]}{self.value}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# class to represent a deck of cards

class Deck():
    # represent a standard 52-card deck
    def __init__(self):
        self.contents = []

        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for value in values:
            for suit in suits:
                self.contents.append(Card(value, suit))

        self.shuffle_deck()

    def deal_card(self):
        if len(self.contents) != 0:
            return self.contents.pop()
        else:
            return None

    def shuffle_deck(self):
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            # temp = self.contents[i]
            # self.contents[i] = self.contents[x]
            # self.contents[x] = temp
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]


new_deck = Deck()

player_a = []
player_b = []

print(new_deck.contents)

for i in range(0, 26):
    player_a.append(new_deck.deal_card())
    player_b.append(new_deck.deal_card())

print(player_a)
print(player_b)
