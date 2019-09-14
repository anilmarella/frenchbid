from utils.player import Player


class Table:

    def __init__(self, players):
        self.player_dict = dict(zip(range(len(players)), players))
        self.table_size = len(self.player_dict)
        self.dealer = players[-1].name

    def get_player_position(self, p_name):
        for pos, plr in self.player_dict.items():
            if plr == p_name:
                return pos
        return -1

    def move_player_to_front_by_name(self, p_name):
        curr_position = self.get_player_position(p_name)
        if curr_position == 0:
            pass
        ks = range(self.table_size)
        re_idx = ks[curr_position:] + ks[:curr_position]
        self.player_dict = {k: self.player_dict[re_idx[k]] for k in ks}

    def get_next_player(self, p_name):
        given_player_pos = self.get_player_position(p_name)
        next_player_pos = (0 if given_player_pos == self.table_size - 1
                           else given_player_pos + 1)
        return self.player_dict[next_player_pos].name

    def get_prev_player(self, p_name):
        given_player_pos = self.get_player_position(p_name)
        next_player_pos = (self.table_size - 1 if given_player_pos == 0
                           else given_player_pos - 1)
        return self.player_dict[next_player_pos].name

    def move_dealer(self):
        self.dealer = self.get_next_player(self.dealer)
        self.move_player_to_front_by_name(self.get_next_player(self.dealer))

    def remove_player(self, p_name):
        if self.dealer == p_name:
            self.dealer = self.get_prev_player(p_name)
        tmpflg = False
        for pos, plr in self.player_dict.items():
            if plr == p_name:
                tmpflg = True
                continue
            pos2 = pos - 1 if tmpflg else pos
            self.player_dict[pos2] = plr
        del self.player_dict[self.table_size - 1]

    def __str__(self):
        temp_lst = ["Pos: {}, Name: {}, Hand: {}".format(k, plr.name, plr.hand)
                    for k, plr in self.player_dict.items()]
        return ("\n".join(temp_lst) + "\n" +
                "Dealer: {}".format(self.dealer))
