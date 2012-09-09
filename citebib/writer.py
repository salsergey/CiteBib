#!/usr/bin/env python
# -*- coding: utf-8 -*-




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
                    block += "\n\t" + str(field) + ' = {' + entries[entry][field] + '},' 
    
            block += '\n}\n\n'
        output.write(block)
