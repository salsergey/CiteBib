#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import sys
from citebib import info


def main(bibfiles, texfiles, format, output=sys.stdout):
    """
    Idea for the structure

    :param bibfiles: list of bibfiles
    :param texfiles: list of texfiles
    :param format: Output format (latex or bibtex)
    :param output: Output file
    """
    from citebib.importer import get_bibtex_entries, get_citations
    from pprint import pprint

    from citebib.config import Configuration, check_default_config

    check_default_config()

    #Load the tex
    citations = []
    for texfile in texfiles:
        citations.extend(get_citations(texfile))
    pprint(citations)

    #Load the bibtex
    entries = {}
    for bibfile in bibfiles:
        entries.update(get_bibtex_entries(bibfile)) 

    #Load configuration
    config = Configuration(format)

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
    pprint(new)


    #write it!
    from citebib.writer import write_bibtex
    from citebib.writer import write_latex
    if format == 'bibtex':
        write_bibtex(new, output)
    elif format == 'latex':
        write_latex(citation, new, config, output) 
    else:
        raise ValueError('Wrong format value')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    parser.add_argument('--latex', help='LateX type output', action='store_true')
    parser.add_argument('-b', metavar='BIBTEX', nargs='+', required=True, help='Bibtex file(s)')
    parser.add_argument('-t', metavar='TEX', nargs='+', required=True, help='Tex file(s)')
    parser.add_argument('-o', metavar='OUTPUT', required=False, help='Output (default: stdout)')
    args = parser.parse_args()

    bibfiles = args.b
    texfiles = args.t
    if args.latex:
        format = 'latex'
    else:
        format = 'bibtex'
    if args.o == None:
        main(bibfiles, texfiles, format)
    else:
        with open(args.o, 'w') as f:
            main(bibfiles, texfiles, format, f)

