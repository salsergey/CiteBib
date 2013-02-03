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


import configparser
import os


class ConfigBibtex():
    """
    Load bitex files from configuration files
    :param name: name of the configuration
    :param location: path of the config directory
    """
    def __init__(self, name='bibtex.conf', location='~/.citebib'):
        filename = str(name)
        filepath = os.path.join(os.path.expanduser(location), filename)

        self.config = configparser.ConfigParser()
        self.config.read(filepath)

    def get_bibtex_paths(self):
        """
        Get a list containing paths of bibtex files
        """
        paths = []
        for section in self.config.sections():
            path = os.path.expanduser(self.config[section].get('path'))
            paths.append(path)
        return paths


class ConfigFormat():
    """
    Load custom formats from configuration files

    :param format: biblio format (raw, latex or bibtex)
    :param name: name of the configuration
    :param location: path of the config directory
    :returns: the configuration
    """
    def __init__(self, format, name='default.conf', location='~/.citebib'):
        self.format = format
        filename = str(name)
        filepath = os.path.join(os.path.expanduser(location), str(format), filename)

        self.config = configparser.ConfigParser()
        self.config.read(filepath)

    def get_reqfields(self, section):
        """
        Return required fields

        :param section: Section of the config file
        :returns: list
        """
        if self.format == 'bibtex':
            content = []
            for element in self.config[section]:
                if self.config[section].getboolean(element):
                    content.append(element)
        elif self.format == 'latex' or self.format == 'raw':
            content = []  # TODO
            possibilities = ['publisher', 'institution', 'title', 'booktitle',
                             'author', 'pages', 'volume', 'editor',
                             'year', 'bookpublisher', 'journal']
            line = self.config[section].get('format')
            for possibility in possibilities:
                if possibility in line:
                    content.append(possibility)
        else:
            raise ValueError('Wrong format')
        return(content)

    def get_style(self, section):
        """
        Return the style (relevant only for latex format)

        :param section: Section of the config file
        :returns: string
        """
        if self.format == 'latex' or self.format == 'raw':
            return self.config[section].get('format')
        else:
            raise ValueError('Wrong format')

    def get_number_authors(self, section):
        """
        Return the number of authors (relevant only for latex format)

        :param section: Section of the config file
        :returns: float
        """
        if self.format == 'latex' or self.format == 'raw':
            return self.config[section].getint('authorlength')
        else:
            raise ValueError('Wrong format')


def check_default_config(location='~/.citebib'):
    """
    Check if default configuration files exists.
    If it does not, create them
    """
    formats = ('latex', 'bibtex', 'raw')
    for format in formats:
        path = os.path.join(os.path.expanduser(location), format)
        if not os.path.exists(path):
            os.makedirs(path)
        file = os.path.join(path, 'default.conf')
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
    elif format == 'raw':
        _write_default_config_raw(inifile)
    else:
        raise ValueError('Wrong format: %s' % format)


def _write_default_config_latex(inifile):
    """
    Write a default configuration file for latex

    :param inifile: ini file name
    """
    fields = {
        'article': ('author, journal, \\textbf{volume}, pages (year).'),
        'book': ('author, title, publisher (year).'),
        'book': ('author, title'),
    }

    config = configparser.ConfigParser()

    for entry in fields:
        content = {'format': fields[entry], 'authorlength': 0}  # TODO
        config[entry] = content

    with open(inifile, 'w') as configfile:
        config.write(configfile)

def _write_default_config_raw(inifile):
    """
    Write a default configuration file for raw

    :param inifile: ini file name
    """
    fields = {
        'article': ('author, journal, volume, pages (year).'),
        'book': ('author, title, publisher (year).'),
        'unpublished': ('author, title.'),
    }

    config = configparser.ConfigParser()

    for entry in fields:
        content = {'format': fields[entry], 'authorlength': 0}  # TODO
        config[entry] = content

    with open(inifile, 'w') as configfile:
        config.write(configfile)


def _write_default_config_bibtex(inifile):
    """
    Write a default configuration file for bibtex

    :param inifile: ini file name
    """
    # TODO: this is messy. Look for suitable configparser function
    # TODO: prefer a smart ordering (like alpha)
    reqfields = {
                'article': ('author', 'title', 'journal', 'volume', 'year', 'pages'),
                'book': ('author', 'editor', 'title', 'publisher', 'year'),
                'booklet': ('title'),
                'conference': ('author', 'title', 'booktitle', 'year'),
                'inproceedings': ('author', 'title', 'booktitle', 'year'),
                'inbook': ('author', 'editor', 'title', 'chapter', 'pages', 'publisher', 'year'),
                'incollection': ('author', 'title', 'bookpublisher', 'year'),
                'manual': ('title'),
                'mastersthesis': ('author', 'title', 'school', 'year'),
                'misc': (''),
                'phdthesis': ('author', 'title', 'school', 'year'),
                'proceedings': ('title', 'year'),
                'techreport': ('author', 'title', 'institution', 'year')
                'unpublished': ('author', 'title')
                }
    fields = ('author', 'editor', 'publisher', 'bookpublisher',
              'title', 'booktitle', 'journal', 'volume',
              'year', 'pages', 'institution')
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
    pass
