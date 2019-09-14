from utils.hand import Hand


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def __str__(self):
        return str(self.name) + ": " + str(self.hand)

    def add_card_to_hand(self, card):
        self.hand.cards.append(card)

    def get_hand_size(self):
        return len(self.hand.cards)

    def remove_card(self, crd):
        self.hand.cards.remove(crd)

    def __eq__(self, p_name):
        if isinstance(p_name, str):
            return self.name == p_name
        return False
