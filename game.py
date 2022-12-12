# This module contains an abstraction for the game.

from board import Board
from mine import MineError
import tkinter as tk

class Game:

    def __init__(self) -> None:
        self.b_width = 0
        self.b_height = 0
        self.m_count = 0
        self.win_countdown = 0
        self.root = None
        self.board = None
        self.set_new_game()


    def play_game(self):
        """
        Creates the board in tkinter
        """
        # set up exception handling for catching the mine exception
        self.root.report_callback_exception = self.handle_exceptions

        # build out the board gui and start the game
        self.board.build_board()
        self.root.mainloop()



    def handle_exceptions(self, x_type, x_val, traceback):
        if isinstance(x_val, MineError):
            self.set_new_game()
            self.play_game()
        print(x_val)


    def set_new_game(self):
        """
        Creates a new tkinter window for a game.
        """
        if self.root is not None:
            self.root.destroy()
        self.set_root()
        self.set_board_dims()
        self.set_board()
        self.set_win_countdown()


    def set_board_dims(self):
        valid = False
        while not valid:
            print("Please choose a difficulty:")
            print(" Enter 1 for Easy (10x10)")
            print(" Enter 2 for Medium (20x20)")
            print(" Enter 3 for Hard (30x30)")
            choice = input(":")
            valid = True
            
            if choice == "1":
                self.b_width, self.b_height = 10, 10
                self.m_count = 20
            elif choice == "2":
                self.b_width, self.b_height = 20, 20
                self.m_count = 100
            elif choice == "3":
                self.b_width, self.b_height = 20, 20
                self.m_count = 180
            else:
                valid = False


    def set_win_countdown(self):
        self.win_countdown = self.b_height * self.b_width - self.m_count


    def decrease_win_countdown(self):
        self.win_countdown -= 1


    def increase_win_countdown(self):
        self.win_countdown += 1


    def set_board(self):
        self.board = Board(self.b_width, self.b_height, self.m_count, self.root, self)


    def set_root(self):
        self.root = tk.Tk()
