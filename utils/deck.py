from itertools import product
from card import Card
from random import shuffle, choice


class Deck:
    def __init__(self):
        self.deck = []
        for c in product(Card.VALID_RANKS, Card.VALID_SUITS):
            self.deck.append(Card(c[0], c[1]))
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)

    def __str__(self):
        return ", ".join([str(c) for c in self.deck])

    def size(self):
        return len(self.deck)

    def deal(self):
        while self.size() != 0:
            yield self.deck.pop()

    def get_random_card(self):
        crd = choice(self.deck)
        self.deck.remove(crd)
        return crd
