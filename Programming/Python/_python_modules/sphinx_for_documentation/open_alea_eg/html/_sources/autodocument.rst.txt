Auto-document your python code
==============================

.. todo:: more details here

Let us suppose you have a python file called *test.py* with a function called *square*

.. code-block:: rest

    .. module:: test
        :platform: Unix, Windows
        :synopsis: sample of documented python code

    .. autofunction:: square

Gives

.. module:: test
    :platform: Unix, Windows
    :synopsis: sample of documented python code

.. autofunction:: square

Using the **module** creates an index (see top right of this page)

.. warning:: the python code must be in the PYTHONPATH.

.. seealso:: http://sphinx.pocoo.org/markup/desc.html
