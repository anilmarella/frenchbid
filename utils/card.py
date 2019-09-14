

class Card:
    VALID_RANKS = ['A', 'K', 'Q', 'J', '2', '3', '4',
                   '5', '6', '7', '8', '9', '10']
    VALID_SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    VALUES = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank in ('J', 'Q', 'K', 'A'):
            return Card.VALUES[self.rank]
        else:
            return int(self.rank)

    def __str__(self):
        return "{}-{}".format(self.rank, self.suit)

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
