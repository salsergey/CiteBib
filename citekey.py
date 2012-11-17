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


import argparse
import sys
from citebib import info


def main(bibfiles, citations, format):
    """
    Idea for the structure

    :param bibfiles: list of bibfiles
    :param citations: list of citations
    :param format: Output format (latex or bibtex)
    :param output: Output file
    """
    from citebib.importer import get_bibtex_entries
    from citebib.config import ConfigFormat, check_default_config

    check_default_config()

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
            for field in entries[entry].keys():
                #If the field is requested
                if field in config.get_reqfields(tmp['type']):
                    tmp[field] = entries[entry][field]
            #Push the entry
            new[entry] = tmp


    #write it!
    from citebib.writer import write_text

    output = sys.stdout
    if format == 'latex' or format == 'raw':
        write_text(citations, new, config, format, output) 
    else:
        raise ValueError('Wrong format value')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    parser.add_argument('--latex', help='LateX type output', action='store_true')
    parser.add_argument('-c', metavar='CONFIG', required=False, help='Configuration file with bibtex paths')
    parser.add_argument('-b', metavar='BIBTEX', nargs='*', required=False, help='Bibtex file(s)')
    parser.add_argument('keys', metavar='KEY', nargs='+', help='Bibtex key(s)')
    args = parser.parse_args()

    bibfiles = args.b

    from citebib.config import ConfigBibtex

    if bibfiles is None:
        if args.c is not None:
            import os.path
            location, name = os.path.split(args.c)
            bib = ConfigBibtex(name, location)
        else:
            bib = ConfigBibtex()
        bibfiles = bib.get_bibtex_paths()

    if args.latex:
        format = 'latex'
    else:
        format = 'raw'
    main(bibfiles, args.keys, format)

