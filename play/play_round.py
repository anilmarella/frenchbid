from utils.deck import Deck
from play.play_set import Set


class Round:
    def __init__(self, table, round_id):
        self.table = table
        self.n_players = self.table.table_size
        self.trump_card = None
        self.deal_cards(round_id)

    def deal_cards(self, round_id):
        dck = Deck()
        dck.shuffle()
        for i, crd in enumerate(dck.deal()):
            idx = i % self.n_players
            self.table.player_dict[idx].add_card_to_hand(crd)
            if (idx == self.n_players - 1 and
                    self.table.player_dict[idx].get_hand_size() == round_id):
                break
        self.trump_card = dck.get_random_card()

    def play_round(self, cards_played):
        s = Set(self.trump_card.suit)
        for plr, card in cards_played.items():
            s.play_card(plr, card)
        winner = s.determine_winner()
        self.table.move_player_to_front_by_name(winner)


