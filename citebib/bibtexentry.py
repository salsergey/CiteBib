#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def clean_last_name(name):
    """
    Return a short clean last name
    """
    name = re.sub("\s+", '',name) #remove white spaces
    name = re.sub("([A-Z]*)[^-.]*", "\g<1>", name) #Keep upper case and -
    name = re.sub("^(\w)(\w)$", "\g<1>. \g<2>.", name) # PG -> P. G.
    name = re.sub("^(\w)-(\w)$", "\g<1>.-\g<2>.", name) # P-G -> P.-G.
    name = re.sub("^(\w)$", "\g<1>.", name) # P -> P.
    return name

def get_authors_latex(authors, short=0):
    """ 
    Get a formated author list
    short: max number of authors, others are in 'et al.'
            if == 0, it means infinite

    :param authors: Raw authors list
    :param short: cleaned authors list length
    :returns: string
    """
    if short == 0: #zero means infinite
        author_list = authors
    else:
        author_list = authors[:short]
    
    author_string = ''
    for pos, name in enumerate(author_list):
        name = name['name'].split(',')
        name[1] = clean_last_name(name[1])
        author_string += str(name[1]) + ' ' + str(name[0]) 

        #Separator
        if pos == len(authors) - 2:
            author_string += ' and '
        elif pos == len(authors) - 1:
            pass
        elif pos + 1 < short and short != 0:
            author_string += ', '
        elif short == 0:
            author_string += ', '
    #Add et al if the list is too long...
    if short != 0 and short < len(authors):
        author_string += ' \\textit{et al.}'
    
    return author_string

def get_authors_bibtex(authors):
    """
    Format the authors to the bibtex format

    :param authors: Raw authors list
    :returns: list
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

def clean_entry(field, content, format='bibtex', number_authors_name=0):
    """
    Clean up a field content for a specific format

    :param field: field (like journal, author...)
    :param content: content of the field
    :param format: bibtex or latex.
    :param number_authors_name: Length of the author list (Latex format)
    :returns: String
    """
    if field == 'author':
        if format == 'bibtex':
            return get_authors_bibtex(content)
        elif format == 'latex':
            return get_authors_latex(content, number_authors_name)
        else:
            raise ValueError('Wrong format: %s' % format)
    elif field == 'journal':
        return content['name']
    elif field == 'pages':
        return re.sub('\sto\s', '-', content)
    else:
        return content

