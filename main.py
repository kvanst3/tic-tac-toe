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

gb.player_action(p1, 4)


