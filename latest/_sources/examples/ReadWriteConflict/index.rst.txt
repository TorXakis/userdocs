Modelling Example - Shared Memory
=================================

How can we model shared memory, i.e., a global variable, in
[TorXakis][7]? For simplicity, we will assume that the shared memory
stores a value of `Data
Type <https://github.com/TorXakis/TorXakis/wiki/Data_Type>`__ Int.

Basic Solution
--------------

We define a process *memory* to manage the shared memory. In the basic
solution, this *memory* process has two communication channels of `Data
Type <https://github.com/TorXakis/TorXakis/wiki/Data_Type>`__ Int: Read
and Write. This *memory* process is a recursive process, with one
parameter: the current memory value. The process

-  either provides the current value over the Read channel,
-  or receives a new value over the Write channel. Since reading a value
   from memory doesn't change its value, after reading, the *memory*
   process is instantiated with the current memory value. Since writing
   a value to memory changes its value, after writing, the *memory*
   process is instantiated with the new value.

::

   PROCDEF memory [ Read, Write :: Int ] ( value :: Int ) ::=
           Read  ! value     >->  memory [Read, Write]( value )
       ##
           Write ? newValue  >->  memory [Read, Write]( newValue )
   ENDDEF

The *memory* process is used as follows, with initial value 0:

::

   PROCDEF usage [ Read, Write :: Int ] ( ) ::=
           memory [ Read, Write ] ( 0 )
       |[ Read, Write ]|
           someProcesses [ Read, Write ] ()
   ENDDEF

where someProcesses contains read statements like

======================== ==================================================
Statement                Action
======================== ==================================================
``Read ? x``             *Read the value in memory*
``Read ! 0``             *Read the memory when the value is zero*
``Read ? x [[ x < 0 ]]`` *Read the memory when the value is less then zero*
======================== ==================================================

and write statements like

=========================== =========================================
Statement                   Action
=========================== =========================================
``Write ! 123``             *Write 123 to memory*
``Write ? x``               *Write an arbritrary value to memory*
``Write ? x [[ x > 123 ]]`` *Write a value larger than 123 to memory*
=========================== =========================================

See the example
`ReadWriteConflict <https://github.com/TorXakis/TorXakis/tree/develop/examps/ReadWriteConflict>`__
for more details.

Advanced Solution
-----------------

In the advanced solution, the *memory* process has only one
communication channel: Memory. This communication channel has as `Data
Type <https://github.com/TorXakis/TorXakis/wiki/Data_Type>`__
MemoryAccess which is defined as follows

::

   TYPEDEF MemoryAccess ::= Read  { value :: Int }
                          | Write { newValue :: Int }
   ENDDEF

The *memory* process is still a recursive process, with one parameter:
the current memory value. The process

-  either provides the Read constructor with the current value over the
   Memory channel,
-  or receives a Write constructor with the new value over the Memory
   channel. Since reading a value from memory doesn't change its value,
   after reading, the *memory* process is instantiated with the current
   memory value. Since writing a value to memory changes its value,
   after writing, the *memory* process is instantiated with the new
   value.

::

   PROCDEF memory [ Memory :: MemoryAccess ] ( value :: Int ) ::=
           Memory ! Read ( value )     >->  memory [Memory](value)
       ##
           Memory ? x [[ isWrite(x) ]] >->  memory [Memory](newValue(x))
   ENDDEF

The *memory* process is used as follows, with initial value 0:

::

   PROCDEF usage [ Memory :: MemoryAccess ] ( ) ::=
           memory [ Memory ] ( 0 )
       |[ Memory ]|
           someProcesses [ Memory ] ()
   ENDDEF

where someProcesses contains read statements like

================================================ ==================================================
Statement                                        Action
================================================ ==================================================
``Memory ? x [[ isRead(x) ]]``                   *Read the value in memory*
``Memory ! Read(0)``                             *Read the memory when the value is zero*
``Memory ? x [[ isRead(x) /\ (value(x) < 0) ]]`` *Read the memory when the value is less then zero*
================================================ ==================================================

and write statements like

====================================================== =========================================
Statement                                              Action
====================================================== =========================================
``Memory ! Write(123)``                                *Write 123 to memory*
``Memory ? x [[ isWrite(x) ]]``                        *Write an arbritrary value to memory*
``Memory ? x [[ isWrite(x) /\ (newValue(x) > 123) ]]`` *Write a value larger than 123 to memory*
====================================================== =========================================

Using Test Purposes
-------------------

In order to be able to use Test Purposes for this case, we need to be
able to identify end states. If we add a way to identify who accesses a
memory cell at a certain point, then we can also use it to signal an end
state. Let's define MemoryAccess and the cell that is accessed
separately:

::

   TYPEDEF MemoryAccess ::= MemoryAccess { identity :: String; value :: Int }
   ENDDEF

   PROCDEF cell [ Read, Write :: MemoryAccess ] ( value :: Int ) ::=
           Read ? ma [[ value (ma) == value]] >-> cell [Read, Write ] (value)
       ##
           Write ? ma >->  cell [Read, Write] (value (ma))
   ENDDEF

The *cell* process is used as follows, with initial value 0:

::

   PROCDEF usage [ Read, Write :: MemoryAccess ] ( ) ::=
           cell [ Read, Write ] ( 0 )
       |[ Read, Write ]|
           someProcess[ Read, Write ] ( )
   ENDDEF

where someProcesses is similar to ones in previous examples but also
contains read statements that signals end states:

=========================================== =====================================================================
Statement                                   Action
=========================================== =====================================================================
``Read ? ma [[ identity (ma) == "Final"]]`` *Read the value in memory by a process that is identified as "Final"*
=========================================== =====================================================================

Let's create a Model for this ``usage``:

::

   CHANDEF Channels ::=
       Read, Write, Dummy :: MemoryAccess
   ENDDEF

   MODELDEF Model ::=
       CHAN IN Dummy
       CHAN OUT  Read, Write

       BEHAVIOUR
                 system [ Read, Write ] ( )
   ENDDEF

   CNECTDEF  Sut ::=
       CLIENTSOCK

       CHAN OUT Dummy                   HOST "localhost"  PORT 7776
       ENCODE   Dummy ? s               -> ! toString(s)
       CHAN IN  Read                    HOST "localhost"  PORT 7777
       DECODE   Read ! fromString(s)    <- ? s
       CHAN IN  Write                   HOST "localhost"  PORT 7778
       DECODE   Write ! fromString(s)   <- ? s
   ENDDEF

   CNECTDEF  Sim ::=
       SERVERSOCK

       CHAN IN   Dummy                   HOST "localhost"  PORT 7776
       DECODE    Dummy ! fromString(s)   <- ? s
       CHAN OUT  Read                    HOST "localhost"  PORT 7777
       ENCODE    Read ? b                ->  ! toString(b)
       CHAN OUT  Write                   HOST "localhost"  PORT 7778
       ENCODE    Write ? b               ->  ! toString(b)
   ENDDEF

Both ``Read`` and ``Write`` channels are output channels but we also
need a simulator in order to run Test Purposes, and simulator needs an
input channel in order to run properly. Hence, the ``Dummy`` channel.

Now we can write a Test Purpose that manipulates the inputs and observes
the outputs:

::

   PROCDEF output [Read, Write :: MemoryAccess](n :: Int) HIT ::=
           Read ! MemoryAccess ("Final",n) >-> HIT
       ##
           Read ? ma [[ (identity(ma) <> "Final") \/ (value(ma) <> n)]] >-> output [Read, Write](n)
       ##
           Write ? ma >-> output [Read, Write](n)
   ENDDEF

   PURPDEF TestPurpose ::=
       CHAN IN   Dummy
       CHAN OUT  Read, Write

       GOAL Hit1 ::= output [Read, Write] (1)
       GOAL Hit2 ::= output [Read, Write] (2)
       GOAL Hit3 ::= output [Read, Write] (3)
   ENDDEF

This Test Purpose will run until ``someProcess`` process in the
``usage`` performs Read accesses with "Final" identity and each of the
given values (1,2 and 3), or given number of steps are performed by
`TorXakis <https://github.com/TorXakis/TorXakis/wiki/TorXakis>`__.

A sample implementation can be found in the example
`ReadWriteTestPurposes <ReadWriteTestPurposes.txs>`__.