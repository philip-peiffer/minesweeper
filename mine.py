# This module contains an abstraction for the mines used in the game

class Mine:

    def __init__(self, x_pos: int, y_pos: int) -> None:
        self.position = (x_pos, y_pos)
        self.neighbors = self.find_neighbors()

    def find_neighbors(self) -> list:
        return []