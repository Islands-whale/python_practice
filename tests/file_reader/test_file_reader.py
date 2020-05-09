#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.file_reader import file_reader as fil


class TestReaderFactory(unittest.TestCase):
    def test_register_reader(self):
        fil.ReaderFactory.register_reader('.txt', fil.TxtReader)
        self.assertEqual(fil.ReaderFactory.strategies['.txt'], fil.TxtReader)

    def test_get_reader(self):
        fil.ReaderFactory.register_reader('.txt', fil.TxtReader)
        reader = fil.ReaderFactory.get_reader('.txt')
        self.assertEqual(reader, fil.TxtReader)


class TestTxtReader(unittest.TestCase):
    def test_init(self):
        obj = fil.TxtReader(r'data\people.txt')
        self.assertEqual(obj.path, r'data\people.txt')

    def test_next(self):
        generator = fil.TxtReader(r'data\people.txt').next()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


class TestCsvReader(unittest.TestCase):
    def test_init(self):
        obj = fil.CsvReader(r'data\people.csv')
        self.assertEqual(obj.path, r'data\people.csv')

    def test_next(self):
        generator = fil.CsvReader(r'data\people.csv').next()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


class TestZipReader(unittest.TestCase):
    def test_init(self):
        obj = fil.ZipReader(r'data\people.zip', 'people.txt')
        self.assertEqual(obj.path, r'data\people.zip')
        self.assertEqual(obj.member, 'people.txt')

    def test_get_member_data(self):
        generator = fil.ZipReader(r'data\people.zip',
                                  'people.txt').get_member_data()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


if __name__ == '__main__':
    unittest.main()
