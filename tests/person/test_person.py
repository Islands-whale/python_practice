#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.person import person as per


class TestPerson(unittest.TestCase):
    def test_init(self):
        obj = per.Person('Jorn', 25)
        self.assertEqual(obj._name, 'Jorn')
        self.assertEqual(obj._age, 25)
        self.assertTrue(isinstance(obj, per.Person))


if __name__ == '__main__':
    unittest.main()
