import tkinter as tk
import tkinter.messagebox
import os
# from ..const_val import *
from frames.const_val import *
from const_val import *
from modules.modules import *


class CommandFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side='top', fill='x', expand=False, padx=FRAME_PAD, pady=FRAME_PAD)

        sample_cmd_frm = BaseCommandFrame(self, text='Sample Command')
        # sample_cmd_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        def new_sample():
            # new = tk.messagebox.askokcancel()
            tl = tk.Toplevel(self)
            tl.resizable(False, False)
            tl.title("setup new sample")
            tl.attributes('-topmost', 'true')

        btn_new_sample = LeftSideButton(sample_cmd_frm, text='New Sample', command=new_sample)
        # btn_new_sample = tk.Button(sample_cmd_frm, text='New Sample', command=new_sample)
        # btn_new_sample.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        def pop_sample():
            tl = tk.Toplevel(self)
            tl.resizable(False, False)
            tl.title("pop sample")
            tl.attributes('-topmost', 'true')

        btn_pop_sample = LeftSideButton(sample_cmd_frm, text='Pop Sample', command=pop_sample)
        # btn_pop_sample.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        total_cmd_frm = BaseCommandFrame(self, text='Total Command')
        # total_cmd_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        def start_all():
            tk.messagebox.showinfo('start all', 'All Sample Run Now.')
            pass

        btn_start = LeftSideButton(total_cmd_frm, text='Start All', command=start_all)
        # btn_start = tk.Button(total_cmd_frm, text='Start All', command=start_all)
        # btn_start.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        def stop_all():
            tk.messagebox.showinfo('stop all', 'All Sample Stop Now.')
            pass

        btn_stop = LeftSideButton(total_cmd_frm, text='Stop All', command=stop_all)
        # btn_stop.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        ext_frm = BaseCommandFrame(self, text='Ext Command')
        # ext_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        def quit_program():
            tk.messagebox.showinfo('quit', 'quit this program.')
            exit(0)
            pass

        btn_quit = LeftSideButton(ext_frm, text='Quit', command=quit_program)
        # btn_quit.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        def shutdown_machine():
            tk.messagebox.showinfo('shut down', 'shut down only raspberrypi.')
            if OS == LINUX:
                os.system('sudo shutdown -h now')

        btn_shutdown = LeftSideButton(ext_frm, text='Shut Down', command=shutdown_machine)
        # btn_shutdown.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        # btn_start_all = tk.Button(self, text='Start')
        # btn_start_all.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)


class BaseCommandFrame(tk.LabelFrame):
    def __init__(self, master, text):
        super().__init__(master, text=text, borderwidth=2, relief="solid")
        self.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)