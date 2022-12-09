# This module contains an abstraction for neighbors to mines
from space import Space

class MineNeighbor(Space):
    
    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)
        self.m_touching = 0


    def put_on_board(self):
        super().put_on_board()
        self.bind("<Button-1>", self.__select)
        self.config(text=f"{self.m_touching}")
        self.grid(row=self.row, column=self.col)


    def __select(self, event):
        super().__select()


    def add_mine(self):
        """
        Increments a mine neighbor's m_touching value.
        """
        self.m_touching += 1