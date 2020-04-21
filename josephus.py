#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus sorting module '

__author__ = 'Chongsen Zhao'

from csv import reader
from zipfile import ZipFile
from io import TextIOWrapper
import os

TXT = 0
CSV = 1
ZIP = 2


class Person:
    """Summary of class here.

    人的基本信息，包括姓名、年龄

    Attributes:
        __name: 姓名
        __age: 年龄
    """
    def __init__(self, name, age):
        """Inits SampleClass with blah."""
        self.__name = name
        self.__age = age
        # print("name:", self.__name, ": constructor")

    # def __del__(self):
    #     """Destructor."""
    #     print("name:", self.__name, ": destructor")

    def print_data(self):
        """Export person information."""
        print("name:", self.__name, "\tage:", self.__age)


class RingSort:
    """Summary of class here.

    对约瑟夫环中的Person对象按照起始位置和步进依次抽取

    Attributes:
        people: 容器，元素为Person对象
        id: 容器的索引
        step: 步进
    """
    def __init__(self):
        """constructor."""
        self.people = []
        self.id = 0
        self.step = 1

    def __iter__(self):
        """返回迭代器"""
        return self

    def __next__(self):
        """返回下一个要抽取的Person对象"""
        if len(self.people) == 0:
            raise StopIteration

        self.id = (self.id + self.step - 1) % len(self.people)
        ret = self.people.pop(self.id)
        return ret

    def reset(self, start, step):
        """设置起始位置和步进"""
        self.id = start - 1
        self.step = step

    def append(self, target):
        """容器里添加Person对象"""
        self.people.append(target)

    # def next_yield(self):
    #     """
    #     创建生成器
    #     每次返回一个要抽取的Person对象
    #     """
    #     for i in range(len(self.people)):
    #         self.id = (self.id + self.step - 1) % len(self.people)
    #         ret = self.people.pop(self.id)
    #         yield ret


class ReadFile:
    def __init__(self, path):
        self.path = path

    def get_type(self, path):
        type = os.path.splitext(path)[-1]
        if type == '.txt':
            return TXT

        if type == '.csv':
            return CSV

        if type == '.zip':
            return ZIP

    def read_txt(self):
        result = []
        with open(self.path) as f_txt:
            for line in f_txt:
                if line.count(',') != 1:
                    raise IOError("格式错误")
                result.append(line)
        return result

    def read_csv(self):
        result = []
        with open(self.path) as f_csv:
            data = reader(f_csv)
            for line in data:
                result.append(line)
        return result

    def read_zip(self):
        result = []
        with ZipFile(self.path) as f_zip:
            with TextIOWrapper(f_zip.open(self.path)) as f_csv:
                data = reader(f_csv)
                for line in data:
                    result.append(line)
        return result


if __name__ == '__main__':

    ring = RingSort()
    path = 'people.csv'
    f = ReadFile(path)

    if f.get_type(path) == TXT:
        data = f.read_txt()
        for line in data:
            line = line.strip('\n')
            name = line.split(',')[0]
            age = line.split(',')[1]
            ring.append(Person(name, age))

    if f.get_type(path) == CSV:
        data = f.read_csv()
        for line in data:
            name = line[0]
            age = line[1]
            ring.append(Person(name, age))

    if f.get_type(path) == ZIP:
        data = f.read_zip()
        for line in data:
            name = line[0]
            age = line[1]
            ring.append(Person(name, age))

    try:
        start = int(input("\nPlease input a starting position:"))
        step = int(input("Please input a step number:"))
    except ValueError:
        print("\nPlease input an integer!")
    else:
        if start <= 0 or step <= 0:
            raise IndexError("Out of range!")

        ring.reset(start, step)
        print("\nThe sequence after sorting is:\n")
        for i in ring:
            i.print_data()

# *=====End File=====* #
