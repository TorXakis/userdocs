Synchronized Operator
=====================================================

Syntax
-----------------------

`processBehaviour <ProcessBehaviour>`__ "||"
`processBehaviour <ProcessBehaviour>`__

Semantics
-----------------------------

process1 \|\| process2

process1 and process2 are executed while synchronized over all channels,
including `EXIT <EXIT>`__.

When both processes have exited then the synchronized composition exits.

Examples
---------------------------

Communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statement

::

       Channel1_Int ? x 
   ||
       Channel1_Int ? y

| describes the process with two sub processes that are synchronized
  over all channels.
| Since both sub processes want to communicate over Channel1_Int,
  communication is possible.
| After that communication has occurred x and y contain the same value,
  and
| since both communications have exited, the synchronized composition
  exits.

Constrained communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statement

::

       Channel1_Int ? x [[ x >= 10 ]]
   ||
       Channel1_Int ? y [[ y <= 20 ]]

| describes the process with two sub processes that are synchronized
  over all channels.
| Since both sub processes want to communicate over Channel1_Int and
| both constraints can be simultaneously satisfied, communication is
  possible.
| After that communication has occurred x and y contain the same value
  in the range [10,20]
| and, since both communications have exited, the synchronized
  composition exits.

Deadlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The statement

::

       Channel1_Int ? x 
   ||
       Channel2_Int ? y

| describes the process with two sub processes that are synchronized
  over all channels.
| Since one sub process wants to communicate the variable x over
  Channel1_Int and
| the other sub process wants to communicate the variable y over another
  channel, Channel2_Int,
| communication under the synchronization constraint is not possible,
  i.e., the process is in
  `deadlock <https://en.wikipedia.org/wiki/Deadlock>`__.
