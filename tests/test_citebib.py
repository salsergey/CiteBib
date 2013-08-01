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
import subprocess

class TestCitebib(unittest.TestCase):

    def test_default(self):
        command = ['citebib', '-b', 'tests/data/article.bib', '-t', 'tests/data/doc.tex']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()
        expected = """@article{Cesar2013,
\tauthor = {C{\\'e}sar, J.},
\tjournal = {Nice Journal},
\tpages = {12--23},
\ttitle = {An amazing title},
\tvolume = {12},
\tyear = {2013},
}\n
"""
        self.assertEqual(out, expected)
        self.assertEqual(stderr, None)

