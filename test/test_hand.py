from utils.hand import Hand
from utils.deck import Deck

d = Deck()
print(str(d))
print(d.size())
print("")

h = Hand()

for c in d.deal():
    h.cards.append(c)
    if len(h.cards) == 10:
        break

print(str(h))
print("")
h.sort_hand(how='asc')
print(str(h))
print("")
h.sort_hand(how='desc')
print(str(h))
print("")
