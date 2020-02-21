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

import sys
import re

from libcitebib.bibtexentry import clean_entry


def write_bibtex(citations, entries, out=sys.stdout):
    """
    Write bibliography in a bibtex format

    :param citations: a list of keys
    :param entries: list of a list containing all data
    :param out: output
    """
    citations.sort()

    block = ''
    for entry in citations:
        try:
            entries[entry]
        except KeyError:
            print("%%Missing entry in bibtex file(s): %s" % entry, file=sys.stderr)
            continue

        block += '@' + str(entries[entry]['ENTRYTYPE']) + '{' + entry + ','

        #Sort the list of fields
        fields = []
        for field in entries[entry]:
            if field != 'ENTRYTYPE':
                fields.append(field)
        fields.sort()

        #Add fields content to block
        for field in fields:
            content = clean_entry(field, entries[entry][field], format='bibtex')
            block += "\n\t" + str(field) + ' = {' + content + '},'

        block += '\n}\n\n'
    out.write(block)


def write_text(ordered_list, entries, config, format='latex', out=sys.stdout):
    """
    Write bibliography in a text format

    :param ordered_list: a list of ordered keys. The order is conserved.
    :param entries: list of a list containing all data
    :param config:
    :param format: style format: latex or raw
    :param out: output
    """
    for entry in ordered_list:
        try:
            authors_list_length = config.get_number_authors(entries[entry]['ENTRYTYPE'])
        except KeyError:
            print("%%Missing entry in bibtex file(s): %s" % entry, file=sys.stderr)
            continue
        if format == 'latex':
            out.write('\\bibitem{%s}\n' % entry)
        #Get the style from config
        style = config.get_style(entries[entry]['ENTRYTYPE'])
        for field in entries[entry]:
            data = clean_entry(field, entries[entry][field], format, number_authors_name=authors_list_length)
            style = re.sub(field, data, style)
        out.write(style)
        out.write('\n')
