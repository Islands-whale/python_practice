#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class Person module '

__author__ = 'Chongsen Zhao'


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
