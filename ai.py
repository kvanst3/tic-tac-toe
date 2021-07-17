from random import randint
import random
from player import Player
import numpy as np


class Ai(Player):
    
    def __init__(self, symbol):
        super().__init__(symbol)

    def random_tick(self, boardgame):
        x = randint(0, 2)
        y = randint(0, 2)
        if boardgame.two_d_data[x, y] == ' ':
            return [x, y]
        else:
            return self.random_tick(boardgame)
    
    def determine_move(self, boardgame):
        current_board = boardgame.two_d_data
        # loop 3 times to get all possible array sets
        for i in range(3):
            # get all the possible array sets (rows, columns, and diagonals)
            all_directions = current_board[i, :], current_board[:, i], current_board.diagonal(), np.fliplr(current_board).diagonal()
            for direction in all_directions:
                coord = self.player_win_with(direction, current_board, i)
                if coord != None:
                    # return the coords of player possible win to counter-act
                    return coord
        # if player is not about to win, put in a random tick
        coord = self.random_tick(boardgame)
        return coord

    def empty_cell(self, listOfELem):
        np.where(listOfELem == ' ')[0].size > 0

    def player_win_with(self, listOfElem, current_board, i):
        # set of elem used to determine if two same ticks are in a given array. If yes, and no third thick: tick.
        setOfElem = []
        for elem in listOfElem:
            # check the elem against the (first round) empty list, and add it (else) to list if not found.
            if elem in setOfElem and elem != ' ':
                # if 2 similar ticks in array, find the empty one.
                if np.where(listOfElem == ' ')[0].size > 0:
                    # return if its a ROW that contains the threat
                    if (listOfElem == current_board[i, :]).all():
                        return [i, np.where(listOfElem == ' ')[0][0]]
                    # return if its a COLUMN that contains the threat
                    elif (listOfElem == current_board[:, i]).all():
                        return [np.where(listOfElem == ' ')[0][0], i]
                    # return if its the DIAGONAL that contains the threat
                    elif (listOfElem == current_board.diagonal()).all():
                        return [np.where(listOfElem == ' ')[0][0], np.where(listOfElem == ' ')[0][0]]
                    else:
                    # return if its the ANTI-DIAGONAL that contains the threat
                        return [np.where(listOfElem == ' ')[0][0], 2 - np.where(listOfElem == ' ')[0][0]]
            else:
                setOfElem.append(elem)
