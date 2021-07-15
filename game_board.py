class GameBoard():

    def __init__(self):
        self.three_d_data = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.data_arr = []
        self.board = """
                {0}|{1}|{2}
                -----------
                {3}|{4}|{5}
                -----------
                {6}|{7}|{8}
                """

        self.arr_deconstruct()
        self.print_board()

    def arr_deconstruct(self):
        self.data_arr = [j.center(3) for i in self.three_d_data for j in i]

    def print_board(self):
        self.arr_deconstruct()
        print(f'{self.board.format(*self.data_arr)}')

    def player_action(self, player, x, y):
        self.three_d_data[y][x] = player.symbol
        self.print_board()
