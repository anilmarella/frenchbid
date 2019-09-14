class Round:
    def __init__(self, trump_suit):
        self.trump = trump_suit
        self.cards_on_table = {}
        self.open_suit = None

    def play_card(self, player_id, card):
        if len(self.cards_on_table) == 0:
            self.open_suit = card[1]
        self.cards_on_table[player_id] = card

    def determine_winner(self):
        max_rank = -1
        winner = None
        trump_on_table = False
        for pid, card in self.cards_on_table:
            if card.suit == self.open_suit and not trump_on_table:
                if card.get_value() > max_rank:
                    winner = pid
                max_rank = max(card.get_value(), max_rank)
            elif card.suit == self.trump:
                max_rank = -1 if not trump_on_table else max_rank
                trump_on_table = True
                if card.get_value() > max_rank:
                    winner = pid
                max_rank = max(card.get_value(), max_rank)
            else:
                continue
        return winner
