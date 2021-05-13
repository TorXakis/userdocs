Guard Operator\ `¶ <#Guard-Operator>`__
=======================================

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

guardedProcessBehaviour

.. raw:: html

   </td>

.. raw:: html

   <td>

`condition <Condition>`__ =>> `processBehaviour <ProcessBehaviour>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

`condition <Condition>`__

.. raw:: html

   </td>

.. raw:: html

   <td>

[[ `valExpr <ValExpr>`__ ]]

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

| Conditional execution: [[ expr ]] =>> next
| Next is only executed when expr is true

Example\ `¶ <#Example>`__
-------------------------

[[ not(isNil(buf)) ]] =>> Value !head(buf)
