# This module contains an abstraction for the board itself.
from space import Space
from mine import Mine
from tkinter import Frame
import random

class Board(Frame):

    def __init__(self, width, height, mine_count, master) -> None:
        self.master = master
        self.width = width
        self.height = height
        self.spaces = width*height
        self.mine_count = mine_count
        self.board = [
            [Space(row, col, board=self) for col in range(self.width)]\
            for row in range(self.height)
        ]


    def build_board(self):
        """
        Performs the tkinter actions necessary to build the board
        frame on the screen.
        """
        super().__init__(master=self.master)
        self.__place_pieces()

        # pack the board inside its parent window
        self.pack()


    def __place_pieces(self):
        """
        Performs the tkinter actions necessary to build the buttons
        onto the board frame.
        """
        self.__create_mines()
        for row in self.board:
            for space in row:
                space.put_on_board()


    def __create_mines(self) -> None:
        """
        Creates the mines and places them on the game board. Requires
        the mine count as an argument. No return.
        """
        if self.mine_count >= self.spaces:
            raise ValueError
        
        mines_left = self.mine_count
        while mines_left > 0:
            row, col = self.__rand_pos()
            if not isinstance(self.board[row][col], Mine):
                mines_left -= 1
                self.board[row][col] = Mine(row, col, board=self)


    def __rand_pos(self) -> tuple:
        """
        Returns a random position on the board in the form (x_pos, y_pos).
        """
        rand_col = random.randrange(0, self.width)
        rand_row = random.randrange(0, self.height)
        return (rand_row, rand_col)