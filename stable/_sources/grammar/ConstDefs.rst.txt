Constant Definitions\ `¶ <#Constant-Definitions>`__
===================================================

In TorXakis, the user can define constants using the CONSTDEF keyword.

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

constDefs

.. raw:: html

   </td>

.. raw:: html

   <td>

“CONSTDEF” constDef (“;” constDef)\* “ENDDEF”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

constDef

.. raw:: html

   </td>

.. raw:: html

   <td>

constName “::” typeName “::=” `valExpr <ValExpr>`__

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

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

| Define constants.
| The ValExpr must yield a constant value of the same `data
  type <Data_Type>`__ as referenced to by the typeName.

Examples\ `¶ <#Examples>`__
---------------------------

The following statement declares two integer constants, named max and
min, with the values 255 and 0, respectively.

.. raw:: html

   <pre>CONSTDEF
      max :: Int ::= 255 ;
      min :: Int ::= 0
   ENDDEF
   </pre>
