import openpyxl as xl
import csv
import os

REPORT_PATH = os.getcwd()
FILENAME = 'result.xlsx'


def parse_log(log: list):
    log


def report_log():
        _wb = xl.workbook()
        _mainsheet = _wb.active
        _samplesheets = {}
        sample_filelist = os.listdir()
        for sample_file in sample_filelist:
            sample_name = os.path.splitext(sample_file)[0]
            sample_sheet = _wb.create_sheet(sample_name)
            _samplesheets[sample_name] = sample_sheet

            log_data = []
            with open(sample_file,'r') as _file:
                reader = list(csv.reader(_file))

                key = reader.pop(0)
                for row in reader:
                    row_dict = {k:v for k, v in zip(key,row)}
                    log_data.append(row_dict)


