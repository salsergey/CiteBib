#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse

from citebib import info


def main(bibfiles, texfiles, format, output):
    """
    Idea for the structure

    :param bibfiles: list of bibfiles
    :param texfiles: list of texfiles
    :param format: Output format (latex or bibtex)
    :param output: Output file
    """
    from citebib.importer import get_bibtex_entries, get_citations
    from pprint import pprint

    #Load the tex
    citations = []
    for texfile in texfiles:
        citations.extend(get_citations(texfile))
    pprint(citations)

    #Load the bibtex
    entries = {}
    for bibfile in bibfiles:
        entries.update(get_bibtex_entries(bibfile)) 

    reqfields = {
        'article' : ('author', 'title', 'journal', 'volume', 'year', 'pages'),
        'book' : ('author','editor','title','publisher','year'),
        'booklet' : ('title'),
        'conference' : ('author','title','booktitle','year'),
        'inproceedings' : ('author','title','booktitle','year'),
        'inbook' : ('author','editor','title','chapter','pages','publisher','year'),
        'incollection' : ('author','title','bookpublisher','year'),
        'manual' : ('title'),
        'mastersthesis' : ('author','title','school','year'),
        'misc' : (),
        'phdthesis' : ('author','title','school','year'),
        'proceedings' : ('title','year'),
        'techreport' : ('author','title','institution','year')
        }


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
                if field in reqfields[tmp['type']]:
                    tmp[field] = entries[entry][field]
            #Push the entry
            new[entry] = tmp
    pprint(new)


    #write it!
    from citebib.writer import write_bibtex
    #TODO depend on format
    write_bibtex(new, output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    parser.add_argument('-b', metavar='BIBTEX', nargs='+', required=True, help='Bibtex file(s)')
    parser.add_argument('-t', metavar='TEX', nargs='+', required=True, help='Tex file(s)')
    parser.add_argument('-o', metavar='OUTPUT', required=False, help='Output')
    args = parser.parse_args()

    #TODO If no output... 
    output = '/tmp/toto'

    bibfiles = args.b
    texfiles = args.t
    format = 'bibtex'
    main(bibfiles, texfiles, format, output)
