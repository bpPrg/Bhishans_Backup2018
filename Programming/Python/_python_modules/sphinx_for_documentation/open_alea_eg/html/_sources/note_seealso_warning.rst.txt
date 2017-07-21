##################
Special directives
##################

colored boxes: note, seealso, todo and warnings
=================================================

There are simple directives like **seealso** that creates nice colored boxes:

.. seealso:: This is a simple **seealso** note. 

created using::

    .. seealso:: This is a simple **seealso** note. Other inline directive may be included (e.g., math :math:`\alpha`) but not al of them.

You have also the **note** and **warning** directives:

.. note::  This is a **note** box.

.. warning:: note the space between the directive and the text

.. todo:: a todo box

There is another nice dircective with the **todo** one but it requires to add `sphinx.ext.todo` extension in the **conf.py** file and these two lines of code::

    [extensions]
    todo_include_todos=True
