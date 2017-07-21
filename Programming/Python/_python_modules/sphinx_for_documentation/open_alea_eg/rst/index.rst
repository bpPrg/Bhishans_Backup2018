.. _rst_tutorial:


##############################################
Restructured Text (reST) and Sphinx CheatSheet
##############################################

.. sidebar:: Summary

    :Authors: **Bhishan Poudel**
    :Date: |today|
    :Release: |release|

.. contents::
   :depth: 2


.. seealso::

    This documentation is based based upon documentation found in:
      * `Sphinx <http://sphinx.pocoo.org/rest.html>`_ 
      * `Docutils <http://docutils.sourceforge.net/rst.html>`_
      * `Openalea <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_

.. seealso::

    Sphinx Themes:
      * `Themes <http://www.sphinx-doc.org/en/stable/theming.html>`_ 
      * `Hex colors <http://htmlcolorcodes.com/>`_ 
      * Location /Users/poudel/anaconda/pkgs/sphinx-1.5.6-py36_0/lib/python3.6/site-packages/Sphinx-1.5.6-py3.6.egg/sphinx/themes/

.. note:: Sphinx code is written in reST. Nonetheless, sphinx adds many additional directives on top of the reST syntax. Therefore sphinx code may not be fully compatible with reST. 

.. admonition:: Information

   some info


############
Generalities
############

Introduction
============

reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext
markup syntax and parser system. It is useful for in-line program documentation
(such as Python docstrings), for quickly creating simple web pages, and for
standalone documents. 

.. warning::

    like Python, reST syntax is sensitive to indentation !

.. warning::

    reST requires blank lines between paragraphs



Text syntax: bold, italic, verbatim and special characters `
============================================================    
.. toctree::
   :maxdepth: 4

   basic_syntax

Headings 
==========
.. toctree::
   :maxdepth: 4

   headings

Directives
============
.. toctree::
   :maxdepth: 4

   directives

Internal and External Links
=============================
.. toctree::
   :maxdepth: 4

   links

list and bullets
================
.. toctree::
   :maxdepth: 4

   list_and_bullets

tables
======
.. toctree::
   :maxdepth: 4

   tables

Include other reST files and TOC
================================
.. toctree::
   :maxdepth: 4

   include_other_rest

Comments and aliases
====================
.. toctree::
   :maxdepth: 4

   comments

##################
Special directives
##################

colored boxes: note, seealso, todo and warnings
=================================================
.. toctree::
   :maxdepth: 4

   note_seealso_warning

Inserting code and Literal blocks
===================================
.. toctree::
   :maxdepth: 4

   insert_code


Maths and Equations with LaTeX
==============================
.. toctree::
   :maxdepth: 4

   maths_and_latex

Add tests with doctests
=======================
.. toctree::
   :maxdepth: 4

   doctest_eg

Auto-document your python code
==============================
.. toctree::
   :maxdepth: 4

   autodocument

Image directive
===============
.. toctree::
   :maxdepth: 4

   directive_image


Figure directive
=================
.. toctree::
   :maxdepth: 4

   directive_figure

Topic directive
===============
.. toctree::
   :maxdepth: 4

   directive_topic

Sidebar directive
=================
.. toctree::
   :maxdepth: 4

   directive_sidebar

glossary, centered, index, download and field list
===================================================
.. toctree::
   :maxdepth: 4

   glossary

Footnote
========
.. toctree::
   :maxdepth: 4

   footnotes_citation

Aliases and Cross-referencing syntax
======================================
.. toctree::
   :maxdepth: 4

   alias_cross_ref
