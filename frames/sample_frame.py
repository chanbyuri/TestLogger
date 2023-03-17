import tkinter as tk
from tkinter import ttk
from frames.const_val import *
from modules.modules import *
from functions.sample import *

SAMPLES: list = ['SB180-A', 'SB181-A', 'SB250-A', 'SB251-A', 'SE018-A(1600RPM)']


class SampleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=FRAME_PAD, pady=FRAME_PAD, fill='both', expand=True)

        scroll = ttk.Scrollbar(self,orient='horizontal')
        scroll.pack(side='bottom', fill='x')

        samplelist = os.listdir(SAMPLE_PATH)
        for i in SAMPLES:
            EachSampleFrame(self,i)



class EachSampleFrame(tk.LabelFrame):
    def __init__(self, master, sample_name):
        super().__init__(master, text=sample_name, borderwidth=2, relief="solid", width=100)
        self.pack(side="left", fill='both', expand=True, padx=FRAME_PAD, pady=FRAME_PAD)

        self._start_time = tk.StringVar()
        self._stop_time = tk.StringVar()
        self._routine_second = tk.IntVar()
        self._is_testing = tk.BooleanVar()
        self._total_test_time = tk.IntVar()
        self._total_cycle = tk.IntVar()

        cmd_frm = BaseElementFrame(self)

        def start_test():
            pass

        def stop_test():
            pass

        def setup_sample():
            pass

        start_btn = LeftSideButton(cmd_frm, text='start', command=start_test)
        stop_btn = LeftSideButton(cmd_frm, text='stop', command=stop_test)
        setup_btn = LeftSideButton(cmd_frm, text='part', command=setup_sample)
        run_led = LedCanvas(cmd_frm)

        start_date_frm = BaseElementFrame(self)

        lbl = LeftSideLabel(start_date_frm, text='start date')
        start_date_txt = tk.StringVar(value='hi')
        etr = LeftSideEntry(start_date_frm, "readonly", start_date_txt)

        stop_date_frm = BaseElementFrame(self)

        lbl = LeftSideLabel(stop_date_frm, text='stop date')
        stop_date_txt = tk.StringVar(value='bye')
        etr = LeftSideEntry(stop_date_frm, "readonly", stop_date_txt)

        start_time_frm = BaseElementFrame(self)

        lbl = LeftSideLabel(start_time_frm, text='start time')
        start_time_txt = tk.StringVar(value='9:00')
        etr = LeftSideEntry(start_time_frm, "readonly", start_time_txt)

        stop_time_frm = BaseElementFrame(self)

        lbl = LeftSideLabel(stop_time_frm, text='stop time')
        stop_time_txt = tk.StringVar(value='18:00')
        etr = LeftSideEntry(stop_time_frm, "readonly", stop_time_txt)


class BaseElementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=1, relief="solid")
        self.pack(fill='x', padx=CHILD_PAD, pady=CHILD_PAD)
