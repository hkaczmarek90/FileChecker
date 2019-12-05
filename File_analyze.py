import os
from os.path import isfile, join
import sys


class Start:
    def __init__(self, year=None, month=None, start_day=None, end_day=None):
        self._year = year
        self._month = month
        self._start = start_day
        self._end = end_day

    def get_data(self):
        if self._year is None:
            while True:
                y = int(input('Podaj rok dla którego chcesz przygotować raport [YYYY]: '))
                if 2015 <= y <= 2030:
                    self._year = y
                    break
                else:
                    if input('Wprowadzony rok jest błędny - chcesz spóbować jeszcze raz? T/N ?').lower() == 't':
                        True
                    else:
                        sys.exit()
        if self._month is None:
            while True:
                m = int(input('Podaj miesiąc dla którego chcesz przygotować raport[MM]: '))
                if 1 <= m <= 12:
                    self._month = m
                    break
                else:
                    if input('Wprowadzony miesiąc jest błędny - chcesz spóbować jeszcze raz? T/N ?').lower() == 't':
                        True
                    else:
                        sys.exit()

        while True:
            sd = int(input('Podaj pierwszy dzień od którego chcesz rozpocząć raport [DD]: '))
            if 1 <= sd <= 31:
                self._start = sd
                break
            else:
                if input('Wprowadzony dzień jest błędny - chcesz spóbować jeszcze raz? T/N ?').lower() == 't':
                    True
                else:
                    sys.exit()

        while True:
            ed = int(input('Podaj ostatni dzień od którego chcesz rozpocząć raport [DD]: '))
            if 1 <= ed <= 31 and ed >= sd:
                self._end = ed
                break
            else:
                if input('Wprowadzony dzień jest błędny - chcesz spóbować jeszcze raz? T/N ?').lower() == 't':
                    True
                else:
                    sys.exit()

    def get_range(self):
        if self._end is not None and self._start is not None:
            return self._end - self._start
        else:
            sys.exit()


class CreateFileList:
    def __init__(self):
        self.required = []

    def create(self, my_range):
        start = my_range._start
        for i in range(my_range.get_range() + 1):

            if start < 10:
                self.required.append(f'Raport_{my_range._year}-{my_range._month}-0{start}.ods')
                start += 1
            else:
                self.required.append(f'Raport_{my_range._year}-{my_range._month}-{start}.ods')
                start += 1
        return self.required


class CheckFiles:
    def is_not_used(self):
        pass

    def file(self, path):
        self.is_not_used
        onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
        result = sorted(onlyfiles)
        return result


class CompareList:
    def is_not_used(self):
        pass

    def comparison(self, list1, list2):
        self.is_not_used
        my_list = []
        for i in list1:
            if i in list2:
                my_list.append(i + ' OK')
            else:
                my_list.append(i + ' NOK')
        for i in my_list:
            print(i)


dane = Start()
dane.get_data()
report = CreateFileList()
checker = CheckFiles()
result = CompareList()
result.comparison(report.create(dane), checker.file('./'))
