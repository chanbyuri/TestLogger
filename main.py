import os
import csv
import tkinter as tk
import tkinter.ttk as ttk

TITLE = "TestLogger"
VERSION = "0.1"
FRAME_PAD = 10
CHILD_PAD = 5
ENCODING = 'UTF-8'

SAMPLES:list = ['SB180-A', 'SB181-A', 'SB250-A', 'SB251-A', 'SE018-A(1600RPM)']


class MainProgram(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(TITLE+VERSION)
        # self.attributes('-fullscreen',True)
        self.geometry("1280x720+0+0")

        # with open('Samples_info.csv','r',encoding=ENCODING) as sample_file:
        #     csv.reader(sample_file)
        self._sample_frame_list = []

        cmd_frame = CommandFrame(self)
        sample_frame = SampleFrame(self)
        # for _sample in SAMPLES:
        #     sp_frm = SampleFrame(self,_sample)
        #     self._sample_frame_list.append(sp_frm)
        self.mainloop()


class CommandFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(side='top', fill='x', expand=False, padx=FRAME_PAD, pady=FRAME_PAD)

        sample_cmd_frm = tk.LabelFrame(self, text='Sample Command', borderwidth=2, relief='solid')
        sample_cmd_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        btn_new_sample = tk.Button(sample_cmd_frm, text='New Sample')
        btn_new_sample.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        btn_pop_sample = tk.Button(sample_cmd_frm, text='Pop Sample')
        btn_pop_sample.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        total_cmd_frm = tk.LabelFrame(self, text='Total Command', borderwidth=2, relief='solid')
        total_cmd_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        btn_start = tk.Button(total_cmd_frm, text='Start All')
        btn_start.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        btn_stop = tk.Button(total_cmd_frm, text='Stop All')
        btn_stop.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        os_frm = tk.LabelFrame(self, text='Os Command', borderwidth=2, relief='solid')
        os_frm.pack(side='left', padx=FRAME_PAD, pady=FRAME_PAD)

        btn_quit = tk.Button(os_frm, text='Quit')
        btn_quit.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        btn_shutdown = tk.Button(os_frm, text='Shut Down')
        btn_shutdown.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)

        # btn_start_all = tk.Button(self, text='Start')
        # btn_start_all.pack(side='left', padx=CHILD_PAD, pady=CHILD_PAD)


class SampleFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=FRAME_PAD, pady=FRAME_PAD, fill='both', expand=True)

        scroll = ttk.Scrollbar(self)
        scroll.pack(side='bottom', fill='x')



        for _sample in SAMPLES:
            new_sample_frm = EachSampleFrame(self, _sample)


class EachSampleFrame(tk.LabelFrame):
    def __init__(self, master, samplename):
        super().__init__(master, text=samplename, borderwidth=2, relief="solid")
        self.pack(side="left", fill='both', expand=True, padx=FRAME_PAD, pady=FRAME_PAD)

        lbl = tk.Label(self, text='each Sample Info')
        lbl.pack(side='top', padx=CHILD_PAD, pady=CHILD_PAD)

if __name__ == '__main__':
    mainProgram = MainProgram()