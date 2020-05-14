#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' file reader module '

__author__ = 'Chongsen Zhao'

import curses
from src.josephus.josephus import Person, Reader, RingSort
from csv import reader
from zipfile import ZipFile
from os.path import splitext
from typing import Iterator, Dict


class ReaderFactory:
    """工厂类"""
    strategies: Dict[str, Reader] = {}

    @classmethod
    def get_reader(cls, type: str) -> Reader:
        """类方法:通过type获取具体的策略类"""
        reader = cls.strategies.get(type)
        if not reader:
            raise ValueError(type)
        return reader

    @classmethod
    def register_reader(cls, strategy_type: str, strategy: Reader):
        """类方法:注册策略类型"""
        if strategy_type == '':
            raise Exception('strategyType can not be null')
        cls.strategies[strategy_type] = strategy


class TxtReader(Reader):
    """Summary of class here.

    从txt文件中获取数据，创建并返回Person对象

    Attributes:
        path: 文件路径
    """
    def __init__(self, path: str):
        """Constructor."""
        self.path = path

    def next(self) -> Iterator[Person]:
        """
        实现接口
        生成器，获取数据返回Person对象
        """
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
    """Summary of class here.

    从csv文件中获取数据，创建并返回Person对象

    Attributes:
        path: 文件路径
    """
    def __init__(self, path: str):
        """Constructor."""
        self.path = path

    def next(self) -> Iterator[Person]:
        """
        实现接口
        生成器，获取数据返回Person对象
        """
        with open(self.path) as fp:
            for line in reader(fp):
                name = line[0]
                try:
                    age = int(line[1])
                except ValueError:
                    age = 0
                yield Person(name, age)


class ZipReader:
    """Summary of class here.

    从zip文件中获取目标文件，读取数据创建并返回Person对象

    Attributes:
        path: 文件路径
        member: zip内的成员文件名
    """
    def __init__(self, path: str, member: str):
        """Constructor."""
        self.path = path
        self.member = member

    def get_member_data(self):  #
        """获取文件数据返回Person对象"""
        with ZipFile(self.path) as fp:
            file_path = fp.extract(self.member, 'data')
            file_type = splitext(file_path)[-1]

            reader = ReaderFactory.get_reader(file_type)
            return reader(file_path).next()


def init_strategies():
    """初始化工厂"""
    ReaderFactory.register_reader('.txt', TxtReader)
    ReaderFactory.register_reader('.csv', CsvReader)


if __name__ == '__main__':

    init_strategies()
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    cursor_y = 3

    try:
        screen.addstr(0, 0, "Please input a starting position:",
                      curses.color_pair(1))
        start = int(screen.getstr())
        screen.addstr(1, 0, "Please input a step number:",
                      curses.color_pair(1))
        step = int(screen.getstr())
    except ValueError:
        print("Please input integer!")
    else:
        if start <= 0 or step <= 0:
            raise IndexError("Out of range!")

        file_reader = TxtReader(r'data\people.txt').next()
        ring = RingSort(start, step, file_reader)

        # file_reader = CsvReader(r'data\people.csv').next()
        # ring = RingSort(start, step, file_reader)

        # file_reader = ZipReader(r'data\people.zip',
        #                         'people.csv').get_member_data()
        # ring = RingSort(start, step, file_reader)

        # file_reader = ZipReader(r'data\people.zip',
        #                         'people.txt').get_member_data()
        # ring = RingSort(start, step, file_reader)

        screen.addstr(3, 0, "The sequence after sorting is:",
                      curses.color_pair(2))
        for i in ring:
            cursor_y += 1
            screen.addstr(cursor_y, 0, i.get_information(),
                          curses.color_pair(2))
    finally:
        screen.addstr(curses.LINES - 1, 0,
                      "Please press any key to continue...",
                      curses.color_pair(3))
        screen.getkey()
        curses.endwin()
