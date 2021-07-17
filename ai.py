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
        for i in range(3):
            all_directions = current_board[i, :], current_board[:, i], current_board.diagonal(), np.fliplr(current_board).diagonal()
            for direction in all_directions:
                coord = self.player_win_with(direction, current_board, i)
                if coord != None:
                    return coord
        
        coord = self.random_tick(boardgame)
        return coord

    def empty_cell(self, listOfELem):
        np.where(listOfELem == ' ')[0].size > 0

    def player_win_with(self, listOfElem, current_board, i):
        setOfElem = []
        for elem in listOfElem:
            if elem in setOfElem and elem != ' ':
                if np.where(listOfElem == ' ')[0].size > 0:
                    if (listOfElem == current_board[i, :]).all():
                        return [i, np.where(listOfElem == ' ')[0][0]]
                    elif (listOfElem == current_board[:, i]).all():
                        return [np.where(listOfElem == ' ')[0][0], i]
                    elif (listOfElem == current_board.diagonal()).all():
                        return [np.where(listOfElem == ' ')[0][0], np.where(listOfElem == ' ')[0][0]]
                    else:
                        return [np.where(listOfElem == ' ')[0][0], 2 - np.where(listOfElem == ' ')[0][0]]
            else:
                setOfElem.append(elem)