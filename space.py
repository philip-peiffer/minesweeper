# This module contains an abstraction for spaces on the board.
from tkinter import Button, RAISED, SUNKEN

class Space(Button):
    bg_color = "grey"
    sus_color = "yellow"

    def __init__(self, row, col, board) -> None:
        self.board = board
        self.row = row
        self.col = col
        self.neighbors = []
        self.suspected = False
        self.selected = False


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
        self.bind("<Button-3>", self.__toggle_suspect)
        self.bind("<Button-1>", self.select)
        self.grid(row=self.row, column=self.col)


    def select(self, event):
        print(f"selected {self.row, self.col}")
        if not self.selected:
            self.selected = True
            self.config(background="red")


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