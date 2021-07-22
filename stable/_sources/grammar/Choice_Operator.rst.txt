Choice Operator
=========================================

Syntax
-----------------------

`processBehaviour <ProcessBehaviour>`__ "##"
`processBehaviour <ProcessBehaviour>`__

Semantics
-----------------------------

process1 ## process2

Either process1 or process2 is executed, but never both.

Examples
---------------------------

The statement

::

       Channel1_Int ? x 
   ##
       Channel2_Int ? y

| describes the process that
| either communicates the variable x over Channel1_Int
| or communicates the variable y over Channel2_Int.
