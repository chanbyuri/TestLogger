import csv
import datetime
import os

PROJECT_DIR = os.getcwd() + '/'
SAMPLE_FOLDER = "samples"
# SAMPLE_PATH = f"{PROJECT_DIR}{SAMPLE_FOLDER}/"
SAMPLE_PATH = f"{SAMPLE_FOLDER}/"
ENCODING = 'UTF-8'


class Sample:
    DEFAULT_KEYS = ['date', 'time', 'log']

    def __init__(self, name):
        self._path:str = f"{SAMPLE_PATH}{name}"
        self._data:list = []
        self._keys:list = []

        try:
            self.import_file()
        except FileNotFoundError:
            self.new_file()

    def new_file(self):
        self._keys = self.DEFAULT_KEYS

        with open(self._path+'.csv', 'w',encoding=ENCODING, newline='') as f:
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
        return _dt

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

    def get_start_datetime(self):
        return self._get_data('log created', True)

    def get_last_stop_test(self):
        return self._get_data('stop test')

    def get_last_start_test(self):
        return self._get_data('start test')

    def _get_data(self, log, updown: bool = False):
        with open(self._path, 'r', encoding=ENCODING, newline='') as f:
            reader = list(csv.reader(f))
            if updown == False:
                #upside to down
                reader = reader.reverse()
            for row in reader:
                if row[self.DEFAULT_KEYS[-1]] == log:
                    return row
        return [None, None, None]


if __name__ == '__main__':
    sample = Sample('test')