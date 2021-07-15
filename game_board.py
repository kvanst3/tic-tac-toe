class GameBoard():

    def __init__(self):
        self.data_dict = {
            'A1': '   ',
            'A2': '   ',
            'A3': '   ',
            'B1': '   ',
            'B2': '   ',
            'B3': '   ',
            'C1': '   ',
            'C2': '   ',
            'C3': '   '
        }
        self.board = """
                {A1}|{A2}|{A3}
                -----------
                {B1}|{B2}|{B3}
                -----------
                {C1}|{C2}|{C3}
                """.format(**self.data_dict)

        self.print_board()

    def print_board(self):
        print(f'{self.board}')
