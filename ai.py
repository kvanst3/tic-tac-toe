from random import randint
import random
from player import Player
import numpy as np


class Ai(Player):
    
    def __init__(self):
        super().__init__()

    def random_tick(self, boardgame):
        x = randint(0, 2)
        y = randint(0, 2)
        if boardgame[x, y] == ' ':
            return [x, y]
        else:
            self.random_tick(boardgame)
    
    def determine_move(self, boardgame):
        current_board = boardgame.two_d_data
        for i in range(3):
            #get row
            listOfELem = current_board[i, :]
            setOfElem = []
            # check if duplicates (non empty) in row. If yes return coordinates
            for elem in listOfELem:
                if elem in setOfElem and elem != ' ':
                    return [i, elem]
                else:
                    setOfElem.append(elem)
            #get row
            listOfELem = current_board[:, i]
            setOfElem = []
            # check if duplicates (non empty) in column. If yes return coordinates
            for elem in listOfELem:
                if elem in setOfElem and elem != ' ':
                    return [elem, i]
                else:
                    setOfElem.append(elem)
            # check diagonal
            listOfELem = current_board.diagonal()
            for elem in listOfELem:
                    if elem in setOfElem and elem != ' ':
                        return [i, elem]
                    else:
                        setOfElem.append(elem)
            #check invert diagonal
            listOfELem = np.fliplr(current_board).diagonal()
            for elem in listOfELem:
                if elem in setOfElem and elem != ' ':
                    return [elem, i]
                else:
                    setOfElem.append(elem)
        
        coord = self.random_tick
        return coord
