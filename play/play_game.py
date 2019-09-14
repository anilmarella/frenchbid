from utils.player import Player
from utils.table import Table
from play.play_round import Round


class Game:

    def __init__(self, n_players):
        self.n_players = n_players
        self.player_names = []
        self.table = None

    def set_table(self, names):
        self.player_names = names
        self.table = Table([Player(n) for n in self.player_names])

    def remove_player(self, name):
        self.table.remove_player(name)

    def play_round_n(self, round_num=5):
        r = Round(self.table, round_num)
        



