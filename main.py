from numpy.core.numeric import False_
from game_board import GameBoard
from player import Player
from ai import Ai


GAME_ON = True


def winner(player):
    if gb.check_if_winner(player):
        print(f"{player.name} won")
        player.win()
        global GAME_ON
        GAME_ON = False
        return True


def board_full(gameboard):
    if ' ' not in gameboard.two_d_data:
        return True


p1 = Player('X')
p2 = Player('0')

gb = GameBoard()


# # against other player
# GAME_ON = True
# players = [p1, p2]
# gb.print_board()
# while GAME_ON:
#     for player in players:
#         loc = [999, 999]
#         while loc[0] not in [0, 1, 2] or loc[1] not in [0, 1, 2]:
#             usr_input = [char for char in input('Specify location. Row 0 to 2, Column 0 to 2. e.g: 01, 22, 02, etc.\n')]
#             try:
#                 loc = [int(i) for i in usr_input]
#                 if gb.tick_in_cell(loc[0], loc[1]):
#                     print('Already a tick, naughty cheater.')
#                     loc = [999, 999]
#             except ValueError:
#                 print("Invalid key.")
#         gb.player_action(player, loc[0], loc[1])
#         if gb.check_if_winner(player):
#             print(f"{player.name} won")
#             player.win()
#             GAME_ON = False
#             break


# against computer

p2 = Ai('0')
gb.print_board()
while GAME_ON:
    # start with impossible coord to force while loop
    loc = [999, 999]
    while loc[0] not in [0, 1, 2] or loc[1] not in [0, 1, 2]:
        usr_input = [char for char in input('Specify location. Row 0 to 2, Column 0 to 2. e.g: 01, 22, 02, etc.\n')]
        try:
            # make sure we're dealing with ints
            loc = [int(i) for i in usr_input]
            # check if user isn't trying to be cheeky and tick an already ticked cell
            if gb.tick_in_cell(loc[0], loc[1]):
                print('Already a tick, naughty cheater.')
                loc = [999, 999]
        # contingency for user keying in nans
        except ValueError:
            print("Invalid key.")
    gb.player_action(p1, loc[0], loc[1])
    if winner(p1) or board_full(gb):
        break

    coord = p2.determine_move(gb)
    gb.player_action(p2, coord[0], coord[1])
    if winner(p2) or board_full(gb):
        break
