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

from libcitebib.importer import get_bibtex_entries
from libcitebib.config import ConfigFormat


def main(bibfiles, citations, format, output=sys.stdout):
    """
    Idea for the structure

    :param bibfiles: list of bibfiles
    :param citations: list of citations
    :param format: Output format (latex or bibtex)
    :param output: Output file
    """

    #Load the bibtex
    entries = {}
    for bibfile in bibfiles:
        entries.update(get_bibtex_entries(bibfile))

    #Load configuration
    config = ConfigFormat(format)

    #Create a new dir with reqfields only
    new = dict()

    for entry in entries:
        citekey = entries[entry]['id']
        #If the key is in the tex file
        if citekey in citations:
            tmp = dict()
            tmp['type'] = entries[entry]['type']
            try:
                req_field = config.get_reqfields(tmp['type'])
            except ValueError as e:
                output.write('% ' + str(e) + '\n')
            else:
                for field in entries[entry].keys():
                    #If the field is requested
                    if field in req_field:
                        tmp[field] = entries[entry][field]
                #Push the entry
                new[entry] = tmp

    #write it!
    if format == 'bibtex':
        from libcitebib.writer import write_bibtex
        write_bibtex(citations, new, output)
    elif format == 'latex' or format == 'raw':
        from libcitebib.writer import write_text
        write_text(citations, new, config, format, output)
    else:
        raise ValueError('Wrong format value')
