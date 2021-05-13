LET Process Behaviour\ `¶ <#LET-Process-Behaviour>`__
=====================================================

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

letProcessBehaviour

.. raw:: html

   </td>

.. raw:: html

   <td>

“LET” assignment (“;” assignment)\* “IN”
`processBehaviour <ProcessBehaviour>`__ “NI”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

assignment

.. raw:: html

   </td>

.. raw:: html

   <td>

`varDecl <VarDecl>`__ “=” `valExpr <ValExpr>`__

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

Introduce variables

Examples\ `¶ <#Examples>`__
---------------------------

Simultaneously define multiple variables\ `¶ <#Simultaneously-define-multiple-variables>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statement

.. raw:: html

   <pre>LET a = 5; b = 3; c = 8 IN
      ...
      LET a = 1+b; b = 2+a; c = a*b IN ... NI
      ...
   NI
   </pre>

| defines two times three new variables (a, b, and c).
| Inside the first LET IN NI block except the second LET IN NI block,
  the values of a, b, and c are 5, 3, and 8, respectively.
| Inside the second LET IN NI block, the values of a, b, and c are 4, 7,
  and 15, respectively.
