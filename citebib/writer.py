#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

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


def print_latex_biblio(entries, out=sys.stdout):
    """
    Print entries to the latex format
    """

    #TODO should depend on filetype !
    #Example here for an article...
    separator = ', '
    for entry in entries:
        line = ''
        line += clean_entry('author', entries[entry]['author'], format='latex')
        line += separator
        line += clean_entry('journal', entries[entry]['journal'], format='latex')
        line += ' (' + clean_entry('year', entries[entry]['year'], format='latex') + ')'

        out.write(line)
