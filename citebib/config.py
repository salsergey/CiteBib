#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
import os

def load_config(format, name='default', location='~/.citebib'):
    """
    Load a configuration

    :param format: biblio format (latex or bibtex)
    :param name: name of the configuration
    :param location:
    :returns: the configuration
    """
    filename = str(name) + '.ini'
    filepath = os.path.join(os.path.expanduser(location), format, filename)

    config = configparser.ConfigParser()
    config.read(filepath)
    return config #FIXME not a good idea...

def check_default_config(location='~/.citebib'):
    """
    Check if default configuration files exists.
    If it does not, create them
    """
    formats = ('latex', 'bibtex')
    for format in formats:
        path = os.path.join(os.path.expanduser(location), format)
        if not os.path.exists(path):
            os.makedirs(path)
        file = os.path.join(path, 'default.ini')
        if not os.access(file, os.F_OK):
            write_default_config(file, format)

def write_default_config(inifile, format):
    """
    This function is a wrapper to write default config files


    :param inifile: ini file name
    :param format: biblio format (latex or bibtex)
    """
    if format == 'latex':
        _write_default_config_latex(inifile)
    elif format == 'bibtex':
        _write_default_config_bibtex(inifile)
    else:
        raise ValueError('Wrong format: %s' % format)


def _write_default_config_latex(inifile):
    """
    Write a default configuration file for latex

    :param inifile: ini file name
    """
    fields = {
        'article' : ('author, journal (year)'),  
    }

    config = configparser.ConfigParser()


    for entry in fields:
        content = {'format': fields[entry], 'authorlength': 2} #TODO
        config[entry] = content


    with open(inifile, 'w') as configfile:
        config.write(configfile)


def _write_default_config_bibtex(inifile):
    """
    Write a default configuration file for bibtex

    :param inifile: ini file name
    """
    reqfields = {
        'article' : ('author', 'title', 'journal', 'volume', 'year', 'pages'),
        'book' : ('author', 'editor', 'title', 'publisher', 'year'),
        'booklet' : ('title'),
        'conference' : ('author', 'title', 'booktitle', 'year'),
        'inproceedings' : ('author', 'title', 'booktitle', 'year'),
        'inbook' : ('author', 'editor', 'title', 'chapter', 'pages', 'publisher', 'year'),
        'incollection' : ('author', 'title', 'bookpublisher', 'year'),
        'manual' : ('title'),
        'mastersthesis' : ('author', 'title', 'school', 'year'),
        'misc' : (''),
        'phdthesis' : ('author', 'title', 'school', 'year'),
        'proceedings' : ('title', 'year'),
        'techreport' : ('author', 'title', 'institution', 'year')
        }
    fields = ('author', 'editor', 'publisher', 'bookpublisher', 
            'title', 'booktitle', 'journal', 'volume', 'year', 'pages', 'institution')
    config = configparser.ConfigParser()

    content = {}
    for el in reqfields:
        for field in fields:
            if field in reqfields[el]:
                content.update({field: True})
            else:
                content.update({field: False})
        config[el] = content

    with open(inifile, 'w') as configfile:
        config.write(configfile)



if __name__ == '__main__':
    #write_default_config_latex('latex.ini')
    #write_default_config_bibtex('bibtex.ini')
    check_default_config()
    print(load_config('bibtex'))