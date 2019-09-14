from utils.player import Player
from utils.deck import Deck

p = Player(name='anil')
d = Deck()

for i in range(5):
    p.add_card_to_hand(d.get_random_card())

print(p.hand)
p.remove_card(p.hand.cards[3])
print(p.hand)
p.add_card_to_hand(d.get_random_card())
print(p.hand)