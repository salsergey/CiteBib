#!/usr/bin/env python
from setuptools import setup

from libcitebib import __version__ as version

def run_setup():
    setup(
        name='CiteBib',
        version=version,
        url="https://github.com/sciunto-org/python-bibtexparser",
        author="Francois Boulogne",
        license="GPLv3+",
        author_email="fboulogne@sciunt.org",
        description=(
            "Generate a nice Bibtex or Latex bibliography "
            "according to the document content"),
        packages=['libcitebib'],
        scripts=['citebib', 'citekey'],


if __name__ == '__main__':
    run_setup()
