##########
Others
##########
Footnote
========

For footnotes, use ``[#name]_`` to mark the footnote location, and add the 
footnote body at the bottom of the document after a â€œFootnotesâ€ rubric 
heading, like so::

  Some text that requires a footnote [#f1]_ .

  .. rubric:: Footnotes

  .. [#f1] Text of the first footnote.


You can also explicitly number the footnotes (``[1]_``) or use auto-numbered 
footnotes without names (``[#]_``). Here is an example [#footnote1]_.

Citations
=========

Citation references, like [CIT2002]_ may be defined at the bottom of the page::

    .. [CIT2002] A citation
              (as often used in journals).

and called as follows::

    [CIT2002]_
