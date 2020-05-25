#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Person test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.domain.person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('Jorn', 25)

    def test_init(self):
        self.assertEqual(self.person._name, 'Jorn')
        self.assertEqual(self.person._age, 25)
        self.assertTrue(isinstance(self.person, Person))

    def test_str(self):
        self.assertEqual(str(self.person), 'name:Jorn\tage:25')


if __name__ == '__main__':
    unittest.main()
