Value Expression
===========================================

Syntax
-----------------------

============= =====================================================================================================================================================================================================================================================================================================================================================
valExpr         :ref:`letValExpr` \| [iteValExpr](IteValExpr) \| [valExpr](ValExpr)? operator [valExpr](ValExpr) \| [valExpr](ValExpr) "::" typeName \| constName \| varName \| funcName "(" neValExprList? ")" \| constructorName ("(" neValExprList ")")? \| Integer \| String \| "REGEX" "(" RegexVal ")" \| "(" [valExpr](ValExpr) ")" \| "ERROR" String
operator      todo
neValExprList :ref:`valExpr` ("," [valExpr](ValExpr))\*
typeName      :ref:`CapsId`
constName     :ref:`SmallId`
varName       :ref:`SmallId`
funcName      :ref:`SmallId`
============= =====================================================================================================================================================================================================================================================================================================================================================

Semantics
-----------------------------

.. _reference-to-function:

Reference to Function.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The reference points to either a predefined function name,
| a function name implicitly defined by a type definition,
| or the function name of a user defined function.

Include types?
