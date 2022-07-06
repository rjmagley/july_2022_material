from random import randint

# could represent a card as a dictionary: {'suit': 'diamonds', 'rank': 'Ace'}
# but I think a Card class is better

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if value == 13:
            self.rank = 'King'
        elif value == 12:
            self.rank = 'Queen'
        elif value == 11:
            self.rank = 'Jack'
        elif value == 1:
            self.rank = 'Ace'
        else:
            self.rank = str(value)

    def get_color(self):
        if self.suit == 'diamond' or self.suit == 'heart':
            return 'red'
        else:
            return 'black'

    def __repr__(self):
        return f'{self.rank[0]}{self.suit[0]}'

    def __str__(self):
        return f'{self.rank} of {self.suit}s'


# Deck class
# representing a standard 52 card deck
# generic, representing any deck you could use for any standard card game
class Deck():

    def __init__(self):
        self.contents = []
        self.suits = ('diamond', 'heart', 'club', 'spade')
        self.values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
        for suit in self.suits:
            for value in self.values:
                self.contents.append(Card(suit, value))
        self.shuffle_deck()

    def shuffle_deck(self):
        # todo: implement proper Fischer-Yates shuffle
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_from_top(self):
        if len(self.contents) == 0:
            return None
        else:
            return self.contents.pop(0)

    def __repr__(self):
        return f'Deck with {len(self.contents)} cards'


new_deck = Deck()

# player_1 = []
# player_2 = []

# while len(new_deck.contents) != 0:
#     player_1.append(new_deck.deal_from_top())
#     player_2.append(new_deck.deal_from_top())

# print(player_1)
# print(player_2)

selected_card_index = input('Pick a card (1 to 52): ')
selected_card = new_deck.contents[int(selected_card_index) - 1]
print(f'Your card is: {selected_card}')