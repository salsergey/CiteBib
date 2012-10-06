#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

from citebib.bibtexentry import clean_entry

def write_bibtex(entries, filename):
    """
    Write all entries in filename
    """
    with open(filename, 'w') as output:
        block = ''
        for entry in entries:
            block += '@' + str(entries[entry]['type']) + '{' + entry + ','
            for field in entries[entry]:
                if field != 'type':
                    content = clean_entry(field, entries[entry][field], format='bibtex')
                    block += "\n\t" + str(field) + ' = {' + content + '},' 
    
            block += '\n}\n\n'
        output.write(block)


def print_latex_biblio(entries, config, out=sys.stdout):
    """
    Print entries to the latex format
    """

    for entry in entries:
        #Get the style from config
        style = config.get_style(entries[entry]['type'])
        for field in entries[entry]:
            data = clean_entry(field, entries[entry][field], format='latex')
            style = re.sub(field, data, style)
        out.write(style)
        out.write('\n')
