# This module contains an abstraction for the game.

from board import Board
import tkinter as tk

class Game:

    def __init__(self, b_width: int, b_height: int, m_count: int) -> None:
        self.win_countdown = b_height * b_width - m_count
        self.window = tk.Tk()
        self.board = Board(b_width, b_height, m_count, self.window)
        self.play_game()


    def play_game(self):
        """
        Creates the board in tkinter
        """
        # create frames for widgets                
        self.window.mainloop()
        # create widgets and bind them to frames
            # create title widget
            # create board widget - each piece is a button
            # create status widget
        # place the frames in the window
        return


    


    def select(self):
        """
        
        """
