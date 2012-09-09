#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
def clean_last_name(name):
    name = re.sub("\s+", '',name) #remove white spaces
    name = re.sub("([A-Z])[^-.]*", "\g<1>", name) #Keep upper case and -
    name = re.sub("^(\w)(\w)$", "\g<1>. \g<2>.", name) # PG -> P. G.
    name = re.sub("^(\w)-(\w)$", "\g<1>.-\g<2>.", name) # P-G -> P.-G.
    name = re.sub("^(\w)$", "\g<1>.", name) # P -> P.
    return name



def get_authors(authors, short=0):
    """ 
    Get a formated author list
    short: max number of authors, others are in 'et al.'
            if == 0, it means infinite
    """
    if short == 0: #zero means infinite
        author_list = authors
    else:
        author_list = authors[:short]
    
    author_string = ''
    for name in author_list:
        name = author['name'].split(',')
        name[1] = clean_last_name(name[1])
        author_string += str(name[0]) + ', ' + str(name[1]) #TODO need separator
    if short != 0 and short < len(authors):
        author_string += 'et al.'
    
    return author_string

def get_authors_bibtex(authors):
    """

    """
    author_list = ''
    for num, author in enumerate(authors):
        #TODO process author_list
        name = author['name'].split(',')
        name[1] = clean_last_name(name[1])
        if num != 0 :
            author_list += ' and '
        author_list += str(name[0]) + ', ' + str(name[1])

    return author_list




def clean_entry(field, content):
    """
    
    """
    if field == 'author':
        #TODO or the other one...
        return get_authors_bibtex(content)
    else:
        return content

