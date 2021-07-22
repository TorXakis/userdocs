IF THEN ELSE Value Expression
=====================================================================

Syntax
-----------------------

========== ===========================================================
iteValExpr "IF" [[valExpr]] "THEN" [[valExpr]] "ELSE" [[valExpr]] "FI"
========== ===========================================================

Semantics
-----------------------------

IF ``expr1`` THEN ``expr2`` ELSE ``expr3`` FI

The type of ``expr1`` must be Boolean. The type of ``expr2`` must be
equal to the type of ``expr3``.

The expressions ``expr2`` and ``expr3`` are only evaluated after the
value of ``expr1`` is evaluated to ``True`` or ``False``, respectively.
For Boolean expressions in which the order of evaluation is irrelevant,
one could consider the `equivalent
alternatives <https://en.wikipedia.org/wiki/Conditioned_disjunction>`__:

-  (``expr1`` => ``expr2``) /\\ (not(``expr1``) => ``expr3``) or
-  (``expr1`` /\\ ``expr2``) \\/ (not(``expr1``) /\\ ``expr3``)
