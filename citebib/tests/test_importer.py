#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    #def test_commented_citations(self):
    #    text = """
    #    I want this one \cite{Foo1999} %but not that one \cite{Bar2000}
    #    """
    #    temp = tempfile.mkstemp()[1] 
    #    with open(temp, 'w') as tmp:
    #        tmp.write(text)

    #    expected = ['Foo1999']
    #    result = get_citations(temp)
    #    self.assertEqual(expected, result)

    #def test_citations_with_option(self):
    #    text = """
    #    \cite[option]{Foo1999}
    #    """
    #    temp = tempfile.mkstemp()[1] 
    #    with open(temp, 'w') as tmp:
    #        tmp.write(text)

    #    expected = ['Foo1999']
    #    result = get_citations(temp)
    #    self.assertEqual(expected, result)
