#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from converter import string_to_latex
class TestLatexConverter(unittest.TestCase):

    def test_accent(self):
        string = 'à é è ö'
        result = string_to_latex(string)
        expected = "\`{a} \\\'{e} \`{e} \\\"{o}"
        self.assertEqual(result, expected)

    def test_accent(self):
        """ Don't touch { and }"""
        string = '{A}'
        result = string_to_latex(string)
        expected = '{A}'
        self.assertEqual(result, expected)
        
from converter import protect_uppercase
class TestUppercaseProtection(unittest.TestCase):

    def test_uppercase(self):
        string = 'A'
        result = protect_uppercase(string)
        expected = '{A}'
        self.assertEqual(result, expected)

    def test_lowercase(self):
        string = 'a'
        result = protect_uppercase(string)
        expected = 'a'
        self.assertEqual(result, expected)
