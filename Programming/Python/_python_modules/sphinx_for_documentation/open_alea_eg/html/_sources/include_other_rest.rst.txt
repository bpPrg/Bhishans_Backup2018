Include other reST files and TOC
================================

Since reST does not have facilities to interconnect several documents, or split
documents into multiple output files, Sphinx uses a custom directive to add 
relations between the single files the documentation is made of, as well as 
tables of contents. The toctree directive is the central element. 

.. code-block:: rest

    .. toctree::
        :maxdepth: 2

        intro
        chapter1
        chapter2

Globbing can be used by adding the *glob* option:

.. code-block:: rest

    .. toctree::
        :glob:

        intro*
        recipe/*
        *

The name of the file is used to create the title in the TOC. You may want to change this behaviour by changing the toctree as follows:

.. code-block:: rest
       
    .. toctree::
        :glob:
       
        intro
        Chapter1 description <chapter1>
