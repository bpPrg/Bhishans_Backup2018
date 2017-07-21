Inserting code and Literal blocks
===================================

:simple code:

    Literal code blocks are introduced by ending a paragraph with the special marker (double coulumn) `::`. The literal block must be indented (and, like all paragraphs, separated from the surrounding ones by blank lines). 


    The two following codes::

        This is a simple example::

            import math
            print 'import done'
    
    and::

        This is a simple example:
        ::

            import math
            print 'import done'

    gives:

    This is a very simple example::

        import math
        print 'import done' 

:code-block:

    By default the syntax of the language is Python, but you can specify the language using the **code-block** directive as follows::

        .. code-block:: html
            :linenos:

           <h1>code block example</h1>

    produces

    .. code-block:: html
       :linenos:

       <h1>code block example</h1>


:literalinclude:

    Then, it is also possible to include the contents of a file as follows:

    .. code-block:: rest

        .. literalinclude:: filename
            :linenos:
            :language: python
            :lines: 1, 3-5
            :start-after: 3
            :end-before: 5

    .. literalinclude:: test.py
        :linenos:
