class GameBoard():

    def __init__(self):
        board = """
                {}|{}|{}
                -----
                {}|{}|{}
                -----
                {}|{}|{}
                """.format('x','x','o','o','o','x','o','x','o')
        print(board)
