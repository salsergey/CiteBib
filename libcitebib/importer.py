#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Author: Francois Boulogne <fboulogne at sciunto dot org>, 2012

import re
from bibtexparser import BibTexParser, getnames

from libcitebib.utils import uniq

def _custumize(record):
    """
    This function curstumizes record for bibtex.
    See bibtexparser lib for more info.
    """
    if "author" in record:
        if record["author"]:
            record["author"] = getnames([i.strip() for i in record["author"].replace('\n', ' ').split(" and ")])
    return(record)

def _get_citations(texfilename):
    """
    Get all citations in a tex file.
    Citations may appear several times.

    :param texfilename: tex file path
    :returns: a list of citations
    """

    with open(texfilename, 'r') as tex:
        #it seems that extra spaces in cite with multiple refs
        #works with bibtex, but not recommanded as said on wikipedia

        #Catch citations
        cite = re.compile('cite(|t|p|t\*|p\*|alt|alp|alt\*|alp\*)({|\[.+?\]{)((\w|-|,|\s)+)}') #Can contain spaces?
        allcite = []

        for line in tex:
            #handle commented lines or parts
            line = line.split('%')[0]

            #we get citations
            results = cite.findall(line)
            if results:
                # loop on all results for the line
                for el in results:
                    #sometimes, cite contains several citations
                    foo = re.sub("\s", "", str(el[2])) #remove extra spaces
                    foo = re.split(",", foo)
                    allcite.extend(foo)
    return allcite

def get_citations(texfilenames):
    """
    Get all citations in tex files
    Citations appear only once.

    :param texfilenames: tex files path
    :returns: a list of citations
    """
    allcite = []
    for texfilename in texfilenames:
       allcite.extend(_get_citations(texfilename))
    #uniqify the list
    #A set could not be used since the order might have a sense
    allcite = uniq(allcite)
    return allcite


def get_bibtex_entries(filename):
    """
    Parse a bibtex file and return the content

    :param filename: bibtex filepath
    :returns: a dictionnary; key=ID, content=entry
    """
    with open(filename, 'r') as bibfile:
        biblio = BibTexParser(bibfile, customisation=_custumize)
    entries = biblio.get_entry_list()

    entries_hash = {}
    for entry in entries:
        entries_hash[entry['id']] = entry

    return entries_hash
