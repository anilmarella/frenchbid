class Hand:
    def __init__(self):
        self.cards = []

    def is_empty(self):
        return len(self.cards) == 0

    def sort_hand(self, how='asc'):
        mul = -1 if how != 'asc' else 1
        self.cards = sorted(self.cards,
                            key=lambda x: (x.suit, mul*x.get_value()))

    def __str__(self):
        return ", ".join([str(c) for c in self.cards])
