Value Expression
===========================================

Syntax
-----------------------

============= =====================================================================================================================================================================================================================================================================================================================================================
valExpr         :ref:`letValExpr` \| :ref:`iteValExpr` \| :ref:`valExpr`? operator :ref:`valExpr` \| :ref:`valExpr` "::" typeName \| constName \| varName \| funcName "(" neValExprList? ")" \| constructorName ("(" neValExprList ")")? \| Integer \| String \| "REGEX" "(" RegexVal ")" \| "(" :ref:`valExpr` ")" \| "ERROR" String
operator      todo
neValExprList :ref:`valExpr` ("," :ref:`valExpr`)\*
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
