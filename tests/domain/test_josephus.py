#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' RingSort test module '

__author__ = 'Chongsen Zhao'

import unittest
from unittest.mock import MagicMock
from src.domain.josephus import RingSort


class TestRingSort(unittest.TestCase):

    def setUp(self):
        mock = MagicMock()
        mock.__iter__.return_value = [1, 2, 3]
        self.ring = RingSort(1, 1, mock)

    def test_init(self):
        self.assertEqual(self.ring.current_id, 0)
        self.assertEqual(self.ring.step, 1)
        self.assertEqual(self.ring._people, [1, 2, 3])

    def test_len(self):
        self.assertEqual(len(self.ring), 3)

    def test_lt(self):
        self.assertTrue(self.ring < 4)

    def test_append(self):
        self.ring.append(4)
        self.assertEqual(self.ring._people, [1, 2, 3, 4])

    def test_iter(self):
        self.assertEqual(iter(self.ring), self.ring)

    def test_next(self):
        self.assertEqual(next(self.ring), 1)
        self.assertEqual(next(self.ring), 2)
        self.assertEqual(next(self.ring), 3)

        with self.assertRaises(StopIteration):
            next(self.ring)


if __name__ == '__main__':
    unittest.main()
