from const_val import *

import tkinter as tk
from frames.sample_frame import *
from frames.command_frame import *


class MainProgram(tk.Tk):
    TITLE = "TestLogger"
    VERSION = "0.1"
    PROGRAM_TITLE = str(TITLE+' '+VERSION)

    def __init__(self):
        super().__init__()
        self.title(self.PROGRAM_TITLE)
        self.geometry("1280x720+100+100")

        self.cmd_frame = CommandFrame(self)
        self.sample_frame = SampleFrame(self)

        self.mainloop()