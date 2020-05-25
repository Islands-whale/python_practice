#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' person module '

__author__ = 'Chongsen Zhao'


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

    def __str__(self) -> str:
        """Get person information."""
        information = 'name:' + self._name + '\tage:' + str(self._age)
        return information
