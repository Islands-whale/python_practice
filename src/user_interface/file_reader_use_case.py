#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' File reader use cace module '

__author__ = 'Chongsen Zhao'

import os.path
from src.user_interface.file_reader import ReaderFactory, ZipReader


class FileReader:

    def __init__(self, path):
        self.path = path
        self.type = os.path.splitext(path)[-1]
        self.reader = ReaderFactory.get_reader(self.type)

    def check_path(self):
        if self.type not in ['.txt', '.csv', '.zip']:
            return None

        return bool(self.reader(self.path))

    def check_zip(self):
        return self.type == '.zip'

    def from_zip(self, member):
        return ZipReader.from_zip(self.path, member)

    def from_txt_csv(self):
        return next(self.reader(self.path))
