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
import tempfile

from importer import get_citations

class TestGetCitations(unittest.TestCase):


    def test_simple_citations(self):

        text = """
        \cite{Foo1999}

        \cite{Here1999} blah \cite{There2012}

        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999', 'Here1999', 'There2012']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_multiple_citations(self):
        text = """
        \cite{Foo1999, Bar2012}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999', 'Bar2012']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_uniq_citations(self):
        text = """
        \cite{Foo1999}
        \cite{Bar2012}
        \cite{Foo1999}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999', 'Bar2012']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_commented_citations(self):
        text = """
        I want this one \cite{Foo1999} %but not that one \cite{Bar2000}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_citations_with_option(self):
        text = """
        \cite[option]{Foo1999}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_natbib(self):
        text = """
        \citet{t90}
        \citep{p90}
        \citet*{tstar90}
        \citep*{pstar90}

        \citealt{alt90}
        \citealp{alp90}
        \citealt*{altstar90}
        \citealp*{alpstar90}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['t90', 'p90', 'tstar90', 'pstar90', 'alt90', 'alp90', 'altstar90', 'alpstar90']
        result = get_citations(temp)
        self.assertEqual(expected, result)

    def test_natbib_1option(self):
        text = """
        \citet[opt]{t90}
        \citep[opt]{p90}
        \citet*[opt]{tstar90}
        \citep*[opt]{pstar90}

        \citealt[opt]{alt90}
        \citealp[opt]{alp90}
        \citealt*[opt]{altstar90}
        \citealp*[opt]{alpstar90}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['t90', 'p90', 'tstar90', 'pstar90', 'alt90', 'alp90', 'altstar90', 'alpstar90']
        result = get_citations(temp)
        self.assertEqual(expected, result)


    @unittest.skip("Not yet implemented!")
    def test_natbib_2options(self):
        text = """
        \citep[opt][]{p90}
        \citep[opt][opt2]{p290}
        """
        temp = tempfile.mkstemp()[1]
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['p90', 'p290']
        result = get_citations(temp)
        self.assertEqual(expected, result)


