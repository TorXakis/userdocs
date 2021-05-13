Variable Declaration\ `¶ <#Variable-Declaration>`__
===================================================

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

varDecl

.. raw:: html

   </td>

.. raw:: html

   <td>

varName (“::” typeName)?

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

Declare a variable. The type can only be left out when the type can be
deducted from the context.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>s :: String
   </pre>

declares a variable named s of type String.
