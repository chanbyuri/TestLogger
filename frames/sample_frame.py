import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
from frames.const_val import *
from modules.modules import *
from functions.sample import *


class SampleFrame(tk.Canvas):
    def __init__(self, master, samples:list):
        self._samples = {}
        super().__init__(master)
        self.pack(padx=FRAME_PAD, pady=FRAME_PAD, fill='both', expand=True)
        scroll = ttk.Scrollbar(self, orient='horizontal', command=self.xview)
        scroll.pack(side='bottom', fill='x')

        for i in samples:
            self.add_sample(i)

    def add_sample(self, name):
        new_sample_frame = EachSampleFrame(self, name)
        self._samples[name] = new_sample_frame

    def pop_sample(self, name):
        self._samples[name].destroy()
        self._samples.pop(name)

    def get_sample_names(self):
        return self._samples


class EachSampleFrame(tk.LabelFrame):
    def __init__(self, master, sample_name):
        self._sample = Sample(sample_name)

        super().__init__(master, text=sample_name, borderwidth=2, relief="solid")
        self.pack(side="left", fill='y', padx=FRAME_PAD, pady=FRAME_PAD)

        self._cmd_frm = CommandFrame(self, self._sample)


class BaseElementFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, borderwidth=1, relief="solid")
        self.pack(fill='x', padx=CHILD_PAD, pady=CHILD_PAD)


class CommandFrame(BaseElementFrame):
    def __init__(self, master, sample):
        super().__init__(master)
        self._sample = sample

        self._start_btn = LeftSideButton(self, text='start', command=self.start_test)
        self._stop_btn = LeftSideButton(self, text='stop', command=self.stop_test)
        self._log_btn = LeftSideButton(self, text='log', command=self.logging)

        if self._sample.is_running() == True:
            self._start_btn['state'] = tk.DISABLED
            self._stop_btn['state'] = tk.NORMAL
            self._log_btn['state'] = tk.DISABLED
        elif self._sample.is_running() == False:
            self._start_btn['state'] = tk.NORMAL
            self._stop_btn['state'] = tk.DISABLED
            self._log_btn['state'] = tk.NORMAL

    def start_test(self):
        date, time = self._sample.add_log_now("start test")
        InformationFrame(self.master, 'start test', [date, time])
        self._start_btn['state'] = tk.DISABLED
        self._stop_btn['state'] = tk.NORMAL
        self._log_btn['state'] = tk.DISABLED

    def stop_test(self):
        date, time = self._sample.add_log_now("stop test")
        InformationFrame(self.master, 'stop test', [date, time])
        self._start_btn['state'] = tk.NORMAL
        self._stop_btn['state'] = tk.DISABLED
        self._log_btn['state'] = tk.NORMAL

    def logging(self):
        log = tk.simpledialog.askstring('write log', 'new log')
        if log == '' or log is None:
            return
        date, time = self._sample.add_log_now(log)
        InformationFrame(self.master, log, [date, time])
        pass


class InformationFrame(BaseElementFrame):
    def __init__(self, master, text, _dt):
        super().__init__(master)

        LeftSideLabel(self, text)
        LeftSideEntry(self, "readonly", _dt)
