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
        self.sus = 0
        self.root = tk.Tk()
        self.board = None
        self.title = tk.Frame(master=self.root)
        self.tracking_frame = tk.Frame(master=self.root)


    def update_gui(self, event):
        """
        Updates the gui by looping through every space on the 
        board and inspecting if they're suspected or selected.
        Updates the win_countdown and sus counts and then 
        redraws the tracking_frame to display info to user.
        """
        # update sus and win counts
        self.set_win_countdown()
        self.sus = 0
        for row in self.board.board:
            for space in row:
                if space.suspected:
                    self.sus += 1
                if space.selected:
                    self.win_countdown -= 1

        # update the tracking frame
        children = self.tracking_frame.winfo_children()
        for child in children:
            child.destroy()

        self.create_tracking_label()
        self.tracking_frame.pack()


    def bind_update_gui(self):
        """
        Binds the update_gui method to the spaces on the board
        so that win countdown can be tracked.
        """
        for row in self.board.board:
            for space in row:
                space.bind("<Button-1>", self.update_gui, "+")
                space.bind("<Button-3>", self.update_gui, "+")


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
        if self.board is not None:
            self.root.destroy()
            self.root = tk.Tk()
            self.title = tk.Frame(master=self.root)
            self.tracking_frame = tk.Frame(master=self.root)
        self.set_root_callback()
        self.create_title_label()
        self.set_board_dims()
        self.build_board()
        self.set_win_countdown()
        self.create_tracking_label()
        self.paint_gui()


    def paint_gui(self):
        """
        Actually places the various frames that are
        properties of this class on the screen.
        """
        self.title.pack()
        self.board.pack()
        self.tracking_frame.pack()


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


    def set_root_callback(self):
        
        self.root.report_callback_exception = self.handle_exceptions


    def create_title_label(self):
        title_label = tk.Label(master=self.title, text="Mine Sweeper")
        title_label.pack()


    def create_tracking_label(self):
        sus_label = tk.Label(master=self.tracking_frame, text="Suspected")
        sus_count = tk.Label(master=self.tracking_frame, text=self.sus)
        win_label = tk.Label(master=self.tracking_frame, text="Spaces Remaining")
        win_count = tk.Label(master=self.tracking_frame, text=self.win_countdown)
        sus_label.pack()
        sus_count.pack()
        win_label.pack()
        win_count.pack()