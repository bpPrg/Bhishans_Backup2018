Text syntax: bold, italic, verbatim and special characters `
============================================================

:basic usage:

  * use one asterisk on each side of a text you want to emphasize in  *italic* and 2 asterisks in you want to make it **bold**::

        *italic*
        **bold**

  * double backquotes are used to make a text verbatim. For instance, it you want to use special characters such as ``*``::

        This ``*`` character is not interpreted

  * Finally, the single backquote is used for reST special commands (e.g., hyper links with spaces)::

        This is how to create hyperlinks (see later)  `OpenAlea wiki <openalea.gforge.inria.fr>`_

    .. note:: If asterisks or backquotes appear in running text and could be confused with inline markup delimiters, they have to be escaped with a backslash.

:advanced usage:

    Be aware of some restrictions of this markup:

    * it may not be nested,
    * content may not start or end with whitespace: ``* text*`` is wrong,
    * it must be separated from surrounding text by non-word characters. 

    Use a backslash escaped space to work around that:

    * ``this is a *longish* paragraph`` is correct and gives *longish*.
    * ``this is a long*ish* paragraph`` is not interpreted as expected. You 
      should use ``this is a long\ *ish* paragraph`` to obtain long\ *ish* paragraph

.. warning::

    In Python docstrings it will be necessary to escape any backslash characters so that they actually reach reStructuredText. The simplest way to do this is to use raw strings:

    ===================================== ================================
    Python string                         Typical result
    ===================================== ================================
    ``r"""\*escape* \`with` "\\""""``     ``*escape* `with` "\"``
    ``"""\\*escape* \\`with` "\\\\""""``  ``*escape* `with` "\"``
    ``"""\*escape* \`with` "\\""""``      ``escape with ""``
    ===================================== ================================
