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
install_requires = [
    'bibtexparser']
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development']


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
        author_email="devel@sciunto.org",
        description=(
            "Generate a nice Bibtex or Latex bibliography "
            "according to the document content"),
        packages=['libcitebib'],
        scripts=['citebib', 'citekey'],
        install_requires=install_requires,
        classifiers = classifiers)


if __name__ == '__main__':
    run_setup()
