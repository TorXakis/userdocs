Process Call\ `¶ <#Process-Call>`__
===================================

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

procCall

.. raw:: html

   </td>

.. raw:: html

   <td>

procName “[" neChannelNameList? "]” “(” neValExprList? “)”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neChannelNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

channelName (“,” channelName)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neValExprList

.. raw:: html

   </td>

.. raw:: html

   <td>

`valExpr <ValExpr>`__ (“,” `valExpr <ValExpr>`__)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

procName

.. raw:: html

   </td>

.. raw:: html

   <td>

`SmallId <SmallId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

channelName

.. raw:: html

   </td>

.. raw:: html

   <td>

`CapsId <CapsId>`__

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

| Call a user defined process, defined with `PROCDEF <ProcDefs>`__.
| Channel name must refer to a predefined channel name.
