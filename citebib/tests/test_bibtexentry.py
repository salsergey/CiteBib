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



#from bibtexentry import get_authors
#
#class TestGetAuthor(unittest.TestCase):
#
#    def test_simple_list(self):
#        authors = [{'name': 'Foo, J', 'id': 'FooJ'}, {'name': 'Bar R', 'id': 'BarR'}, {'name': 'Foobar, D', 'id': 'FoobarD'}]
#        expected = 'Foo, J. and Bar, R. and Foobar, D.'
#        result = get_authors(authors)
#        self.assertEqual(expected, result)

from bibtexentry import get_authors_bibtex

class TestGetAuthor(unittest.TestCase):

    def test_simple_list(self):
        authors = [{'name': 'Foobar, D', 'id': 'FoobarD'}]
        expected = 'Foobar, D.'
        result = get_authors_bibtex(authors)
        self.assertEqual(expected, result)

    def test_simple_list2(self):
        authors = [{'name': 'Foo, D', 'id': 'FooD'}, {'name': 'Bar, B', 'id': 'BarB'}]
        expected = 'Foo, D. and Bar, B.'
        result = get_authors_bibtex(authors)
        self.assertEqual(expected, result)
