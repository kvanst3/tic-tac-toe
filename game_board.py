class GameBoard():

    def __init__(self):
        self.data_arr = [
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   ',
            '   '
        ]
        self.board = """
                {0}|{1}|{2}
                -----------
                {3}|{4}|{5}
                -----------
                {6}|{7}|{8}
                """

        self.print_board()

    def print_board(self):
        print(f'{self.board.format(*self.data_arr)}')

    def player_action(self, player, position):
        self.data_arr[position] = f' {player.symbol} '
        self.print_board()
