# This module contains an abstraction for spaces that are neither mines
# or neighbors to mines.
from space import Space

class FreeSpace(Space):

    def __init__(self, row, col, board) -> None:
        super().__init__(row, col, board)
        self.bind("<Button-1>", self.select)

    def select(self):
        """
        Recursively expands outwards performing select
        method on neighbors until a mine neighbor is hit.
        """