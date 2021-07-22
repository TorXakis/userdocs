Guard Operator
=======================================

Syntax
-----------------------

======================= ===============================================================
guardedProcessBehaviour :ref:`condition` =>> [processBehaviour](ProcessBehaviour)
:ref:`condition`  [[ [valExpr](ValExpr) ]]
======================= ===============================================================

Semantics
-----------------------------

| Conditional execution: [[ expr ]] =>> next
| Next is only executed when expr is true

Example
-------------------------

[[ not(isNil(buf)) ]] =>> Value !head(buf)
