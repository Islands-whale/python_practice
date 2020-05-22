#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' file reader module '

__author__ = 'Chongsen Zhao'

from src.josephus.josephus import Person, Reader
from csv import reader
from zipfile import ZipFile
from os.path import splitext
from typing import Dict


class ReaderFactory:
    """工厂类"""
    strategies: Dict[str, Reader] = {}

    @classmethod
    def get_reader(cls, type: str) -> Reader:
        """类方法:通过type获取具体的策略类"""
        reader = cls.strategies.get(type)
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
        self.open_temp = True
        self.fp = None

    def __iter__(self):
        return self

    def __next__(self):
        """
        实现接口，获取数据返回Person对象
        """
        try:
            if self.open_temp:
                self.fp = open(self.path)
                self.open_temp = False
        except Exception:
            return None
        else:
            line = next(self.fp)
            if not line:
                self.fp.close()
                self.open_temp = True
                raise StopIteration
            lst = line.split()
            name = lst[0]
            try:
                age = int(lst[1])
            except ValueError:
                age = 0
            return Person(name, age)


class CsvReader(Reader):
    """Summary of class here.

    从csv文件中获取数据，创建并返回Person对象

    Attributes:
        path: 文件路径
    """
    def __init__(self, path: str):
        """Constructor."""
        self.path = path
        self.open_temp = True
        self.fp = None

    def __iter__(self):
        return self

    def __next__(self):
        """
        实现接口
        生成器，获取数据返回Person对象
        """
        try:
            if self.open_temp:
                self.fp = open(self.path)
                self.open_temp = False
        except Exception:
            return None
        else:
            line = next(reader(self.fp))
            if not line:
                self.fp.close()
                self.open_temp = True
                raise StopIteration
            name = line[0]
            try:
                age = int(line[1])
            except ValueError:
                age = 0
            return Person(name, age)


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

    def next(self):  #
        """获取文件数据返回Person对象"""
        try:
            with ZipFile(self.path) as fp:
                file_path = fp.extract(self.member, 'data')
                file_type = splitext(file_path)[-1]

                reader = ReaderFactory.get_reader(file_type)
                return reader(file_path)
        except Exception:
            return None


"""初始化工厂"""
ReaderFactory.register_reader('.txt', TxtReader)
ReaderFactory.register_reader('.csv', CsvReader)
