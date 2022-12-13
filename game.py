# This module contains an abstraction for the game.

from board import Board
from mine import MineError
import tkinter as tk
import logging


class Game:

    def __init__(self) -> None:
        self.b_width = 0
        self.b_height = 0
        self.m_count = 0
        self.non_mine_count = 0
        self.sus = 0
        self.root = tk.Tk()
        self.board = None
        self.title = tk.Frame(master=self.root)
        self.tracking_frame = tk.Frame(master=self.root)
        self.log = logging.getLogger("ms_game")


    def __update_gui(self, event):
        """
        Updates the gui by looping through every space on the 
        board and inspecting if they're suspected or selected.
        Updates the win_countdown and sus counts and then 
        redraws the tracking_frame to display info to user.
        """
        # update sus and win counts
        self.__set_blank_space_count()
        self.sus = 0
        for row in self.board.board:
            for space in row:
                if space.suspected:
                    self.sus += 1
                if space.selected:
                    self.non_mine_count -= 1

        # update the tracking frame
        children = self.tracking_frame.winfo_children()
        for child in children:
            child.destroy()

        self.__create_tracking_label()
        self.tracking_frame.pack()


    def play_game(self):
        """
        Creates a new game in tkinter and launches game loop.
        """

        self.__set_new_game()

        # start the game
        self.root.mainloop()


    def __handle_exceptions(self, x_type, x_val, traceback):
        """
        Used to set the root callback to catch MineErrors
        that are raised when a user clicks a mine. Default
        is to log the error message.
        """
        if isinstance(x_val, MineError):
            return self.play_game()
        self.log.log(x_type)


    def __set_new_game(self):
        """
        Creates a new tkinter window for a game.
        """
        if self.board is not None:
            self.root.destroy()
            self.root = tk.Tk()
            self.title = tk.Frame(master=self.root)
            self.tracking_frame = tk.Frame(master=self.root)
        self.__set_root_callback()
        self.__create_title_label()
        self.__set_board_dims()
        self.__build_board()
        self.__set_blank_space_count()
        self.__create_tracking_label()
        self.__paint_gui()


    def __paint_gui(self):
        """
        Actually places the various frames that are
        properties of this class on the screen.
        """
        self.title.pack(side=tk.TOP)
        self.board.pack(side=tk.LEFT)
        self.tracking_frame.pack(side=tk.RIGHT)


    def __set_board_dims(self):
        """
        Prompts the user for input on game difficulty.
        Sets board dimension attributes based on selection.
        """
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


    def __set_blank_space_count(self):
        """
        Sets the count of blank spaces based on board dimensions
        and mine count. To be called after getting user input on 
        difficulty.
        """
        self.non_mine_count = self.b_height * self.b_width - self.m_count
        self.sus = 0


    def __build_board(self):
        """
        Creates the board frame to be used in the gui along with all
        of the space widgets. Sets the board frame as a class property.
        Binds the update of the gui to the board spaces so that tracking
        frame can be updated on each click.
        """
        self.board = Board(self.b_width, self.b_height, self.m_count, self.root)
        self.board.build_board()
        self.__bind_update_gui()


    def __bind_update_gui(self):
        """
        Binds the update_gui method to the spaces on the board
        so that tracking frame can be updated with each click.
        """
        for row in self.board.board:
            for space in row:
                space.bind("<Button-1>", self.__update_gui, "+")
                space.bind("<Button-3>", self.__update_gui, "+")


    def __set_root_callback(self):
        """
        Sets callback behavior for the tkinter root.
        """
        self.root.report_callback_exception = self.__handle_exceptions


    def __create_title_label(self):
        """
        Creates the label used in the title frame.
        """
        title_label = tk.Label(master=self.title, text="Mine Sweeper")
        title_label.pack()


    def __create_tracking_label(self):
        """
        Creates the labels used in the tracking frame.
        """
        sus_label = tk.Label(master=self.tracking_frame, text="Suspected")
        sus_count = tk.Label(master=self.tracking_frame, text=self.sus)
        win_label = tk.Label(master=self.tracking_frame, text="Spaces Remaining")
        win_count = tk.Label(master=self.tracking_frame, text=self.non_mine_count)
        sus_label.pack()
        sus_count.pack()
        win_label.pack()
        win_count.pack()
