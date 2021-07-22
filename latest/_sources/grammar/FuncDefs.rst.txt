Function Defintions
=================================================

Syntax
-----------------------

===================== ==============================================================================
funcDefs              "FUNCDEF" funcDef (";" funcDef)\* "ENDDEF"
funcDef               funcName "(" neVarsDeclarationList? ")" "::" typeName "::=" :ref:`valExpr`
neVarsDeclarationList varsDeclaration (";" varsDeclaration )\*
varsDeclaration       neVarNameList "::" typeName
neVarNameList         varName ("," varName )\*
funcName              :ref:`SmallId`
varName               :ref:`SmallId`
typeName              :ref:`CapsId`
===================== ==============================================================================

Semantics
-----------------------------

Define functions.

Examples
---------------------------

Function to determine whether a integer is an int32; a 32-bits integer.

::

   FUNCDEF isValid_int32 ( x :: Int ) :: Bool ::= (-2147483648 <= x) /\ (x <= 2147483647) ENDDEF

Function to determine the validity of a password. In this example, a
valid password is a string whose length is larger than 8, and that
contains a capital, a small letter, and a digit.

::

   FUNCDEF validPassword ( pw :: String ) :: Bool ::=
         len(pw) > 8
      /\ strinre(pw, REGEX('.*[A-Z].*'))
      /\ strinre(pw, REGEX('.*[a-z].*'))
      /\ strinre(pw, REGEX('.*[0-9].*'))
   ENDDEF

Recursive function to determine the length of an instance of the
recursive data type List_Int:

::

   FUNCDEF lengthList_Int ( x :: List_Int ) :: Int ::=
      IF isCNil_Int(x) THEN
         0
      ELSE
         1 + lengthList_Int(tail(x))
      FI
   ENDDEF

Function with multiple variables that checks for equality.

::

   FUNCDEF allEqual ( xi, yi :: Int; xs, ys :: String; xl, yl :: List_Int ) :: Bool ::=
      (xi == yi) /\ (xs == ys) /\ (xl == yl)
   ENDDEF

Definition of multiple functions in a single FUNCDEF block.

::

   FUNCDEF 
      max ( x, y :: Int ) :: Int ::= IF (x > y) THEN x ELSE y FI ;
      min ( x, y :: Int ) :: Int ::= IF (x < y) THEN x ELSE y FI
   ENDDEF
