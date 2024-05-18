class Hand:
    cards = []
    total = 0
    soft = False
    bust = False
    split = False
    stake = 0
   
    def __init__(self, stake: int):
        self.cards = []
        self.stake = stake


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
    
    def add_stake(self, stake: int):
        self.stake = stake

    def show_cards(self) -> list[str]:
        return [card['rank'] for card in self.cards] 
    
    def get_total(self) -> tuple:
        return self.total, self.soft

    def show_options(self) -> list[str] | None:
        options = []
        if self.bust:
            return None
        options.append("s")
        options.append("h")
        if len(cards) == 2:
            options.append("d")

    def get_cards(self) -> list[tuple]:
        return self.cards
