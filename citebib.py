#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse

from citebib import info


def test():
    """
    Idea for the structure
    """
    from citebib.importer import get_bibtex_entries
    from pprint import pprint

    bibfile = 'biblio.bib'
    texfile = 'text.tex'
    bibfile2 = 'a.bib'

    #Load the bibtex
    entries = get_bibtex_entries(bibfile2) 
    pprint(entries)

    reqfield = ('author', 'year')


    #Create a new dir with reqfields only
    new = dict()

    for entry in entries:
        #TODO
        #if entry in tex file:
        tmp = dict()
        for field in entries[entry].keys():
            if field in reqfield:
                tmp[field] = entries[entry][field]

        new[entry] = tmp
    pprint(new)


    #Format the biblio

    #write it!

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    args = parser.parse_args()

    test()
