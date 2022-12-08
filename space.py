# This module contains an abstraction for spaces on the board.
from tkinter import Button, RAISED, SUNKEN

class Space(Button):
    bg_color = "grey"
    sus_color = "yellow"

    def __init__(self, row, col, master) -> None:
        super().__init__(
            master=master,
            relief=RAISED,
            borderwidth=1,
            width=3,
            height=2,
            background="grey"
        )
        self.row = row
        self.col = col
        self.suspected = False
        self.selected = False

        # bind right mouse click actions to button
        self.bind("<Button-3>", self.toggle_suspect)
        self.grid(row=self.row, column=self.col)


    def select(self):
        self.selected = True
        self.config(relief=SUNKEN)
        # TODO: on inheriting classes, call super.select() but then
        # each has their own way of changing config


    def toggle_suspect(self, *args):
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