# This module contains an abstraction for spaces on the board.
from tkinter import Button, RAISED, SUNKEN

class Space(Button):
    bg_color = "grey"
    sus_color = "yellow"

    def __init__(self, row, col, board) -> None:
        self.board = board
        self.row = row
        self.col = col
        self.suspected = False
        self.selected = False


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
        self.bind("<Button-3>", self.__toggle_suspect)
        self.grid(row=self.row, column=self.col)


    def __select(self):
        self.selected = True
        self.config(relief=SUNKEN)
        # TODO: on inheriting classes, call super.select() but then
        # each has their own way of changing config


    def __toggle_suspect(self, event):
        """
        Toggles the suspected attribute between True/False.
        Also updates the button text to show a question mark on 
        the GUI.
        """
        
        self.suspected = not self.suspected
        if self.suspected:
            self.config(text="?", background=self.sus_color)
            return
        self.config(text="", background=self.bg_color)