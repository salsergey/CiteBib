#!/usr/bin/env python

from distutils.core import setup
from libcitebib import info

setup(
    name         = 'CiteBib',
    version      = info.VERSION,
    url          = info.URL,
    author       = "Francois Boulogne",
    license      = info.LICENSE,
    author_email = info.EMAIL,
    description  = info.SHORT_DESCRIPTION,
    packages     = ['libcitebib'],
    scripts      = ['citebib', 'citekey'],
)
