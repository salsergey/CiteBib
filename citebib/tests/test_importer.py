#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import tempfile

from importer import get_citations

class TestGetCitations(unittest.TestCase):


    def test_citations(self):
        
        text = """
        \cite{Foo1999}
        \cite{Foo1999, Bar2012}
        
        \cite{Here1999} blah \cite{There2012}

        """
        temp = tempfile.mkstemp()[1] 
        with open(temp, 'w') as tmp:
            tmp.write(text)

        expected = ['Foo1999', 'Bar2012', 'Here1999', 'There2012']
        result = get_citations(temp)
        self.assertEqual(expected, result)
