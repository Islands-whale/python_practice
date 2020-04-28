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
    def __init__(self, name, age):
        """Inits SampleClass with blah."""
        self._name = name
        self._age = age
        # print("name:", self._name, ": constructor")

    # def __del__(self):
    #     """Destructor."""
    #     print("name:", self._name, ": destructor")

    def print_data(self):
        """Export person information."""
        print("name:", self._name, "\tage:", self._age)


class FileReader:
    """Summary of class here.

    读取文件中的数据，并将数据放进列表中

    Attributes:
        path: 文件路径
    """
    def __init__(self, path):
        self.path = path

    def read_txt(self):
        result = []
        with open(self.path) as fp:
            for line in fp:
                lst = line.split()
                result.append(lst)
        return result

    def read_csv(self):
        result = []
        with open(self.path) as fp:
            data = reader(fp)
            for line in data:
                result.append(line)
        return result

    def read_zip(self, member):
        with ZipFile(self.path) as fp:
            file_path = fp.extract(member)

            obj = FileReader(file_path)
            extension_name = splitext(file_path)[-1]

            if extension_name == '.txt':
                return obj.read_txt()
            if extension_name == '.csv':
                return obj.read_csv()
        return obj


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
                self._people.append(Person(name=each[0], age=each[1]))

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


if __name__ == '__main__':

    try:
        start = int(input("\nPlease input a starting position:"))
        step = int(input("Please input a step number:"))
    except ValueError:
        print("\nPlease input an integer!")
    else:
        if start <= 0 or step <= 0:
            raise IndexError("Out of range!")

        path = 'people.zip'

        target_file = FileReader(path)
        file_data = target_file.read_zip('people.csv')

        ring = RingSort(start, step, file_data)

        print("\nThe sequence after sorting is:\n")
        for i in ring:
            i.print_data()

# *=====End File=====* #
