from play.play_round import Round
from utils.player import Player
from utils.table import Table
import random


player_names = ['anil', 'pogo', 'mangal', 'ramya', 'harsha']
players = [Player(name) for name in player_names]
table = Table(players)


r = Round(table)
print(r.table)
r.table.move_player_to_front_by_name('ramya')
print(r.table)
r.table.move_player_to_front_by_name('harsha')
print(r.table)
# r.table.move_dealer()
# print(r.table)
r.table.remove_player("anil")
print(r.table)


print("Trump is : {}".format(r.trump_card))

# cards_played = {'anil': random.choice(players[0].hand.cards),
#                 'pogo': random.choice(players[1].hand.cards),
#                 'mangal': random.choice(players[2].hand.cards),
#                 'ramya': random.choice(players[3].hand.cards),
#                 'harsha': random.choice(players[4].hand.cards)}
#
# r.play_round(cards_played)
# print(r.players)
