Choice Operator\ `¶ <#Choice-Operator>`__
=========================================

Syntax\ `¶ <#Syntax>`__
-----------------------

`processBehaviour <ProcessBehaviour>`__ “##”
`processBehaviour <ProcessBehaviour>`__

Semantics\ `¶ <#Semantics>`__
-----------------------------

process1 ## process2

Either process1 or process2 is executed, but never both.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>    Channel1_Int ? x 
   ##
       Channel2_Int ? y
   </pre>

| describes the process that
| either communicates the variable x over Channel1_Int
| or communicates the variable y over Channel2_Int.
