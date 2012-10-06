#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from writer import print_latex_biblio
from io import StringIO

class TestLatexBiblio(unittest.TestCase):

    @unittest.skip('TO be redone')    
    def test_article(self):

        biblio = {'Carroll1986': {'author': [{'id': 'CarrollBJ', 'name': 'Carroll, B J'}],
                     'journal': {'id': 'Langmuir', 'name': 'Langmuir'},
                     'pages': '248 to 250', 'title': 'Equilibrium conformations of liquid drops on thin cylinders under forces of capillarity. A theory for the roll-up process', 
                     'type': 'article', 'volume': '2', 'year': '1986'}}
       
        out = StringIO()
        style = 'author, journal (year)'
        print_latex_biblio(biblio, style, out=out)
        result = out.getvalue().strip()

        expected = 'B. J. Carroll, Langmuir (1986)' 
        self.assertEqual(result, expected)
