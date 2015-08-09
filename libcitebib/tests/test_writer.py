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

from libcitebib.writer import write_text
from io import StringIO

class TestLatexBiblio(unittest.TestCase):

    @unittest.skip('TO be redone')
    def test_article(self):

        biblio = {'Carroll1986': {'author': [{'ID': 'CarrollBJ', 'name': 'Carroll, B J'}],
                     'journal': {'ID': 'Langmuir', 'name': 'Langmuir'},
                     'pages': '248 to 250', 'title': 'Equilibrium conformations of liquid drops on thin cylinders under forces of capillarity. A theory for the roll-up process',
                     'ENTRYTYPE': 'article', 'volume': '2', 'year': '1986'}}

        out = StringIO()
        style = 'author, journal (year)'
        write_text(biblio, style, out=out)
        result = out.getvalue().strip()

        expected = 'B. J. Carroll, Langmuir (1986)'
        self.assertEqual(result, expected)
