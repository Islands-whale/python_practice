#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus use case test module '

__author__ = 'Chongsen Zhao'

import unittest
from unittest.mock import MagicMock
from src.use_cases.josephus_use_case import JosephusUseCase


class TestJosephusUseCase(unittest.TestCase):

    def test_check_number(self):
        self.assertTrue(JosephusUseCase.check_number('1', '1'))
        self.assertFalse(JosephusUseCase.check_number('1', '-1'))
        self.assertFalse(JosephusUseCase.check_number('1', 'a'))

    def test_create_josephus(self):
        mock = MagicMock()
        mock.__iter__.return_value = [1, 2, 3]
        ring = JosephusUseCase.create_josephus('1', '1', mock)
        self.assertEqual(ring.current_id, 0)
        self.assertEqual(ring.step, 1)
        self.assertEqual(ring._people, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
