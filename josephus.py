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


if __name__ == "__main__":
    original = ['a', 'b', 'c', 'd']
    final = cycle_sort(original, 2, 2)
    print(final)

# *=====End File=====* #
