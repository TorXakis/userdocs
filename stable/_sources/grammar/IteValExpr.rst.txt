IF THEN ELSE Value Expression\ `¶ <#IF-THEN-ELSE-Value-Expression>`__
=====================================================================

Syntax\ `¶ <#Syntax>`__
-----------------------

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

iteValExpr

.. raw:: html

   </td>

.. raw:: html

   <td>

“IF” [[valExpr]] “THEN” [[valExpr]] “ELSE” [[valExpr]] “FI”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

IF ``expr1`` THEN ``expr2`` ELSE ``expr3`` FI

The type of ``expr1`` must be Boolean. The type of ``expr2`` must be
equal to the type of ``expr3``.

The expressions ``expr2`` and ``expr3`` are only evaluated after the
value of ``expr1`` is evaluated to ``True`` or ``False``, respectively.
For Boolean expressions in which the order of evaluation is irrelevant,
one could consider the `equivalent
alternatives <https://en.wikipedia.org/wiki/Conditioned_disjunction>`__:
\* (``expr1`` => ``expr2``) / (not(``expr1``) => ``expr3``) or \*
(``expr1`` / ``expr2``) \\/ (not(``expr1``) / ``expr3``)
