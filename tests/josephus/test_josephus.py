#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.josephus import josephus as jos


class TestRingSort(unittest.TestCase):
    def test_init(self):
        obj = jos.RingSort(1, 2, ['Jorn'])
        self.assertEqual(obj.current_id, 0)
        self.assertEqual(obj.step, 2)
        self.assertEqual(obj._people[0], 'Jorn')

    def test___next__(self):
        obj = jos.RingSort(1, 3, [0, 1, 2, 3])
        self.assertEqual(obj.__next__(), 2)
        self.assertEqual(obj.__next__(), 1)


if __name__ == '__main__':
    unittest.main()
