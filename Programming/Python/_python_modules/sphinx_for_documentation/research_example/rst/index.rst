.. image:: ../images/trust_jedi.png
   :height: 100px
   :width: 400 px
   :align: center


.. contents:: Table of Contents
   :depth: 3


Chapter 1
==========
This is chapter 1.

.. toctree::
   :maxdepth: 4

   galaxy_count_conversion
   mag_diff_f6_f8


Tutorial
==========
Commands to run after I edit rst/index.rst or any rst files inside rst.


| make clean  
| make html  
| sphinx-build -b html rst html  
| open html/index.rst 

.. toctree::
   :maxdepth: 4

   tutorial
   hello


For the colored special dirctives follow this link


`Special Directives <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html#include-other-rest-files-and-toc>`_

The directives **seealso**, **note** **warning** work always but to make the
directive **todo** work, we should active **todo** in conf.py.  

[extensions]
todo_include_todos=True



.. seealso:: This is a simple **seealso** note.
.. note:: This is a simple **note** note.
.. warning:: This is a simple **warning** note.
.. todo:: This is a simple **todo** note.





