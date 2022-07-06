from random import randint

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value == 11:
            self.rank = 'Jack'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 13:
            self.rank = 'King'
        elif value == 1:
            self.rank = 'Ace'
        else:
            self.rank = str(value)

    def __repr__(self):
        return f"{self.value}{self.suit[0]}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):

        self.suits = ['hearts', 'spades', 'diamonds', 'clubs']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.contents = []

        # for suit in self.suits:
        #     for value in self.values:
        #         self.contents.append(Card(suit, value))

        self.contents = [Card(suit, value) for suit in self.suits for value in self.values]

        self.shuffle_deck()

        
    def shuffle_deck(self):
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_card(self):
        if len(self.contents) == 0:
            return None
        return self.contents.pop()

    def deal_multiple_cards(self, number_of_cards):
        cards = []
        for i in range(0, number_of_cards):
            cards.append(self.deal_card())

        return cards



new_deck = Deck()

player_1 = []
player_2 = []

print(new_deck.contents)
player_1.append(new_deck.deal_card())