# This module contains an abstraction for neighbors to mines
from space import Space

class MineNeighbor(Space):
    
    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)
        self.m_touching = 0


    @property
    def display_text(self):
        return f"{self.m_touching}"


    def put_on_board(self):
        super().put_on_board()
        self.grid(row=self.row, column=self.col)


    def select(self, event):
        """
        Configures the space to display the number of mines
        touching the space. Bound to left click.
        """
        super().select(event)


    def add_mine(self):
        """
        Increments a mine neighbor's m_touching value.
        """
        self.m_touching += 1