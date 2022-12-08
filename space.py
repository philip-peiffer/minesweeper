# This module contains an abstraction for spaces on the board.

class Space:

    def __init__(self, x_pos: int, y_pos: int) -> None:
        self.suspected = False
        self.selected = False
        self.position = (x_pos, y_pos)
    
    def select(self):
        self.selected = True
    
    def toggle_suspect(self):
        """Toggles the suspected attribute between True/False."""
        self.suspected = not self.suspected