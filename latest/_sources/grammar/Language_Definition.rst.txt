Language Definition
=================================================

Syntax
-----------------------

============= =========================================================================================================================================================================================================
specification ( :ref:`modelDefs` \| :ref:`cnectDefs` \| :ref:`chanDefs` \| :ref:`typeDefs` \| :ref:`constDefs` \| :ref:`funcDefs` \| :ref:`procDefs` \| :ref:`stautDef` ) \*
============= =========================================================================================================================================================================================================

Semantics
-----------------------------

| A specification contains zero or more definitions.
| A `Model Definition <ModelDefs>`__ is needed to step a TorXakis model.
| A `Model Definition <ModelDefs>`__ and `Connection
  Definition <CnectDefs>`__ are minimally needed to test a SUT or
  simulate a system using a TorXakis model.
