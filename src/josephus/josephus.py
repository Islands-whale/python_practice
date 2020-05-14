#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus sorting module '

__author__ = 'Chongsen Zhao'

from typing import Iterator


class Person:
    """Summary of class here.

    人的基本信息，包括姓名、年龄

    Attributes:
        _name: 姓名
        _age: 年龄
    """
    def __init__(self, name: str, age: int):
        """Inits SampleClass with blah."""
        self._name = name
        if age < 0:
            raise ValueError('Age can not be less than 0!')
        self._age = age
        # print("name:", self._name, ": constructor")

    # def __del__(self):
    #     """Destructor."""
    #     print("name:", self._name, ": destructor")

    def get_information(self) -> str:
        """Get person information."""
        information = 'name:' + self._name + '\tage:' + str(self._age)
        return information


class Reader:
    """基类"""
    def next(self):
        """定义接口"""
        raise NotImplementedError('my next: not implemented!')


class RingSort:
    """Summary of class here.

    对约瑟夫环中的Person对象按照起始位置和步进依次抽取

    Attributes:
        _people: 元素为Person对象的容器
        current_id: 容器中要剔除数据的索引
        step: 步进
    """
    def __init__(self, start: int, step: int, reader: Iterator[Person] = None):
        """constructor."""
        self._people = []
        self.current_id = start - 1
        self.step = step

        if reader:
            for each in reader:
                self._people.append(each)

    def append(self, target: Person):
        """容器里添加Person对象"""
        self._people.append(target)

    def __iter__(self):
        """返回迭代器"""
        return self

    def __next__(self) -> Person:
        """返回下一个要抽取的Person对象"""
        if len(self._people) == 0:
            raise StopIteration

        self.current_id = (self.current_id + self.step - 1) % len(self._people)
        ret = self._people.pop(self.current_id)
        return ret
