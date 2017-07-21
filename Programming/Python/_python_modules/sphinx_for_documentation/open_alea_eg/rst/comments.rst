Comments and aliases
====================

:Comments: comments can be made by adding two dots at the beginning of a line as follows::

    .. comments

:Aliases:


    The first method is to add at end of your reST document something like::

        .. _Python: http://www.python.org/

    Then, write your text inserting the keywrod ``Python_`` . The final result will be as follows: Python_ . 

    A second method is as follows::

        .. |longtext| replace:: this is a very very long text to include

    and then insert  `|longtext|` wherever needed.
 
    .. note::
        Note that when you define the reference or alias, the underscore is before the keyword. However, when you refer to it, the underscore is at the end. The underscore after the keyword is also used for internal references, citations, aliases ... 
