#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:35:35 2020

@author: TakahiroKurokawa
"""

import unittest

class TestFunc(unittest.TestCase):
    def test_func(self):
        from hello import func
        self.assertIsNone(func("こんにちは"))