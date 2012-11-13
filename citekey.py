#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
    from citebib.importer import get_bibtex_entries, get_citations
    from pprint import pprint

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
    #pprint(new)


    #write it!
    from citebib.writer import write_bibtex
    from citebib.writer import write_latex

    output=sys.stdout
    if format == 'latex' or format == 'raw':
        write_latex(citations, new, config, format, output) 
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

