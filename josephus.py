#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus sorting module '

__author__ = 'Chongsen Zhao'

from csv import reader
from zipfile import ZipFile, ZipExtFile
from io import TextIOWrapper
from os.path import splitext

NUMBER_IN_ZIP = 0


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


class RingSort:
    """Summary of class here.

    对约瑟夫环中的Person对象按照起始位置和步进依次抽取

    Attributes:
        _people: 元素为Person对象的容器
        current_id: 容器中要剔除数据的索引
        step: 步进
    """
    def __init__(self, start, step):
        """constructor."""
        self._people = []
        self.current_id = start - 1
        self.step = step

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

    @classmethod
    def create_from_txt(cls, path):
        """从txt文件中提取数据，创建并返回类的对象"""
        obj = cls(start, step)
        with open(path) as f_txt:
            for line in f_txt:
                line = line.split()
                obj.append(Person(name=line[0], age=line[1]))
        return obj

    @classmethod
    def create_from_csv(cls, path):
        """从csv文件中提取数据，创建并返回类的对象"""
        obj = cls(start, step)
        with open(path) as f_csv:
            if isinstance(f_csv, ZipExtFile):
                f_csv = TextIOWrapper(f_csv)
            data = reader(f_csv)
            for line in data:
                obj.append(Person(name=line[0], age=line[1]))
        return obj

    @classmethod
    def create_from_zip(cls, path):
        """从zip文件中提取数据，创建并返回类的对象"""
        with ZipFile(path) as f_zip:
            path_in_zip = f_zip.namelist()[NUMBER_IN_ZIP]
            obj = RingSort.create_from_csv(path_in_zip)
        return obj


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
        extension_name = splitext(path)[-1]

        if extension_name == '.txt':
            ring = RingSort.create_from_txt(path)

        if extension_name == '.csv':
            ring = RingSort.create_from_csv(path)

        if extension_name == '.zip':
            ring = RingSort.create_from_zip(path)

        print("\nThe sequence after sorting is:\n")
        for i in ring:
            i.print_data()

# *=====End File=====* #
