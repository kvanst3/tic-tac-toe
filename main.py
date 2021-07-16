from game_board import GameBoard
from player import Player
from ai import Ai


p1 = Player('X')
p2 = Player('0')

gb = GameBoard()


# against other player
game_on = True
players = [p1, p2]
gb.print_board()
while game_on:
    for player in players:
        loc = [999, 999]
        while loc[0] not in [0, 1, 2] or loc[1] not in [0, 1, 2]:
            usr_input = [char for char in input('Specify location. Row 0 to 2, Column 0 to 2. e.g: 01, 22, 02, etc.\n')]
            try:
                loc = [int(i) for i in usr_input]
                if gb.tick_in_cell(loc[0], loc[1]):
                    print('Already a tick, naughty cheater.')
                    loc = [999, 999]
            except ValueError:
                print("Invalid key.")
        gb.player_action(player, loc[0], loc[1])
        if gb.check_if_winner(player):
            print(f"{player.name} won")
            player.win()
            game_on = False
            break


# against computer
game_on = True
p2 = Ai('0')
gb.print_board()
while game_on:
    loc = [999, 999]
    while loc[0] not in [0, 1, 2] or loc[1] not in [0, 1, 2]:
        usr_input = [char for char in input('Specify location. Row 0 to 2, Column 0 to 2. e.g: 01, 22, 02, etc.\n')]
        try:
            loc = [int(i) for i in usr_input]
            if gb.tick_in_cell(loc[0], loc[1]):
                print('Already a tick, naughty cheater.')
                loc = [999, 999]
        except ValueError:
            print("Invalid key.")
    gb.player_action(p1, loc[0], loc[1])
    if gb.check_if_winner(p1):
        print(f"{p1.name} won")
        p1.win()
        game_on = False
        break
    coord = p2.determine_move()
    gb.player_action(p2, coord[0], coord[1])
    if gb.check_if_winner(p2):
        print(f"{p2.name} won")
        p2.win()
        game_on = False
        break
