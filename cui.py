import os
from functions.sample import *


class MainProgram:
    def __init__(self):
        self._sample_path = PROJECT_DIR+SAMPLE_FOLDER
        self._samplefiles:list = os.listdir(self._sample_path)
        self._sample_names:list = [os.path.splitext(i)[0] for i in self._samplefiles]

        self._sample_list = {i: Sample(i) for i in self._sample_names}
        
    def start_test(self, sample_name):
        self._sample_list[sample_name].add_log_now('start test')

    def stop_test(self, sample_name):
        self._sample_list[sample_name].add_log_now('stop test')

    def print_samples(self):
        print('samples',self._sample_names,end='\n')

    def print_commands(self):
        print('command list','1.start','2.stop','0.end',end='\n')
        


if __name__ == '__main__':
    mp = MainProgram()
    while True:
        mp.print_samples()
        mp.print_commands()
        cmd = int(input('cmd :'))

        if cmd == 0:
            exit(0)
        elif cmd == 1:
            sp = str(input('sample name :'))
            mp.start_test(sp)
        elif cmd == 2:
            sp = str(input('sample name :'))
            mp.stop_test(sp)