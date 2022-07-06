from random import randint


class Card:
    def __init__(self, suit, value, rank):
        self.suit = suit
        self.value = value
        self.rank = rank

    def __repr__(self):
        return(f'{self.rank} of {self.suit}s')


class Deck:
    def __init__(self):
        self.contents = []
        self.construct_deck()
        self.shuffle_deck()

    def construct_deck(self):

        suits = ['heart', 'diamond', 'club', 'spade']
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        for suit in suits:
            for value in values:
                if value == 1:
                    new_card = Card(suit, value, 'Ace')
                elif value == 11:
                    new_card = Card(suit, value, 'Jack')
                elif value == 12:
                    new_card = Card(suit, value, 'Queen')
                elif value == 13:
                    new_card = Card(suit, value, 'King')
                else:
                    new_card = Card(suit, value, str(value))
                self.contents.append(new_card)

    def shuffle_deck(self):
        for i in range(0, len(self.contents)):
            x = randint(0, len(self.contents) - 1)
            self.contents[i], self.contents[x] = self.contents[x], self.contents[i]

    def deal_top_card(self):
        try:
            return self.contents.pop(0)
        except:
            print('Deck is empty!')
            return None

    def add_to_bottom(self, card):
        self.contents.append(card)

    def add_to_top(self, card):
        self.contents.insert(0, card)


new_deck = Deck()
player_hand = []
print(new_deck.contents)
player_hand.append(new_deck.deal_top_card())
player_hand.append(new_deck.deal_top_card())
player_hand.append(new_deck.deal_top_card())
print(player_hand)
