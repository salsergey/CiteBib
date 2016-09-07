#!/usr/bin/env python
from setuptools import setup


VERSION_FILE = 'libcitebib/_version.py'
MAJOR = 0
MINOR = 4
MICRO = 3
VERSION = '{major}.{minor}.{micro}'.format(
    major=MAJOR, minor=MINOR, micro=MICRO)
VERSION_TEXT = (
    '# This file was generated from setup.py\n'
    "version = '{version}'\n")

def run_setup():
    version = VERSION
    s = VERSION_TEXT.format(version=version)
    with open(VERSION_FILE, 'w') as f:
        f.write(s)
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
