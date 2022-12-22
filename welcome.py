import tkinter as tk
import logging


class DifficultyBtn(tk.Button):
    
    def __init__(self, master, difficulty, **kwargs):
        super().__init__(master=master, **kwargs)
        self.difficulty = difficulty
    
    
    def get_board_dims(self):
        if self.difficulty == "EASY":
            # returns height, width, mine_count
            return 10, 10, 20
        elif self.difficulty == "MEDIUM":
            return 10, 10, 30
        else:
            return 15, 15, 55



class Welcome(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.title_frame = self.__create_title("Please choose a difficulty")
        self.easy_btn = self.__create_difficulty_btn(20, "EASY")
        self.med_btn = self.__create_difficulty_btn(40, "MEDIUM")
        self.hard_btn = self.__create_difficulty_btn(60, "HARD")
        self.log = logging.getLogger("welcome")


    def __create_title(self, title_label):
        """
        Creates a tkinter frame with a label that is passed in as
        argument title_label. Returns the frame.
        """
        frame = tk.Frame(master=self, height=15, width=20)
        label = tk.Label(master=frame, text=title_label)
        label.pack()
        return frame


    def __create_difficulty_btn(self, mine_count, difficulty_label):
        """
        Creates a tkinter frame with a button that a user can click
        to set the game difficulty. Must pass the mine_count (int) and 
        difficulty label (string). Returns the frame.
        """

        button = DifficultyBtn(
            master=self,
            difficulty=difficulty_label.upper(),
            text=f"{difficulty_label}\n{mine_count} mines",
            width=15,
            height=10
        )
        button
        return button


    def display(self):
        """
        Paints the frame with the various choices on the screen.
        """
        self.title_frame.pack(expand=tk.TRUE, fill=tk.BOTH)
        self.easy_btn.pack(expand=tk.TRUE, fill=tk.BOTH, side=tk.LEFT)
        self.med_btn.pack(expand=tk.TRUE, fill=tk.BOTH, side=tk.LEFT)
        self.hard_btn.pack(expand=tk.TRUE, fill=tk.BOTH, side=tk.LEFT)
        self.pack(expand=tk.TRUE, fill=tk.BOTH)


    def bind_func_to_buttons(self, func):
        """
        Binds the passed func to left button clicks for each
        difficulty button.
        """
        self.log.debug(f"Binding func to buttons: {func}")
        self.easy_btn.bind("<Button-1>", func)
        self.med_btn.bind("<Button-1>", func)
        self.hard_btn.bind("<Button-1>", func)
