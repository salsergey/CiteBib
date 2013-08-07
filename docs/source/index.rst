.. CiteBib documentation master file, created by
   sphinx-quickstart on Thu Aug  1 16:31:20 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CiteBib's documentation!
===================================


:Authors: François Boulogne
:Download: `Stable version <http://sciunto.org/source/>`_
:Developer's corner: `github.com project <https://github.com/sciunto/CiteBib>`_
:Generated: |today|
:License: GPL v3
:Version: |release|



Contents:

.. toctree::
   :maxdepth: 2

   install


What is Citebib?
================

The best description is my usage. I have several bibtex managed with jabref. When I write an article, I pick up some references from these bibtex files. The point is that I do not want to use the big bibtex files for my article because:

* they contain unused entries
* they contain custom fields/notes

citebib reads your tex files, track \cite{} calls, and select useful fields. Then, it generates:

* a clean bibtex file,
* or a bibliography in a latex format (because some journals do not support bibtex)

The behavior is customisable from the configuration.

Given a key, citekey returns a formatted reference. (Might be useful for emails, presentations...)

How to install
==============

See :doc:`install`.


Configuration
=============

TODO

Usage
=====

citebib
-------

To print the syntax:

.. code-block:: sh

    citebib -h


citekey
-------

To print the syntax:

.. code-block:: sh

    citekey -h

To print the reference *foo2010* in a raw style:

.. code-block:: sh

    citekey foo2010

To print the reference *foo2010* in a latex style:

.. code-block:: sh

    citekey --latex foo2010

To print the bibtex entry *foo2010*:

.. code-block:: sh

    citekey --bibtex foo2010


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

