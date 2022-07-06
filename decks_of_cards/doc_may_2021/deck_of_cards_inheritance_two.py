from random import randint

class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value # numeric value of the card
        # values of 1, 11, 12 and 13 are special
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
        return f"{self.suit[0]}{self.value}"

    def __str__(self):
        return f"{self.rank} of {self.suit}"
        

class Deck():

    def __init__(self):

        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # values for cards - 1 is ace, 11 is jack, 12 is queen, 13 is king
        self.contents = []
        self.build_deck()
        self.shuffle_deck()

    # splitting this into its own method to make inheritance cleaner
    def build_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.contents.append(Card(suit, value))

    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    # not what we're doing, but interesting
    def shuffle_deck(self):
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_card(self):
        if len(self.contents) == 0:
            print("no cards in deck!")
            return None

        return self.contents.pop()

# five-card draw deck - doesn't have the same range of cards
# (Deck) indicates that we are inheriting from the Deck class
class FiveCardDrawDeck(Deck):

    def __init__(self):

        # super() is a special method that gets the properties and methods of
        # the Deck class - no need to redefine deal_card() for example
        super().__init__()
        self.values = [1, 7, 8, 9, 10, 11, 12, 13]
        self.contents = []
        # now that build_deck() is its own thing, life is a bit easier
        self.build_deck()
        self.shuffle_deck()

# casino-level blackjack is usually played with 2 to 6 decks of cards -
# this prevents card counting, which benefits the casino
class CasinoBlackjackDeck(Deck):
     def __init__(self):

        super().__init__()
        self.contents = []
        # call this six times, get six sets of cards in your deck
        self.build_deck()
        self.build_deck()
        self.build_deck()
        self.build_deck()
        self.build_deck()
        self.build_deck()
        self.shuffle_deck()

new_deck = Deck()
print(new_deck.contents)

new_fivecard_deck = FiveCardDrawDeck()
print(new_fivecard_deck.contents)

new_blackjack_deck = CasinoBlackjackDeck()
print(new_blackjack_deck.contents)
