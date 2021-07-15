from game_board import GameBoard
from player import Player


p1 = Player('X')
p2 = Player('0')

# original_name = input('P1 want to change name?')
# if original_name == 'y':
#     new_name = input('Well? Go on then!\n')
#     p1.change_name(new_name)
#     print(p1.name)

gb = GameBoard()

gb.player_action(p1, 0, 2)
gb.player_action(p1, 1, 1)
gb.player_action(p1, 2, 2)
if gb.check_if_winner(p1):
    print("you won")
else:
    print("not yet")

