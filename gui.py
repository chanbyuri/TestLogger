from const_val import *

import tkinter as tk
from frames.sample_frame import *
from frames.command_frame import *
import os

class MainProgram(tk.Tk):
    TITLE = "TestLogger"
    VERSION = "0.1"
    PROGRAM_TITLE = str(TITLE+' '+VERSION)
    GEOMETRY = "1280x720+100+100"

    def __init__(self):
        super().__init__()
        self.title(self.PROGRAM_TITLE)
        self.geometry(self.GEOMETRY)

        self.cmd_frame = CommandFrame(self)

        if SAMPLE_FOLDER not in os.listdir():
            os.mkdir(SAMPLE_FOLDER)
        sample_list = os.listdir(SAMPLE_PATH)
        self.sample_frame = SampleFrame(self, sample_list)

        self.mainloop()


if __name__ == '__main__':
    MainProgram()