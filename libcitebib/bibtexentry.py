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

import re
from libcitebib.converter import string_to_latex


def clean_last_name(name):
    """
    Return a short clean last name
    """
    name = re.sub("\s+", '', name)  # remove white spaces
    name = re.sub("([A-Z]*)[^-.]*", "\g<1>", name)  # Keep upper case and -
    name = re.sub("^(\w)(\w)$", "\g<1>. \g<2>.", name)  # PG -> P. G.
    name = re.sub("^(\w)-(\w)$", "\g<1>.-\g<2>.", name)  # P-G -> P.-G.
    name = re.sub("^(\w)$", "\g<1>.", name)  # P -> P.
    return name


def get_authors_latex(authors, short=0):
    """
    Get a formated author list
    short: max number of authors, others are in 'et al.'
            if == 0, it means infinite

    :param authors: Raw authors list
    :param short: cleaned authors list length
    :returns: string
    """
    if short == 0:  # zero means infinite
        author_list = authors
    else:
        author_list = authors[:short]

    author_string = ''
    for pos, name in enumerate(author_list):
        name = name.split(',')
        name[1] = clean_last_name(name[1])
        author_string += str(name[1]) + ' ' + str(name[0])

        #Separator
        if pos == len(authors) - 2:
            author_string += ' and '
        elif pos == len(authors) - 1:
            pass
        elif pos + 1 < short and short != 0:
            author_string += ', '
        elif short == 0:
            author_string += ', '
    #Add et al if the list is too long...
    if short != 0 and short < len(authors):
        author_string += ' \\textit{et al.}'

    return author_string


def get_authors_bibtex(authors):
    """
    Format the authors to the bibtex format

    :param authors: Raw authors list
    :returns: list
    """
    author_list = ''
    for num, author in enumerate(authors):
        #TODO process author_list
        name = author.split(',')
        name[1] = clean_last_name(name[1])
        if num != 0:
            author_list += ' and '
        author_list += str(name[0]) + ', ' + str(name[1])

    return author_list


def clean_entry(field, content, format='bibtex', number_authors_name=0):
    """
    Clean up a field content for a specific format

    :param field: field (like journal, author...)
    :param content: content of the field
    :param format: bibtex or latex.
    :param number_authors_name: Length of the author list (Latex format)
    :returns: String
    """

    if field == 'author':
        if format == 'bibtex':
            auth = get_authors_bibtex(content)
            return string_to_latex(auth)
        elif format == 'raw':
            auth = get_authors_latex(content, number_authors_name)
            return auth
        elif format == 'latex':
            auth = get_authors_latex(content, number_authors_name)
            return string_to_latex(auth)
        else:
            raise ValueError('Wrong format: %s' % format)
    elif field == 'title':
        return string_to_latex(content)
    elif field == 'school':
        return string_to_latex(content)
    elif field == 'publisher':
        return string_to_latex(content)
    elif field == 'editor':
        return string_to_latex(content)
    elif field == 'journal':
        return string_to_latex(content)
    elif field == 'pages':
        return re.sub('\sto\s', '--', content)
    else:
        return content
