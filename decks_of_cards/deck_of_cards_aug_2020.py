from random import randint

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        ranks = {'11': 'Jack', '12': 'Queen', '13': 'King', '1': 'Ace'}
        if str(value) in ranks:
            self.rank = ranks[str(value)]
        else:
            self.rank = str(value)

    def __repr__(self):
        return (f"{self.rank} of {self.suit}s")

    # def rank(self):
    #     ranks = {'11': 'Jack', '12': 'Queen', '13': 'King', '1': 'Ace'}
    #     if str(value) in ranks:
    #         return ranks[str(value)]
    #     else:
    #         return str(value)

class Deck():

    def __init__(self):
        self.contents = []
        self.generate_deck()
        self.shuffle_deck()

    def generate_deck(self):
        suits = ['heart', 'diamond', 'club', 'spade']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for suit in suits:
            for value in values:
                # print(f"position in loops: {suit} and {value}")
                new_card = Card(suit, value)
                self.contents.append(new_card)
        # alternate code:
        # self.contents = [Card(suit, value) for suit in suits for value in values]


    def shuffle_deck(self):
        # there is a built-in function for this: random.shuffle()
        # https://docs.python.org/3/library/random.html#random.shuffle
        # but I wrote this to show you multiple variable assignment :)
        for i in range(0, 52):
            x = randint(0, 51)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_card(self):
        # try/except:
        # try to run every line under try block
        # if any of those lines cause an exception
        # (like popping out of an empty list)
        # then run the code in the except block instead
        try:
            return self.contents.pop(0)
        except:
            print('Deck is empty!')
            return None

    def add_to_bottom(self, card):
        self.contents.append(card)

new_deck = Deck()
player_hand = []
print(new_deck.contents)
player_hand.append(new_deck.deal_card())
player_hand.append(new_deck.deal_card())
player_hand.append(new_deck.deal_card())
print(player_hand)