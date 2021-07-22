Enable Operator
=========================================

Syntax
-----------------------

| `processBehaviour <ProcessBehaviour>`__ >>>
  `processBehaviour <ProcessBehaviour>`__
| `processBehaviour <ProcessBehaviour>`__ >>> "ACCEPT" ("?"
  `varDecl <VarDecl>`__ \| "!" `valExpr <ValExpr>`__ )\* IN
  `processBehaviour <ProcessBehaviour>`__ NI

Semantics
-----------------------------

| Synchronize on EXIT of multiple processes.
| When EXIT values are communicated, they must be ACCEPTed for further
  use.

Examples
---------------------------

::

   (
       A ? x :: Int >-> EXIT ! x ? y :: Int
   |||
       B ? y :: Int >-> EXIT ? x :: Int ! y
   ) 
   >>> ACCEPT ? a ? b IN 
      C ! a + b
   NI
