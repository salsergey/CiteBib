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

    ###########
    # BAD USAGE
    ###########
    @unittest.skip('finish this test')
    def test_not_existing_bibfile(self):
        command = ['citebib', '-b', 'tests/data/not_existing.bib', '-t', 'tests/data/doc_article.tex']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()

    @unittest.skip('finish this test')
    def test_not_existing_texfile(self):
        command = ['citebib', '-b', 'tests/data/article.bib', '-t', 'tests/data/not_existing.tex']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()

    @unittest.skip('finish this test')
    def test_not_missingkey_in_bibtex(self):
        command = ['citebib', '-b', 'tests/data/book.bib', '-t', 'tests/data/doc_article.tex']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()


    ###########
    # ARTICLES
    ###########
    def test_article_default(self):
        command = ['citebib', '-b', 'tests/data/article.bib', '-t', 'tests/data/doc_article.tex']
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


    ###########
    # BOOKS
    ###########
    def test_book_default(self):
        command = ['citebib', '-b', 'tests/data/book.bib', '-t', 'tests/data/doc_book.tex']
        process = subprocess.Popen(command, bufsize=4096, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode()
        expected = """@book{Bird1987,
\tauthor = {Bird, R.B. and Armstrong, R.C. and Hassager, O.},
\tpublisher = {Wiley Edition},
\ttitle = {Dynamics of Polymeric Liquid},
\tyear = {1987},
}\n
"""
        self.assertEqual(out, expected)
        self.assertEqual(stderr, None)

