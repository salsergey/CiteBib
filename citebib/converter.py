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

import citebib.bibtexparser as bibtexparser
import re

def string_to_latex(string):
    """
    Convert a string to its latex equivalent
    """
    unicode_to_latex = bibtexparser.BibTexParser.unicode_to_latex
    escape = [' ', '{', '}']

    new = []
    for pos, char in enumerate(string):
        if char in escape:
            new.append(char)
        elif char in unicode_to_latex.keys():
            new.append(unicode_to_latex[char])
        else:
            new.append(char)
    return ''.join(new)

def protect_uppercase(string):
    """
    Protect uppercase letters for bibtex

    :param string: string to convert
    :returns: string
    """
    string = re.sub("([A-Z])", '{\g<1>}', string)
    return string 

