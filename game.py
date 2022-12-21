# This module contains an abstraction for the game.

from board import Board
from mine import MineError, Mine
from welcome import Welcome, DifficultyBtn
from score_frame import ScoreFrame
import tkinter as tk
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="./logger.txt",
    format="%(asctime)s; %(levelname)s: %(message)s"
)

class Game:

    def __init__(self) -> None:
        self.b_width = 0
        self.b_height = 0
        self.m_count = 0
        self.non_mine_count = 0
        self.sus = 0
        self.root = tk.Tk()
        self.board = None
        self.title = self.__create_title()
        self.score_frame = ScoreFrame(master=self.root)
        self.welcome_page = Welcome(master=self.root)
        self.log = logging.getLogger("ms_game")

        self.root.report_callback_exception = self.__handle_exceptions


    def __handle_difficulty_choice(self, event: tk.Event):
        """
        To be bound to the difficulty buttons on the welcome page.
        This method tears down the welcome page and builds the 
        actual game after the user input.
        """
        self.log.debug(f"setting board dims due to event {event}")
        self.b_height, self.b_width, self.m_count = event.widget.get_board_dims()

        self.log.info("Building board")
        self.__recursive_teardown(self.welcome_page)
        self.__build_board()
        self.__update_counts()
        self.__update_score_frame()
        self.__paint_gui()


    def __handle_mine_click(self):
        """
        Updates the GUI to show a restart button in the score frame
        area. Also reveals the location of all the pieces.
        """
        restart = tk.Button(master=self.score_frame, text="RESTART?")
        restart.bind("<Button-1>", self.play_game, "+")
        restart.pack()
        self.__reveal_board()


    def __update_gui(self, event: tk.Event):
        """
        Updates the gui by looping through every space on the 
        board and inspecting if they're suspected or selected.
        Updates the win_countdown and sus counts and then 
        redraws the tracking_frame to display info to user.
        """
        self.log.debug(f"Updating the gui due to event {event}")
        if isinstance(event.widget, Mine):
            return self.__handle_mine_click()

        # update sus and win counts
        self.__update_counts()

        # update the score frame
        self.__update_score_frame()


    def __reveal_board(self):
        """
        Loops through all spaces on board and reveals what they
        were by calling the reveal method. To be used when a user
        clicks on a mine.
        """
        for row in self.board.board:
            for space in row:
                space.reveal()


    def play_game(self, event=None):
        """
        Creates a new game in tkinter and launches game loop.
        """
        self.log.info("Starting a new game...")
        self.__set_new_game()

        # start the game
        self.root.mainloop()


    def __handle_exceptions(self, x_type, x_val, traceback):
        """
        Used to set the root callback to catch MineErrors
        that are raised when a user clicks a mine. Default
        is to log the error message.
        """
        self.log.error(f"exception type: {x_type}, val: {x_val}")


    def __set_new_game(self):
        """
        Creates a new tkinter window for a game.
        """
        if self.board is not None:
            self.__recursive_teardown(self.root)
            self.__init__()
        
        self.__set_board_dims()


    def __paint_gui(self):
        """
        Actually places the various frames that are
        properties of this class on the screen.
        """
        self.title.pack(side=tk.TOP)
        self.board.pack(side=tk.LEFT)
        self.score_frame.pack(side=tk.RIGHT)


    def __set_board_dims(self):
        """
        Prompts the user for input on game difficulty.
        Sets board dimension attributes based on selection.
        """
        self.welcome_page.bind_func_to_buttons(self.__handle_difficulty_choice)
        self.welcome_page.display()
        self.log.info("Displaying welcome page")


    def __update_counts(self):
        """
        Sets the count of blank spaces based on board dimensions
        and mine count. To be called after getting user input on 
        difficulty.
        """
        self.non_mine_count = self.b_height * self.b_width - self.m_count
        self.sus = 0
        for row in self.board.board:
            for space in row:
                if space.selected:
                    self.non_mine_count -= 1
                elif space.suspected:
                    self.sus += 1


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


    def __create_title(self):
        """
        Creates the title with label used in the game.
        """
        title_frame = tk.Frame(master=self.root)
        title_label = tk.Label(master=title_frame, text="Mine Sweeper")
        title_label.pack()
        return title_frame


    def __update_score_frame(self):
        """
        Updates the info that you see in the score frame.
        """
        self.score_frame.update_spaces_remaining(self.non_mine_count)
        self.score_frame.update_suspected(self.sus)
        self.score_frame.update_mine_count(self.m_count)


    def __recursive_teardown(self, widget: tk.Widget):
        for child in widget.winfo_children():
            self.__recursive_teardown(child)
        widget.destroy()
