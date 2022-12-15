# This module contains an abstraction for spaces on the board.
from tkinter import Button, RAISED
import logging

class Space(Button):
    bg_color = "grey"
    sus_color = "yellow"
    sel_color = "red"

    def __init__(self, row, col, board) -> None:
        self.board = board
        self.row = row
        self.col = col
        self.neighbors = []
        self.suspected = False
        self.selected = False
        self.log = logging.getLogger("space")


    @property
    def display_text(self):
        return ""


    def add_neighbor(self, neighbor):
        """
        Adds a space's neighbor to its list of neighbors. 
        Note - neighbor must be a space, mine, or
        mine neighbor type.
        """
        self.neighbors.append(neighbor)


    def put_on_board(self):
        """
        Performs the tkinter actions necessary to put the
        space on the board and binds the necessary actions
        to the space.
        """
        super().__init__(
            master=self.board,
            relief=RAISED,
            borderwidth=1,
            width=3,
            height=2,
            background="grey"
        )

        # bind right mouse click actions to button
        self.bind("<Button-3>", self.__toggle_suspect, "+")
        self.bind("<Button-1>", self.select, "+")
        self.grid(row=self.row, column=self.col)


    def select(self, event):
        if not self.selected:
            self.log.info(f"Selecting ({self.row, self.col})")
            self.suspected = False
            self.selected = True
            self.reveal()


    def reveal(self):
        """
        Reveals the space by changing background to approp color.
        """
        self.config(background=self.sel_color, text=self.display_text)


    def __toggle_suspect(self, event):
        """
        Toggles the suspected attribute between True/False.
        Also updates the button text to show a question mark on 
        the GUI.
        """
        
        if self.selected:
            return
        self.suspected = not self.suspected
        if self.suspected:
            self.log.info(f"Flagging {self.row, self.col} as suspected")
            return self.config(text="?", background=self.sus_color)

        self.log.info(f"Removing sus flag from {self.row, self.col}")    
        self.config(text="", background=self.bg_color)