import names


class Player():

    def __init__(self, sym):
        self.name = names.get_first_name()
        self.symbol = sym
        self.score = 0

    def change_name(self, player_name):
        self.name = player_name

    def win(self):
        self.score += 1


