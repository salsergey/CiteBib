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

from libcitebib.utils import uniq

class TestUniq(unittest.TestCase):

    def test_simple_list(self):
        data = ['a', 'b', 'c']
        expected = data
        result = uniq(data)
        self.assertEqual(expected, result)

    def test_complete_list(self):
        data = ['a', 'b', 'c', 'b']
        expected = ['a', 'b', 'c']
        result = uniq(data)
        self.assertEqual(expected, result)
