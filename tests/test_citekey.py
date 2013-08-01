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

class TestCitekey(unittest.TestCase):

    def test_default(self):
        command = ['citekey', 'Cesar2013', '-b', 'tests/data/article.bib']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()
        expected = 'J. César, Nice Journal, 12, 12--23 (2013).\n'
        self.assertEqual(out, expected)
        self.assertEqual(stderr, None)

    def test_latex(self):
        command = ['citekey', '--latex', 'Cesar2013', '-b', 'tests/data/article.bib']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()
        expected = "\\bibitem{Cesar2013}\nJ. C{\\'e}sar, Nice Journal, \\textbf{12}, 12--23 (2013).\n"
        self.assertEqual(out, expected)
        self.assertEqual(stderr, None)




