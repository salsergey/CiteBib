#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse

from citebib import info




def main(bibfile, texfile, output):
    """
    Idea for the structure
    """
    from citebib.importer import get_bibtex_entries, get_citations
    from pprint import pprint


    from citebib.bibtexentry import clean_entry




    #Load the tex
    citations = get_citations(texfile)
    pprint(citations)

    #Load the bibtex
    entries = get_bibtex_entries(bibfile) 

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
                    tmp[field] = clean_entry(field, entries[entry][field], format='bibtex') #FIXME format
            #Push the entry
            new[entry] = tmp
    pprint(new)


    #write it!
    from citebib.writer import write_bibtex
    write_bibtex(new, output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=info.SHORT_DESCRIPTION,
                             epilog='')
    parser.add_argument('--version', action='version', version=info.NAME + ' ' + info.VERSION) 
    args = parser.parse_args()

    bibfile = 'biblio.bib'
    texfile = 'text.tex'
    bibfile2 = 'a.bib'
    output = '/tmp/toto'
    #TODO list of files for bibfile, texfile...
    main(bibfile, texfile, output)
