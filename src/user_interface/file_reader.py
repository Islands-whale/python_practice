#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' file reader module '

__author__ = 'Chongsen Zhao'

from src.domain.person import Person
import csv
from zipfile import ZipFile
from os.path import splitext, isfile
from typing import Dict


class Reader:
    """基类，定义接口"""

    def __next__(self):
        raise NotImplementedError('my __next__: not implemented!')

    def __bool__(self):
        raise NotImplementedError('my __bool__: not implemented!')


class ReaderFactory:
    """工厂类"""
    strategies: Dict[str, Reader] = {}

    @classmethod
    def get_reader(cls, type: str) -> Reader:
        """类方法:通过type获取具体的策略类"""
        return cls.strategies.get(type)

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

    def __next__(self):
        """
        实现接口，获取数据返回Person对象
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

    def __bool__(self):
        return isfile(self.path)


class CsvReader(Reader):
    """Summary of class here.

    从csv文件中获取数据，创建并返回Person对象

    Attributes:
        path: 文件路径
    """
    def __init__(self, path: str):
        """Constructor."""
        self.path = path

    def __next__(self):
        """
        实现接口
        生成器，获取数据返回Person对象
        """
        with open(self.path) as fp:
            for line in csv.reader(fp):
                name = line[0]
                try:
                    age = int(line[1])
                except ValueError:
                    age = 0
                yield Person(name, age)

    def __bool__(self):
        return isfile(self.path)


class ZipReader:
    """Summary of class here.

    从zip文件中获取目标文件，读取数据创建并返回Person对象

    Attributes:
        path: 文件路径
        member: zip内的成员文件名
    """
    def __init__(self, path: str):
        self.path = path

    def __bool__(self):
        return isfile(self.path)

    @classmethod
    def get_file_list(cls, path):
        with ZipFile(path) as fp:
            return fp.namelist()

    @classmethod
    def from_zip(cls, path, member):
        try:
            with ZipFile(path) as fp:
                file_path = fp.extract(member, 'data')
        except Exception:
            return None

        else:
            file_type = splitext(file_path)[-1]
            reader = ReaderFactory.get_reader(file_type)
            return next(reader(file_path))


"""初始化工厂"""
ReaderFactory.register_reader('.txt', TxtReader)
ReaderFactory.register_reader('.csv', CsvReader)
ReaderFactory.register_reader('.zip', ZipReader)
