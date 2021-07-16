import numpy as np


class GameBoard():

    def __init__(self):
        self.two_d_data = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        self.data_arr = []
        self.board = """
                {0}|{1}|{2}
                -----------
                {3}|{4}|{5}
                -----------
                {6}|{7}|{8}
                """

        self.arr_deconstruct()

    def arr_deconstruct(self):
        self.data_arr = [j.center(3) for i in self.two_d_data for j in i]

    def print_board(self):
        self.arr_deconstruct()
        print(f'{self.board.format(*self.data_arr)}')

    def player_action(self, player, x, y):
        self.two_d_data[y][x] = player.symbol
        self.print_board()

    def tick_in_cell(self, x, y):
        if self.two_d_data[y][x] != ' ':
            return True
        else:
            return False

    def check_if_winner(self, player):
        # this could be improved by taking the position of last play and check for win. but for now we'll roll with inefficiency
        for i in range(3):
            # check if elements in row i are the same
            if all(j == player.symbol for j in self.two_d_data[i, :]):
                return True
            # check if elements in column i are the same
            elif all(j == player.symbol for j in self.two_d_data[:, i]):
                return True
        # check diagonals
        if all(i == player.symbol for i in self.two_d_data.diagonal()):
            return True
        elif all(i == player.symbol for i in np.fliplr(self.two_d_data).diagonal()):
            return True
        else:
            return False
