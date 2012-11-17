#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

from citebib.bibtexentry import clean_entry

def write_bibtex(citations, entries, out=sys.stdout):
    """
    Write all entries in filename
    """
    #TODO: we must check if all citations are available as in write_text

    citations.sort()

    block = ''
    for entry in citations:
        try:
            entries[entry]
        except KeyError:
            print("%%Missing entry in bibtex file(s): %s" % entry, file=sys.stderr)
            continue

        block += '@' + str(entries[entry]['type']) + '{' + entry + ','

        #Sort the list of fields
        fields = []
        for field in entries[entry]:
            if field != 'type':
                fields.append(field)
        fields.sort()

        #Add fields content to block
        for field in fields:
            content = clean_entry(field, entries[entry][field], format='bibtex')
            block += "\n\t" + str(field) + ' = {' + content + '},' 
    
        block += '\n}\n\n'
    out.write(block)


def write_text(ordered_list, entries, config, format='latex', out=sys.stdout):
    """
    Print entries to the latex format
    """
    for entry in ordered_list:
        try:
            authors_list_length = config.get_number_authors(entries[entry]['type'])
        except KeyError:
            print("%%Missing entry in bibtex file(s): %s" % entry, file=sys.stderr)
            continue
        authors_list_length = 0 #FIXME: bugs... somewhere
        if format == 'latex':
            out.write('\\bibitem{%s}\n' % entry)
        #Get the style from config
        style = config.get_style(entries[entry]['type'])
        for field in entries[entry]:
            data = clean_entry(field, entries[entry][field], format, number_authors_name=authors_list_length)
            style = re.sub(field, data, style)
        out.write(style)
        out.write('\n')


