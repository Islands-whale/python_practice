#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Circular sorting module '

__author__ = 'Chongsen Zhao'


def cycle_sort(target, begin, step):
    """ 对原列表重新排序生成新列表

    在原列表中从指定位置开始，按照步进每次取出一个元素放入新列表
    并把该元素从原列表中弹出，不参与下次排序

    Args:
        target: 原列表
        begin: 起始位置
        step: 步进

    Returns:
        排序后的新列表

    Raises:
        TypeError: An error occurred accessing wrong data type.
        IndexError: An error occurred accessing invalid index.
    """
    pos = begin - 1
    result = []

    for i in range(len(target)):
        pos = (pos + step - 1) % len(target)
        result.append(target[pos])
        target.pop(pos)

    return result


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
        """Export sales information."""
        print("name:", self.__name, "\tage:", self.__age)


if __name__ == '__main__':

    Person1 = Person("zhangsan", 30)
    Person2 = Person("lisi", 35)
    Person3 = Person("wangwu", 42)
    Person4 = Person("zhouliu", 10)

    original = [Person1, Person2, Person3, Person4]
    print("\nThe sequence before sorting is:\n")
    for i in range(len(original)):
        original[i].print_data()

    try:
        begin = int(input("\nPlease input a starting position:"))
        step = int(input("Please input a step number:"))
    except ValueError:
        print("\nPlease input an integer!")
    else:
        if begin <= 0 or begin > len(original) or step <= 0:
            raise IndexError("Out of range!")

        final = cycle_sort(original, begin, step)
        print("\nThe sequence after sorting is:\n")
        for i in range(len(final)):
            final[i].print_data()

# *=====End File=====* #
