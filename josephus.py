#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus sorting module '

__author__ = 'Chongsen Zhao'

from csv import reader
from zipfile import ZipFile
from os.path import splitext


class Person:
    """Summary of class here.

    人的基本信息，包括姓名、年龄

    Attributes:
        _name: 姓名
        _age: 年龄
    """
    def __init__(self, name, age: int):
        """Inits SampleClass with blah."""
        self._name = name
        if age < 0:
            raise ValueError('Age can not be less than 0!')
        self._age = age
        # print("name:", self._name, ": constructor")

    # def __del__(self):
    #     """Destructor."""
    #     print("name:", self._name, ": destructor")

    def print_data(self):
        """Export person information."""
        print("name:", self._name, "\tage:", self._age)


class ReaderFactory:
    strategies = {}

    @classmethod
    def get_reader(cls, type):
        reader = cls.strategies.get(type)
        if not reader:
            raise ValueError(type)
        return reader

    @classmethod
    def register_reader(cls, strategy_type, strategy):
        if strategy_type == '':
            raise Exception('strategyType can not be null')
        cls.strategies[strategy_type] = strategy


class Reader:
    def next(self):
        raise NotImplementedError('my next: not implemented!')


class TxtReader(Reader):
    def __init__(self, path):
        self.path = path

    def next(self) -> Person:
        with open(self.path) as fp:
            for line in fp:
                lst = line.split()
                name = lst[0]
                try:
                    age = int(lst[1])
                except ValueError:
                    age = 0
                yield Person(name, age)


class CsvReader(Reader):
    def __init__(self, path):
        self.path = path

    def next(self) -> Person:
        with open(self.path) as fp:
            for line in reader(fp):
                name = line[0]
                try:
                    age = int(line[1])
                except ValueError:
                    age = 0
                yield Person(name, age)


class ZipReader:
    def __init__(self, path, member):
        self.path = path
        self.member = member

    def get_member(self):
        with ZipFile(self.path) as fp:
            file_path = fp.extract(self.member)
            file_type = splitext(file_path)[-1]

            reader = ReaderFactory.get_reader(file_type)
            return reader(file_path).next()


class RingSort:
    """Summary of class here.

    对约瑟夫环中的Person对象按照起始位置和步进依次抽取

    Attributes:
        _people: 元素为Person对象的容器
        current_id: 容器中要剔除数据的索引
        step: 步进
    """
    def __init__(self, start, step, reader=None):
        """constructor."""
        self._people = []
        self.current_id = start - 1
        self.step = step

        if reader:
            for each in reader:
                self._people.append(each)

    def append(self, target):
        """容器里添加Person对象"""
        self._people.append(target)

    def __iter__(self):
        """返回迭代器"""
        return self

    def __next__(self):
        """返回下一个要抽取的Person对象"""
        if len(self._people) == 0:
            raise StopIteration

        self.current_id = (self.current_id + self.step - 1) % len(self._people)
        ret = self._people.pop(self.current_id)
        return ret


def init_strategies():
    ReaderFactory.register_reader('.txt', TxtReader)
    ReaderFactory.register_reader('.csv', CsvReader)


if __name__ == '__main__':

    init_strategies()

    try:
        start = int(input("\nPlease input a starting position:"))
        step = int(input("Please input a step number:"))
    except ValueError:
        print("\nPlease input an integer!")
    else:
        if start <= 0 or step <= 0:
            raise IndexError("Out of range!")

        # file_reader = TxtReader('people.txt').next()
        # ring = RingSort(start, step, file_reader)

        # file_reader = CsvReader('people.csv').next()
        # ring = RingSort(start, step, file_reader)

        file_reader = ZipReader('people.zip', 'people.csv').get_member()
        ring = RingSort(start, step, file_reader)

        # file_reader = ZipReader('people.zip', 'people.txt').get_member()
        # ring = RingSort(start, step, file_reader)

        print("\nThe sequence after sorting is:\n")
        for i in ring:
            i.print_data()

# *=====End File=====* #
