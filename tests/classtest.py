#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' class test module '

__author__ = 'Chongsen Zhao'

from src.josephus import Person
from src.josephus import ReaderFactory
from src.josephus import TxtReader
from src.josephus import CsvReader
from src.josephus import ZipReader
from src.josephus import RingSort
import unittest


class TestPerson(unittest.TestCase):
    def test_init(self):
        obj = Person('Jorn', 25)
        self.assertEqual(obj._name, 'Jorn')
        self.assertEqual(obj._age, 25)
        self.assertTrue(isinstance(obj, Person))


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
        obj = TxtReader(r'data\people.txt')
        self.assertEqual(obj.path, r'data\people.txt')

    def test_next(self):
        generator = TxtReader(r'data\people.txt').next()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


class TestCsvReader(unittest.TestCase):
    def test_init(self):
        obj = CsvReader(r'data\people.csv')
        self.assertEqual(obj.path, r'data\people.csv')

    def test_next(self):
        generator = CsvReader(r'data\people.csv').next()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


class TestZipReader(unittest.TestCase):
    def test_init(self):
        obj = ZipReader(r'data\people.zip', 'people.txt')
        self.assertEqual(obj.path, r'data\people.zip')
        self.assertEqual(obj.member, 'people.txt')

    def test_get_member_data(self):
        generator = ZipReader(r'data\people.zip',
                              'people.txt').get_member_data()

        person = generator.__next__()
        self.assertEqual(person._name, 'Jorn')
        self.assertEqual(person._age, 25)

        person = generator.__next__()
        self.assertEqual(person._name, 'Tom')
        self.assertEqual(person._age, 30)


class TestRingSort(unittest.TestCase):
    def test_init(self):
        obj = RingSort(1, 2, ['Jorn'])
        self.assertEqual(obj.current_id, 0)
        self.assertEqual(obj.step, 2)
        self.assertEqual(obj._people[0], 'Jorn')

    def test___next__(self):
        obj = RingSort(1, 3, [0, 1, 2, 3])
        self.assertEqual(obj.__next__(), 2)
        self.assertEqual(obj.__next__(), 1)


if __name__ == '__main__':
    unittest.main()
