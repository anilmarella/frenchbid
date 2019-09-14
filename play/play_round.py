from utils.deck import Deck
from utils.player import Player
from play.play_round import Round


class Game:
    def __init__(self, n_players=5):
        self.n_players = n_players
        self.players = [Player(idx) for idx in range(n_players)]
        self.trump_card = None
        self.round = None

    def deal_cards(self, round_id=10):
        dck = Deck()
        dck.shuffle()
        for i, crd in enumerate(dck.deal()):
            idx = i % self.n_players
            if (idx == self.n_players - 1 and
                    self.players[idx].get_hand_size() == round_id):
                break
            self.players[idx].add_card_to_hand(crd)
        self.trump_card = dck.get_random_card()
        self.round = Round(self.trump_card.suit)

    def 

