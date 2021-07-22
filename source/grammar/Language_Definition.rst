Language Definition
=================================================

Syntax
-----------------------

============= =========================================================================================================================================================================================================
specification ( :ref:`modelDefs` \| [cnectDefs](CnectDefs) \| [chanDefs](ChanDefs) \| [typeDefs](TypeDefs) \| [constDefs](ConstDefs) \| [funcDefs](FuncDefs) \| [procDefs](ProcDefs) \| [stautDef](StautDef) ) \*
============= =========================================================================================================================================================================================================

Semantics
-----------------------------

| A specification contains zero or more definitions.
| A `Model Definition <ModelDefs>`__ is needed to step a TorXakis model.
| A `Model Definition <ModelDefs>`__ and `Connection
  Definition <CnectDefs>`__ are minimally needed to test a SUT or
  simulate a system using a TorXakis model.
