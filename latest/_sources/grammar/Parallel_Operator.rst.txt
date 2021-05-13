Parallel Operator\ `¶ <#Parallel-Operator>`__
=============================================

Syntax\ `¶ <#Syntax>`__
-----------------------

`processBehaviour <ProcessBehaviour>`__ “\||\|”
`processBehaviour <ProcessBehaviour>`__

Semantics\ `¶ <#Semantics>`__
-----------------------------

process1 \||\| process2

| The processes 1 and 2 run independently in parallel.
| No synchronization between the processes is required.
| Of course, the processes might communicate with each other.

When both processes have exited then parallel composition exits

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>ChannelId1 ? x ||| ChannelId2 ? y
   </pre>

describes the process that can, in any order, do the following two
things:

-  Communicate variable x over ChannelId1
-  Communicate variable y over ChannelId2

The process ends when both communications have occurred.

In other words, the following three behaviours can be observed:

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

First 1 then 2

.. raw:: html

   </td>

.. raw:: html

   <td>

ChannelId1 ? x `>-> <Sequence_Operator>`__ ChannelId2 ? y

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

First 2 then 1

.. raw:: html

   </td>

.. raw:: html

   <td>

ChannelId2 ? y `>-> <Sequence_Operator>`__ ChannelId1 ? x

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Synchronously

.. raw:: html

   </td>

.. raw:: html

   <td>

ChannelId1 ? x `\| <Synchronous_Operator>`__ ChannelId2 ? y

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>
