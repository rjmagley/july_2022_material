class Card():

    def __init__(self, value, suit):
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

    def __repr__(self):
        return f"{self.suit[0]}{self.value}"

    def __str__(self):
        return f"{self.rank} of {self.suit}s"

class Deck():

    def __init__(self):
        self.contents = []
        
        suits = ['heart', 'club', 'spade', 'diamond']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for suit in suits: # for x in y
            for value in values:
                self.contents.append(Card(value, suit))
        # list comprehension

    def deal_card(self):
        if len(self.contents) > 0:
            return self.contents.pop(0)

    # shuffle the deck?

new_deck = Deck()

player_a = []
player_b = []

x = 520

for i in range(0, x):
    card_a = new_deck.deal_card()
    if card_a != None:
        player_a.append(card_a)
    card_b = new_deck.deal_card()
    if card_b != None:
        player_b.append(card_b)

print(player_a)
print(player_b)

print(len(new_deck.contents))

        