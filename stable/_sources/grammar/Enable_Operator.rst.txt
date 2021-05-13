Enable Operator\ `¶ <#Enable-Operator>`__
=========================================

Syntax\ `¶ <#Syntax>`__
-----------------------

| `processBehaviour <ProcessBehaviour>`__ >>>
  `processBehaviour <ProcessBehaviour>`__
| `processBehaviour <ProcessBehaviour>`__ >>> “ACCEPT” (“?”
  `varDecl <VarDecl>`__ \| “!” `valExpr <ValExpr>`__ )\* IN
  `processBehaviour <ProcessBehaviour>`__ NI

Semantics\ `¶ <#Semantics>`__
-----------------------------

| Synchronize on EXIT of multiple processes.
| When EXIT values are communicated, they must be ACCEPTed for further
  use.

Examples\ `¶ <#Examples>`__
---------------------------

.. raw:: html

   <pre>(
       A ? x :: Int >-> EXIT ! x ? y :: Int
   |||
       B ? y :: Int >-> EXIT ? x :: Int ! y
   ) 
   >>> ACCEPT ? a ? b IN 
      C ! a + b
   NI
   </pre>
