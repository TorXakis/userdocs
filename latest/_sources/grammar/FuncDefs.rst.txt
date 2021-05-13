Function Defintions\ `¶ <#Function-Defintions>`__
=================================================

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

funcDefs

.. raw:: html

   </td>

.. raw:: html

   <td>

“FUNCDEF” funcDef (“;” funcDef)\* “ENDDEF”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

funcDef

.. raw:: html

   </td>

.. raw:: html

   <td>

funcName “(” neVarsDeclarationList? “)” “::” typeName “::=”
`valExpr <ValExpr>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neVarsDeclarationList

.. raw:: html

   </td>

.. raw:: html

   <td>

varsDeclaration (“;” varsDeclaration )\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

varsDeclaration

.. raw:: html

   </td>

.. raw:: html

   <td>

neVarNameList “::” typeName

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neVarNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

varName (“,” varName )\*

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

Define functions.

Examples\ `¶ <#Examples>`__
---------------------------

Function to determine whether a integer is an int32; a 32-bits integer.

.. raw:: html

   <pre>FUNCDEF isValid_int32 ( x :: Int ) :: Bool ::= (-2147483648 <= x) /\ (x <= 2147483647) ENDDEF
   </pre>

Function to determine the validity of a password. In this example, a
valid password is a string whose length is larger than 8, and that
contains a capital, a small letter, and a digit.

.. raw:: html

   <pre>FUNCDEF validPassword ( pw :: String ) :: Bool ::=
         len(pw) > 8
      /\ strinre(pw, REGEX('.*[A-Z].*'))
      /\ strinre(pw, REGEX('.*[a-z].*'))
      /\ strinre(pw, REGEX('.*[0-9].*'))
   ENDDEF
   </pre>

Recursive function to determine the length of an instance of the
recursive data type List_Int:

.. raw:: html

   <pre>FUNCDEF lengthList_Int ( x :: List_Int ) :: Int ::=
      IF isCNil_Int(x) THEN
         0
      ELSE
         1 + lengthList_Int(tail(x))
      FI
   ENDDEF
   </pre>

Function with multiple variables that checks for equality.

.. raw:: html

   <pre>FUNCDEF allEqual ( xi, yi :: Int; xs, ys :: String; xl, yl :: List_Int ) :: Bool ::=
      (xi == yi) /\ (xs == ys) /\ (xl == yl)
   ENDDEF
   </pre>

Definition of multiple functions in a single FUNCDEF block.

.. raw:: html

   <pre>FUNCDEF 
      max ( x, y :: Int ) :: Int ::= IF (x > y) THEN x ELSE y FI ;
      min ( x, y :: Int ) :: Int ::= IF (x < y) THEN x ELSE y FI
   ENDDEF
   </pre>
