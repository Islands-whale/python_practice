#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus use case test module '

__author__ = 'Chongsen Zhao'

import unittest
from src.use_cases.josephus_use_case import JosephusUseCase


class TestJosephusUseCase(unittest.TestCase):

    def test_check_number(self):
        self.assertTrue(JosephusUseCase.check_number('1', '1'))
        self.assertFalse(JosephusUseCase.check_number('1', '-1'))
        self.assertFalse(JosephusUseCase.check_number('1', 'a'))

    def test_create_josephus(self):
        ring = JosephusUseCase.create_josephus('1', '1', ['a', 'b'])
        self.assertEqual(ring.current_id, 0)
        self.assertEqual(ring.step, 1)
        self.assertEqual(ring._people, ['a', 'b'])


if __name__ == '__main__':
    unittest.main()
