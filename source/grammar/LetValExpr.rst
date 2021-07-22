LET Value Expression
===================================================

Syntax
-----------------------

========== ================================================================
letValExpr "LET" assignment (";" assignment)\* "IN" :ref:`valExpr` "NI"
assignment :ref:`varDecl` "=" [valExpr](ValExpr)
========== ================================================================

Semantics
-----------------------------

Introduce variables

Examples
---------------------------

Simultaneously define multiple variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statement

::

   LET a = 5; b = 3; c = 8 IN
      ...
      LET a = 1+b; b = 2+a; c = a*b IN ... NI
      ...
   NI

| defines two times three new variables (a, b, and c).
| Inside the first LET IN NI block except the second LET IN NI block,
  the values of a, b, and c are 5, 3, and 8, respectively.
| Inside the second LET IN NI block, the values of a, b, and c are 4, 7,
  and 15, respectively.
