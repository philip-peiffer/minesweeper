from tkinter import Frame, Label, StringVar

class ScoreFrame(Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.__mine_count = StringVar(master=self, value='0')
        self.__spaces_remaining = StringVar(master=self, value='0')
        self.__sus_track = StringVar(master=self, value='0')
        self.__create_label("Mine Countdown", self.__mine_count)
        self.__create_label("Spaces Remaining", self.__spaces_remaining)
        self.__create_label("Suspected", self.__sus_track)


    def __create_label(self, label_text, var):
        Label(master=self, text=label_text).pack()
        Label(master=self, textvariable=var).pack()


    def update_spaces_remaining(self, val):
        self.__spaces_remaining.set(f"{val}")


    def update_suspected(self, val):
        self.__sus_track.set(f"{val}")


    def update_mine_count(self, val):
        self.__mine_count.set(f"{val}")