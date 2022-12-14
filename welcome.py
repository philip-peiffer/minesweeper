import tkinter as tk

class Welcome(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.easy_frame = self.__create_difficulty_box(20, "EASY")
        self.med_frame = self.__create_difficulty_box(40, "MEDIUM")
        self.hard_frame = self.__create_difficulty_box(60, "HARD")


    def __create_difficulty_box(self, mine_count, difficulty_label):
        """
        Creates a tkinter frame with a button that a user can click
        to set the game difficulty. Must pass the mine_count (int) and 
        difficulty label (string). Returns the frame.
        """
        frame = tk.Frame(master=self)
        button = tk.Button(master=frame, text=f"{difficulty_label}\n{mine_count} mines")
        button.pack(expand=tk.TRUE)
        return frame


    def display(self):
        """
        Paints the frame with the various choices on the screen.
        """
        self.easy_frame.pack(side=tk.LEFT)
        self.med_frame.pack()
        self.hard_frame.pack(side=tk.RIGHT)
        self.pack()


    def tear_down(self):
        """
        Removes the frame and all children from the screen by
        destroying it.
        """
        self.destroy()


    def bind_func_to_buttons(self, func):
        """
        Binds the passed func to left button clicks for each
        difficulty button.
        """
        self.easy_frame.bind("<Button-1>", func)
        self.med_frame.bind("<Button-1>", func)
        self.hard_frame.bind("<Button-1>", func)
