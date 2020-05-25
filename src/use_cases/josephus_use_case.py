#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Josephus use cace module '

__author__ = 'Chongsen Zhao'

from src.domain.josephus import RingSort


class JosephusUseCase():

    @classmethod
    def check_number(cls, start_str, step_str):
        try:
            start = int(start_str)
            step = int(step_str)
        except ValueError:
            return None
        else:
            if start > 0 and step > 0:
                return True

            return None

    @classmethod
    def create_josephus(cls, start, step, reader):
        return RingSort(int(start), int(step), reader)
