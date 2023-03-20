import tkinter as tk
import tkinter.messagebox
import os
# from ..const_val import *
from frames.const_val import *
from const_val import *
from modules.modules import *
import tkinter.simpledialog


class CommandFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side='top', fill='x', expand=False, padx=FRAME_PAD, pady=FRAME_PAD)

        sample_cmd_frm = BaseCommandFrame(self, text='Sample Command')

        def new_sample():
            name = tk.simpledialog.askstring('set new sample', "sample name")
            if name is not None and name != '':
                master.sample_frame.add_sample(name+'.csv')

        btn_new_sample = LeftSideButton(sample_cmd_frm, text='New Sample', command=new_sample)

        def pop_sample():
            names = master.sample_frame.get_sample_names()
            name = tk.simpledialog.askstring('pop sample', "sample name")
            if name in names:
                master.sample_frame.pop_sample(name)

        btn_pop_sample = LeftSideButton(sample_cmd_frm, text='Pop Sample', command=pop_sample)

        total_cmd_frm = BaseCommandFrame(self, text='Total Command')

        def start_all():
            tk.messagebox.showinfo('start all', 'All Sample Run Now.')
            pass

        btn_start = LeftSideButton(total_cmd_frm, text='Start All', command=start_all)

        def stop_all():
            tk.messagebox.showinfo('stop all', 'All Sample Stop Now.')
            pass

        btn_stop = LeftSideButton(total_cmd_frm, text='Stop All', command=stop_all)

        ext_frm = BaseCommandFrame(self, text='Ext Command')

        def quit_program():
            tk.messagebox.showinfo('quit', 'quit this program.')
            exit(0)
            pass

        btn_quit = LeftSideButton(ext_frm, text='Quit', command=quit_program)

        def shutdown_machine():
            tk.messagebox.showinfo('shut down', 'shut down only raspberrypi.')
            if OS == LINUX:
                os.system('sudo shutdown -h now')

        btn_shutdown = LeftSideButton(ext_frm, text='Shut Down', command=shutdown_machine)


class BaseCommandFrame(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text, borderwidth=2, relief="solid")
        self.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

