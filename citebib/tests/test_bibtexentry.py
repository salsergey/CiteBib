#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from bibtexentry import clean_last_name

class TestCleanLastName(unittest.TestCase):
    
    def test_simple_lastname(self):
        lastname = ' A. '
        expected = 'A.'
        result = clean_last_name(lastname)
        self.assertEqual(expected, result)

    def test_one_long_lastname(self):
        lastname = ' Adrian '
        expected = 'A.'
        result = clean_last_name(lastname)
        self.assertEqual(expected, result)

    def test_one_composed_lastname(self):
        lastname = 'Pierre-Gilles'
        expected = 'P.-G.'
        result = clean_last_name(lastname)
        self.assertEqual(expected, result)

