#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from utils import uniq

class TestUniq(unittest.TestCase):
    
    def test_simple_list(self):
        data = ['a', 'b', 'c']
        expected = data
        result = uniq(data)
        self.assertEqual(expected, result)

    def test_complete_list(self):
        data = ['a', 'b', 'c', 'b']
        expected = ['a', 'b', 'c']
        result = uniq(data)
        self.assertEqual(expected, result)
