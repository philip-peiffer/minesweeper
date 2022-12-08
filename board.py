# This module contains an abstraction for the board itself.
from space import Space
from mine import Mine
from tkinter import Frame, Button
import random

class Board(Frame):

    def __init__(self, width, height, mine_count, master) -> None:
        super().__init__(master=master)
        self.width = width
        self.height = height
        self.mine_count = mine_count
        self.board = [
            [Space(row, col, master=self) for col in range(self.width)]\
            for row in range(self.height)
        ]
        
        # pack the board inside its parent window
        self.pack()


    def pop_mines(self, mine_count: int) -> None:
        """
        Creates the mines and places them on the game board. Requires
        the mine count as an argument. No return.
        """
        if mine_count >= self.width * self.height:
            raise ValueError

        while mine_count > 0:
            x, y = self.rand_pos()
            if not isinstance(self.board[x][y], Mine):
                mine_count -= 1
                self.board[x][y] = Mine(x, y, master=self)


    def rand_pos(self) -> tuple:
        """
        Returns a random position on the board in the form (x_pos, y_pos).
        """
        rand_x_pos = random.randrange(0, self.width)
        rand_y_pos = random.randrange(0, self.height)
        return (rand_x_pos, rand_y_pos)