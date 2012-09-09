#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse

from citebib import info




def test():
    """
    Idea for the structure
    """
    from citebib.importer import get_bibtex_entries, get_citations
    from pprint import pprint


    from citebib.bibtexentry import clean_entry



    bibfile = 'biblio.bib'
    texfile = 'text.tex'
    bibfile2 = 'a.bib'

    #Load the tex
    citations = get_citations(texfile)
    pprint(citations)

    #Load the bibtex
    entries = get_bibtex_entries(bibfile) 
    #pprint(entries)

    reqfield = ('author', 'year')


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
                if field in reqfield:
                    tmp[field] = clean_entry(field, entries[entry][field])
            #Push the entry
            new[entry] = tmp
    pprint(new)


    #write it!
    from citebib.writer import write_bibtex
    write_bibtex(new, '/tmp/toto')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    args = parser.parse_args()

    test()
