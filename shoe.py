import random

class Shoe:
    cards = []
    number_of_cards = 0
    cards_left = 0
    running_count = 0
    true_count = 0
    num_decks = 0
    dead = False


    def __init__(self, num_decks = 4):
        self.num_decks = num_decks
        self.cards = self.create_deck()
        self.number_of_cards = len(self.cards)
        self.cards_left = len(self.cards)

    def create_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit, 'image': f"{rank}o{suit[0]}.png"} for suit in suits for rank in ranks]
        cards = deck * self.num_decks
        random.shuffle(cards)
        cut_card = {'rank': 'cut', 'suit': 'cut'}
        randomindex = random.randint(35*self.num_decks, 45*self.num_decks)
        cards.insert(randomindex, cut_card)

        return cards
#draw card and update counts
    def draw_card(self):
        if len(self.cards) == 0:
            raise ValueError("No cards left in the shoe.")
        drawn_card = self.cards.pop()
        if drawn_card['rank'] == 'cut':
            self.dead = True
            drawn_card = self.cards.pop()
        if drawn_card['rank'] in ['2', '3', '4', '5', '6']:
            self.running_count += 1
        elif drawn_card['rank'] in ['10', 'J', 'Q', 'K', 'A']:
            self.running_count -= 1
        self.cards_left -= 1
        self.true_count = int(self.running_count / round(self.cards_left / 52))

        return drawn_card

