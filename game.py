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


    def update_gui(self, event):
        print(self.win_countdown)


    def bind_update_gui(self):
        """
        Binds the update_gui method to the spaces on the board
        so that win countdown can be tracked.
        """
        for row in self.board.board:
            for space in row:
                space.bind("<Button-1>", self.update_gui, "+")


    def play_game(self):
        """
        Creates a new game in tkinter and launches game loop.
        """

        self.set_new_game()

        # start the game
        self.root.mainloop()



    def handle_exceptions(self, x_type, x_val, traceback):
        if isinstance(x_val, MineError):
            self.play_game()
        print(x_val)


    def set_new_game(self):
        """
        Creates a new tkinter window for a game.
        """
        if self.root is not None:
            self.root.destroy()
        self.set_root()
        title = self.create_title()
        title.pack()
        self.set_board_dims()
        self.build_board()
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


    def build_board(self):
        self.board = Board(self.b_width, self.b_height, self.m_count, self.root, self)
        self.board.build_board()
        self.bind_update_gui()


    def set_root(self):
        self.root = tk.Tk()
        self.root.report_callback_exception = self.handle_exceptions


    def create_title(self):
        title = tk.Frame(master=self.root)
        title_label = tk.Label(master=title, text="Mine Sweeper")
        title_label.pack()
        return title