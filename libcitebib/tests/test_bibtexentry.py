#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Author: Francois Boulogne <fboulogne at sciunto dot org>, 2012

import unittest

from libcitebib.bibtexentry import clean_last_name

class TestCleanLastName(unittest.TestCase):

    def test_simple_lastname(self):
        lastname = ' A '
        expected = 'A.'
        result = clean_last_name(lastname)
        self.assertEqual(expected, result)

    def test_souble_lastname(self):
        lastname = ' AB '
        expected = 'A. B.'
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



from libcitebib.bibtexentry import get_authors_latex as get_authors

class TestGetAuthor(unittest.TestCase):

    def test_one_author(self):
        authors = ['Foo, J']
        expected = 'J. Foo'
        result = get_authors(authors)
        self.assertEqual(expected, result)

    def test_two_authors(self):
        authors = ['Foo, J', 'Bar, R']
        expected = 'J. Foo and R. Bar'
        result = get_authors(authors)
        self.assertEqual(expected, result)


    def test_simple_list(self):
        authors = ['Foo, J', 'Bar, R', 'Foobar, D']
        expected = 'J. Foo, R. Bar, and D. Foobar'
        result = get_authors(authors)
        self.assertEqual(expected, result)

    def test_short_list(self):
        authors = ['Foo, J', 'Bar, R', 'Foobar, D']
        expected = 'J. Foo, et al.'
        result = get_authors(authors, 1)
        self.assertEqual(expected, result)


from libcitebib.bibtexentry import get_authors_bibtex

class TestGetAuthorBibtex(unittest.TestCase):

    def test_simple_list(self):
        authors = ['Foobar, D']
        expected = 'Foobar, D.'
        result = get_authors_bibtex(authors)
        self.assertEqual(expected, result)

    def test_simple_list2(self):
        authors = ['Foo, D', 'Bar, B']
        expected = 'Foo, D. and Bar, B.'
        result = get_authors_bibtex(authors)
        self.assertEqual(expected, result)
