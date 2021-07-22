Constant Definitions
===================================================

In TorXakis, the user can define constants using the CONSTDEF keyword.

Syntax
-----------------------

========= ================================================
constDefs "CONSTDEF" constDef (";" constDef)\* "ENDDEF"
constDef  constName "::" typeName "::=" :ref:`valExpr`
constName :ref:`SmallId`
typeName  :ref:`CapsId`
========= ================================================

Semantics
-----------------------------

| Define constants.
| The ValExpr must yield a constant value of the same `data
  type <Data_Type>`__ as referenced to by the typeName.

Examples
---------------------------

The following statement declares two integer constants, named max and
min, with the values 255 and 0, respectively.

::

   CONSTDEF
      max :: Int ::= 255 ;
      min :: Int ::= 0
   ENDDEF
