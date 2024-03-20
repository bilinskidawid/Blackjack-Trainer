class Hand:
    bust = False
    cards = []
    total = 0
    soft = False

    def add_card(self, card: tuple) -> None:
        self.cards.append(card)
        if card['rank'] in ['J', 'Q', 'K']:
            self.total += 10
        elif card['rank'] == 'A':
            if self.total + 11 > 21:
                self.total += 1
                self.soft = False
            else:
                self.soft = True
                self.total += 11
        else:
            self.total += int(card['rank'])
        if self.total > 21 and self.soft:
            self.total -= 10
            self.soft = False
        elif self.total > 21:
            self.bust = True
    def show_cards(self) -> list[tuple]:
        return self.cards
        
