#!/usr/bin/env python3            -------------->在Windows、Unix-like(mac/linux/unix)上均可运行
# -*- coding: utf-8 -*-           -------------->文件编码格式 UTF-8

' Book sales information module '

__author__ = 'Chongsen Zhao'

from josephus_sort import cycle_sort


class SalesData:
    """Summary of class here.

    书籍的销售情况，包括书籍的编号、销售单价以及销售量

    Attributes:
        __book_no: 书籍编号
        __units_sold: 销售量
        __unit_price: 单价
    """

    def __init__(self, book_no, units_sold, unit_price):
        """Inits SampleClass with blah."""
        self.__book_no = book_no
        self.__units_sold = units_sold
        self.__unit_price = unit_price
        # print("ISBN:", self.__book_no, ": constructor")

    # def __del__(self):
    #     """Destructor."""
    #     print("ISBN:", self.__book_no, ": destructor")

    def print_data(self):
        """Export sales information."""
        print("ISBN:", self.__book_no, "\tUnits_sold:", self.__units_sold,
              "\tUnit_price:", self.__unit_price)


if __name__ == '__main__':

    data1 = SalesData("999-1", 111, 45)
    data2 = SalesData("999-2", 222, 30)
    data3 = SalesData("999-3", 333, 22)
    data4 = SalesData("999-4", 444, 10)

    original = [data1, data2, data3, data4]
    print("\nThe sequence before sorting is:\n")
    for i in range(len(original)):
        original[i].print_data()

    try:
        begin = int(input("\nPlease input a starting position:"))
        step = int(input("Please input a step number:"))
    except TypeError:
        print("\nPlease input an integer!")
    else:
        if begin <= 0 or begin > len(original) or step <= 0:
            raise IndexError("Out of range!")

        final = cycle_sort(original, begin, step)
        print("\nThe sequence after sorting is:\n")
        for i in range(len(final)):
            final[i].print_data()

# *=====End File=====* #
