import csv
import datetime
import os

PROJECT_DIR = os.getcwd() + '/'
SAMPLE_FOLDER = "samples/"
SAMPLE_PATH = f"{PROJECT_DIR}{SAMPLE_FOLDER}"
ENCODING = 'UTF-8'

class Sample:
    DEFAULT_KEYS = ['date', 'time', 'log']

    def __init__(self, name):
        self._path:str = f"{PROJECT_DIR}{SAMPLE_FOLDER}{name}.csv"
        self._data:list = []
        self._keys:list = []

        try:
            self.import_file()
        except FileNotFoundError:
            self.new_file()

    def new_file(self):
        self._keys = self.DEFAULT_KEYS

        with open(self._path, 'w',encoding=ENCODING, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self._keys)
        self.add_log_now('log created')

    def import_file(self):
        with open(self._path, 'r',encoding=ENCODING) as f:
            file_data:list = list(csv.reader(f))
            _keys = file_data.pop(0)
            for _values in file_data:
                dict_data = {}
                for k, v in zip(_keys, _values):
                    dict_data[k] = v
                self._data.append(dict_data)

    def export_file(self):
        with open(self._path, 'w',encoding=ENCODING, newline='') as f:
            writer = csv.writer(f)

            category = self._data[0].keys()
            writer.writerow(category)
            for each_data in self._data[1:]:
                writer.writerow(each_data.values())

    def add_log_now(self, log):
        _dt = datetime.datetime.now()
        self.add_log(_dt, log)

    def add_log(self, _dt:datetime.datetime, log):
        date = _dt.strftime('%Y-%m-%d')
        time = _dt.strftime('%H:%M')
        data = [date, time, log]
        dict_data = {}
        for k, v in zip(self._keys, data):
            dict_data[k] = v
        self._data.append(dict_data)
        
        with open(self._path, 'a', encoding=ENCODING, newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, time, log])

    def print_data(self):
        for i in self._data:
            print(i)


if __name__ == '__main__':
    sample = Sample('test')