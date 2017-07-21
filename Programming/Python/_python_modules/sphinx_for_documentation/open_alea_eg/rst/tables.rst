tables
======

There are several ways to write tables. Use standard reStructuredText tables as explained here. They work fine in HTML output, however, there are some gotchas when using tables for LaTeX output.

:simple table:

    Simple tables can be written as follows::

        +---------+---------+-----------+
        | 1       |  2      |  3        |
        +---------+---------+-----------+

    which gives:

    +---------+---------+-----------+
    | 1       | 2       | 3         |
    +---------+---------+-----------+



:complex table:

    ::

        +------------+------------+-----------+
        | Header 1   | Header 2   | Header 3  |
        +============+============+===========+
        | body row 1 | column 2   | column 3  |
        +------------+------------+-----------+
        | body row 2 | Cells may span columns.|
        +------------+------------+-----------+
        | body row 3 | Cells may  | - Cells   |
        +------------+ span rows. | - contain |
        | body row 4 |            | - blocks. |
        +------------+------------+-----------+

    gives:

    .. htmlonly::

        +------------+------------+-----------+
        | Header 1   | Header 2   | Header 3  |
        +============+============+===========+
        | body row 1 | column 2   | column 3  |
        +------------+------------+-----------+
        | body row 2 | Cells may span columns.|
        +------------+------------+-----------+
        | body row 3 | Cells may  | - Cells   |
        +------------+ span rows. | - contain |
        | body row 4 |            | - blocks. |
        +------------+------------+-----------+

:another way:

    ::

        =====  =====  ======
           Inputs     Output
        ------------  ------
          A      B    A or B
        =====  =====  ======
        False  False  False
        True   False  True
        =====  =====  ======

    gives:

    .. htmlonly::

        =====  =====  ======
           Inputs     Output
        ------------  ------
          A      B    A or B
        =====  =====  ======
        False  False  False
        True   False  True
        =====  =====  ======

.. note:: table and latex documents are not yet compatible in sphinx, and you should therefore precede them with the a special directive (.. htmlonly::)


The previous examples work fine in HTML output, however there are some gotchas when using tables in LaTeX: the column width is hard to determine correctly automatically. For this reason, the following directive exists::

    .. tabularcolumns:: column spec

This directive gives a â€œcolumn specâ€ for the next table occurring in the source file. It can have values like::

    |l|l|l|

which means three left-adjusted (LaTeX syntax). By default, Sphinx uses a table layout with L for every column. This code::

    .. tabularcolumns:: |l|c|p{5cm}|

    +--------------+---+-----------+
    |  simple text | 2 | 3         |
    +--------------+---+-----------+

gives 

.. htmlonly::

    .. tabularcolumns:: |l|c|p{5cm}|

    +--------------+------------+-----------+
    | title        |            |           |
    +==============+============+===========+
    |  simple text | 2          | 3         |
    +--------------+------------+-----------+

