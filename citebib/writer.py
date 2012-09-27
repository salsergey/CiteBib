#!/usr/bin/env python
# -*- coding: utf-8 -*-

from citebib.bibtexentry import clean_entry

def write_bibtex(entries, filename):
    """
    Write all entries in filename
    """
    with open(filename, 'w') as output:
        block = ''
        for entry in entries:
            block += '@' + str(entries[entry]['type']) + '{'
            for field in entries[entry]:
                if field != 'type':
                    content = clean_entry(field, entries[entry][field], format='bibtex')
                    block += "\n\t" + str(field) + ' = {' + content + '},' 
    
            block += '\n}\n\n'
        output.write(block)


def print_latex_biblio(entries):
    """
    Print entries to the latex format
    """

    for entry in entries:
        line = ''
        line += clean_entry('author', entries[entry]['author'], format='latex')

        print(line)
