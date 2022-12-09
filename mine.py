# This module contains an abstraction for the mines used in the game
from space import Space

class MineError(Exception):
    pass

class Mine(Space):
    bg_color = "black"
    
    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)


    def put_on_board(self):
        super().put_on_board()
        self.bind("<Button-1>", self.__select)
        self.config(background="black")
        self.grid(row=self.row, column=self.col)


    def __select(self, event):
        super().__select()
        raise MineError
