#!/usr/bin/env python
# -*- coding: utf-8 -*

import bibtexparser
import re

def string_to_latex(string):
    """
    Convert a string to its latex equivalent
    """
    unicode_to_latex = bibtexparser.BibTexParser.unicode_to_latex
    unicode_to_latex.pop(' ')
    unicode_to_latex.pop('{')
    unicode_to_latex.pop('}')

    new = []
    for pos, char in enumerate(string):
        if char in unicode_to_latex.keys():
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

