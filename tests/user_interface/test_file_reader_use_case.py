#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' File reader use case test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.user_interface.file_reader_use_case import FileReader
from src.user_interface.file_reader import TxtReader


class TestFileReader(unittest.TestCase):

    def test_init(self):
        self.obj = FileReader(r'data\people.txt')
        self.assertEqual(self.obj.path, r'data\people.txt')
        self.assertEqual(self.obj.type, '.txt')
        self.assertEqual(self.obj.reader, TxtReader)

    def test_check_path(self):
        self.assertTrue(FileReader(r'data\people.txt').check_path())
        self.assertFalse(FileReader('datapeople.txt').check_path())
        self.assertFalse(FileReader('datapeople').check_path())

    def test_check_type(self):
        self.assertTrue(FileReader(r'data\people.zip').check_type())
        self.assertFalse(FileReader(r'data\people.txt').check_type())
        self.assertFalse(FileReader(r'data\people.csv').check_type())

    def test_from_zip(self):
        self.assertFalse(FileReader(r'data\people.zip').from_zip('people.tt'))
        generator = FileReader(r'data\people.zip').from_zip('people.txt')

        person = next(generator)
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = next(generator)
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)

        person = next(generator)
        self.assertEqual(person._name, 'Jerry')
        self.assertEqual(person._age, 35)

        person = next(generator)
        self.assertEqual(person._name, 'Mike')
        self.assertEqual(person._age, 40)

        with self.assertRaises(StopIteration):
            next(generator)

    def test_from_txt_csv(self):
        generator = FileReader(r'data\people.txt').from_txt_csv()

        person = next(generator)
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = next(generator)
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)

        person = next(generator)
        self.assertEqual(person._name, 'Jerry')
        self.assertEqual(person._age, 35)

        person = next(generator)
        self.assertEqual(person._name, 'Mike')
        self.assertEqual(person._age, 40)

        with self.assertRaises(StopIteration):
            next(generator)


if __name__ == '__main__':
    unittest.main()
