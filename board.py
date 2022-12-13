# This module contains an abstraction for the board itself.
from free_space import FreeSpace
from mine import Mine
from mine_neighbors import MineNeighbor
from tkinter import Frame
import random

class Board(Frame):

    def __init__(self, width, height, mine_count, master_window, game) -> None:
        self.game = game
        self.master = master_window
        self.width = width
        self.height = height
        self.spaces = width*height
        self.mine_count = mine_count
        self.board = [
            [FreeSpace(row, col, self) for col in range(self.width)]\
            for row in range(self.height)
        ]
        super().__init__(master=self.master)


    def build_board(self):
        """
        Performs the tkinter actions necessary to build the board
        frame on the screen.
        """
        self.__place_pieces()


    def __place_pieces(self):
        """
        Performs the tkinter actions necessary to build the buttons
        onto the board frame.
        """
        self.__create_mines()
        for row in self.board:
            for space in row:
                space.put_on_board()
                self.__add_neighbors(space)


    def __create_mines(self) -> None:
        """
        Creates the mines and places them on the game board. No return.
        """
        if self.mine_count >= self.spaces:
            raise ValueError
        
        mines_left = self.mine_count
        while mines_left > 0:
            row, col = self.__rand_pos()
            if not isinstance(self.board[row][col], Mine):
                mines_left -= 1
                new_mine = Mine(row, col, board=self)
                self.board[row][col] = new_mine
                self.__create_mine_neighbors(new_mine)


    def __create_mine_neighbors(self, mine):
        """
        Looks at all spaces connected to a mine's location given
        by the mine and replaces any space object
        with a mine_neighbor object. If a mine_neighbor already
        exists there, then increments neighbor count.
        """
        for row in range(-1, 2):
            for col in range(-1, 2):
                n_row = mine.row + row
                n_col = mine.col + col
                
                row_out_bound = (n_row >= self.height or n_row < 0)
                col_out_bound = (n_col >= self.width or n_col < 0)
                if row_out_bound or col_out_bound:
                    continue

                neighbor = self.board[n_row][n_col]
                neighbor_is_mine = isinstance(neighbor, Mine)
                
                if neighbor_is_mine:
                    continue

                if not isinstance(neighbor, MineNeighbor):
                    neighbor = MineNeighbor(n_row, n_col, self)
                    self.board[n_row][n_col] = neighbor
                neighbor.add_mine()


    def __add_neighbors(self, space):
        """
        Requires a space as an argument, which must be a space, 
        a mine, or mine neighbor type. Finds the connected nodes 
        to space, and adds them to the list of neighbors stored in
        the space object.
        NOTE - this must be done after placing all pieces on the board
        so that the neighbor lists are correct.
        """
        if not isinstance(space, (FreeSpace, Mine, MineNeighbor)):
            raise ValueError

        for row in range(-1, 2):
            for col in range(-1, 2):
                n_row = space.row + row
                n_col = space.col + col
                
                pointing_at_self = ((row, col) == (0, 0))
                row_out_bound = (n_row >= self.height or n_row < 0)
                col_out_bound = (n_col >= self.width or n_col < 0)
                
                if pointing_at_self or row_out_bound or col_out_bound:
                    continue

                space.add_neighbor(self.board[n_row][n_col])


    def __rand_pos(self) -> tuple:
        """
        Returns a random position on the board in the form (x_pos, y_pos).
        """
        rand_col = random.randrange(0, self.width)
        rand_row = random.randrange(0, self.height)
        return (rand_row, rand_col)