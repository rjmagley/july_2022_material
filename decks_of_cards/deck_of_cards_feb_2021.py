import random

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
        return f"{self.rank[0]}{self.suit[0]}"

    def __str__(self):
        return f"{self.rank} of {self.suit}s"


class Deck():

    def __init__(self, number_of_decks = 2):
        self.suits = ['diamond', 'heart', 'spade', 'club']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.contents = []

        for i in range(0, number_of_decks):
            for suit in self.suits:
                for value in self.values:
                    self.contents.append(Card(suit, value))

        self.shuffle()

    def pick_a_card(self):
        x = random.randint(0, len(self.contents) - 1)
        print(self.contents[x])

    def shuffle(self):
        for i in range(0, len(self.contents)):
            x = random.randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i] 

    def deal_card(self, target_player, number_of_cards = 1):
        to_deal = []
        for i in range(0, number_of_cards):
            target_player.add_card(self.contents.pop())

class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def __str__(self):
        return f"{self.name}'s hand: {self.hand}"

deck = Deck(1)

player_a = Player('Bob')
player_b = Player('Alice')
player_c = Player('Jort')

players = [player_a, player_b, player_c]

for player in players:
    deck.deal_card(player, 2)
    print(player)




        
