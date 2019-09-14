from utils.player import Player
from utils.table import Table
from play.play_round import Round

class GameService:

    def __init__(self):
        self.players = []
        self.table = None
        self.curr_round = None

    def add_player(self, p_name):
        self.players.append(Player(p_name))

    def initialize_table(self):
        self.table = Table(self.players)

    def get_player_hand(self, p_name):
        plr = next(p for p in self.players if p == p_name)
        return plr.hand

    def initialize_round(self, round_num):
        self.curr_round = Round(self.table, round_num)

    def

