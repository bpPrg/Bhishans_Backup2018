Maths and Equations with LaTeX
==============================

In order to include equations or simple Latex code in the text (e.g., :math:`\alpha \leq \beta` ) use the following code::

     :math:`\alpha > \beta`  


.. warning:: 
    The *math* markup can be used within reST files (to be parsed by Sphinx) but within your python's docstring, the slashes need to be escaped ! ``:math:`\alpha``` should therefore be written ``:math:`\\alpha``` or put an "r" before the docstring  

Note also, that you can easily more complex mathematical expressions using the math directive as follows::

    .. math::
        
        n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

.. math:: n_{\mathrm{offset}} = \sum_{k=0}^{N-1} s_k n_k

It seems that there is no limitations to LaTeX usage:

.. math:: 

   s_k^{\mathrm{column}} = \prod_{j=0}^{k-1} d_j , \quad  s_k^{\mathrm{row}} = \prod_{j=k+1}^{N-1} d_j .
