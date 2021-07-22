Parallel Operator
=============================================

Syntax
-----------------------

`processBehaviour <ProcessBehaviour>`__ "|||"
`processBehaviour <ProcessBehaviour>`__

Semantics
-----------------------------

process1 \||\| process2

| The processes 1 and 2 run independently in parallel.
| No synchronization between the processes is required.
| Of course, the processes might communicate with each other.

When both processes have exited then parallel composition exits

Examples
---------------------------

The statement

::

   ChannelId1 ? x ||| ChannelId2 ? y

describes the process that can, in any order, do the following two
things:

-  Communicate variable x over ChannelId1
-  Communicate variable y over ChannelId2

The process ends when both communications have occurred.

In other words, the following three behaviours can be observed:

============== =======================================================
First 1 then 2 ChannelId1 ? x :ref:`>->` ChannelId2 ? y
First 2 then 1 ChannelId2 ? y :ref:`>->` ChannelId1 ? x
Synchronously  ChannelId1 ? x :ref:`|` ChannelId2 ? y
============== =======================================================
