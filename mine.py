# This module contains an abstraction for the mines used in the game
from space import Space

class MineError(Exception):
    pass

class Mine(Space):
    sel_color = "black"
    
    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)


    def select(self, event):
        """
        Raises MineError to be caught by game.
        """
        raise MineError
