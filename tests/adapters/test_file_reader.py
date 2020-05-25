#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' File reader test module '

__author__ = 'Chongsen Zhao'

import unittest
import os.path
from src.adapters.file_reader import (ReaderFactory, TxtReader, CsvReader,
                                      ZipReader)


class TestReaderFactory(unittest.TestCase):
    def test_register_reader(self):
        ReaderFactory.register_reader('.txt', TxtReader)
        self.assertEqual(ReaderFactory.strategies['.txt'], TxtReader)

    def test_get_reader(self):
        ReaderFactory.register_reader('.txt', TxtReader)
        reader = ReaderFactory.get_reader('.txt')
        self.assertEqual(reader, TxtReader)


class TestTxtReader(unittest.TestCase):
    def test_init(self):
        reader = TxtReader(r'data\people.txt')
        self.assertEqual(reader.path, r'data\people.txt')

    def test_next(self):
        generator = next(TxtReader(r'data\people.txt'))

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

    def test_bool(self):
        self.assertTrue(os.path.isfile(r'data\people.txt'))
        self.assertFalse(os.path.isfile('xxx.txt'))


class TestCsvReader(unittest.TestCase):
    def test_init(self):
        reader = CsvReader(r'data\people.csv')
        self.assertEqual(reader.path, r'data\people.csv')

    def test_next(self):
        generator = next(CsvReader(r'data\people.csv'))

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

    def test_bool(self):
        self.assertTrue(os.path.isfile(r'data\people.csv'))
        self.assertFalse(os.path.isfile('xxx.csv'))


class TestZipReader(unittest.TestCase):
    def test_init(self):
        reader = ZipReader(r'data\people.zip')
        self.assertEqual(reader.path, r'data\people.zip')

    def test_bool(self):
        self.assertTrue(os.path.isfile(r'data\people.zip'))
        self.assertFalse(os.path.isfile('xxx.zip'))

    def test_get_file_list(self):
        members = ZipReader.get_file_list(r'data\people.zip')
        self.assertEqual(members, ['people.csv', 'people.txt'])

    def test_from_zip(self):
        self.assertFalse(ZipReader.from_zip(r'data\people.zip', 'xxx.txt'))
        generator = ZipReader.from_zip(r'data\people.zip', 'people.txt')

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
