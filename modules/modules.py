import tkinter as tk

from const_val import *
from frames.const_val import *


class LeftSideButton(tk.Button):
    def __init__(self, master, text, command):
        super().__init__(master, text=text, command=command)
        self.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)


class LeftSideLabel(tk.Label):
    def __init__(self, master, text):
        super().__init__(master, text=text)
        self.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)


class LeftSideEntry(tk.Entry):
    def __init__(self, master, state, str_var):
        super().__init__(master, textvariable=str_var, state=state, width=5)
        self.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD, fill='x', expand=True)


class LedCanvas(tk.Canvas):
    def __init__(self, master):
        super().__init__(master,width=20, height=20)
        self.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)
        self.draw_red_led()
    def draw_red_led(self):
        self.create_oval(2,2,21,21,fill='red')
    def draw_green_led(self):
        self.create_oval(2,2,21,21,fill='green')

