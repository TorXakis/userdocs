Value Expression\ `¶ <#Value-Expression>`__
===========================================

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

valExpr

.. raw:: html

   </td>

.. raw:: html

   <td>

  `letValExpr <LetValExpr>`__
\| `iteValExpr <IteValExpr>`__
\| `valExpr <ValExpr>`__? operator `valExpr <ValExpr>`__
\| `valExpr <ValExpr>`__ “::” typeName
\| constName
\| varName
\| funcName “(” neValExprList? “)”
\| constructorName (“(” neValExprList “)”)?
\| Integer
\| String
\| “REGEX” “(” RegexVal “)”
\| “(” `valExpr <ValExpr>`__ “)”
\| “ERROR” String

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

operator

.. raw:: html

   </td>

.. raw:: html

   <td>

todo

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

typeName

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

   <tr>

.. raw:: html

   <td>

constName

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

varName

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

funcName

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

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

Reference to Function.\ `¶ <#Reference-to-Function>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The reference points to either a predefined function name,
| a function name implicitly defined by a type definition,
| or the function name of a user defined function.

Include types?
