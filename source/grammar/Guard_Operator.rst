Guard Operator
=======================================

Syntax
-----------------------

======================= ===============================================================
guardedProcessBehaviour :ref:`condition` =>> :ref:`processBehaviour`
:ref:`condition`  :ref:`[ [valExpr` ]]
======================= ===============================================================

Semantics
-----------------------------

| Conditional execution: [[ expr ]] =>> next
| Next is only executed when expr is true

Example
-------------------------

[[ not(isNil(buf)) ]] =>> Value !head(buf)
