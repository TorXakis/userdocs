.. _adder_example:

=======================================================================
TorXakis Adder Example
=======================================================================

The directory ``examps/adder`` contains a TorXakis MBT example of a simple
arithmetic adder. The adder adds and subtracts two integers.

There are multiple specification files which present various approaches
for testing Adder:

-  Adder.txs
-  AdderStAut.txs
-  AdderPurposes.txs
-  AdderReplay.txs
-  ReplayProc.txs
-  MAdder.txs

Communication between TorXakis and SUT (Adder) occurs via sockets, where
the SUT acts as the server-side.

Inputs:

- Plus(<n>,<m>)
- Minus(<n>,<m>)

Output:

- <n+m> or <n-m>, respectively

Prerequisites
=============

Java installed: `http://java.com <http://java.com>`__

SUTs
====

.. _adderjava:

Adder.java
----------

Java SUT with a single adder, communicating as server via stream-mode
socket, with as argument.

Compile and execute SUT:

.. code-block:: sh

  $ javac Adder.java              # compile Adder
  $ java Adder <portnr>           # start Adder


Test SUT from another terminal window:

.. code-block:: sh

  $ telnet localhost <portnr>
  Plus(25,17)
  42
  ...


NOTE: For Windows perhaps better with ``putty`` instead of ``telnet``.

Models
======

.. _addertxs:

Adder.txs
---------

Includes

* two models

  #. Adder
  #. Adder3

* two SUT representations

  #. Sut
  #. Sut3

* one simulator specification (Sim)

1. Adder Model and Sut Connection
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TorXakis model for a single Adder, communicating via ``localhost:7890``.

Observe the behaviour of model
""""""""""""""""""""""""""""""

To observe the behaviour of model, you can use the stepper

.. code-block:: sh


        $ torxakis Adder.txs
        TXS >> stepper Adder
        TXS >> step 10
        TXS >> ...


Execute TorXakis against the actual SUT
"""""""""""""""""""""""""""""""""""""""

To execute TorXakis against the actual SUT, the SUT must first be running and listening on
port 7890. Run in a terminal window:

.. code-block:: sh

        $ java -cp Adder 7890

Then in a different terminal window run torxakis against the SUT:

.. code-block:: sh

        $ torxakis Adder.txs
        TXS >> tester Adder SutConnection
        TXS >> test 10
        TXS >> ...
        TXS >> help              # TorXakis help for more possibilities


2. Adder3 Model and Sut3 Connection:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TorXakis model for three parallel Adders, communicating via <localhost,7890> <localhost,7891> <localhost,7892>.

Observe the behaviour of model
""""""""""""""""""""""""""""""

To observe the behaviour of model, you can use the stepper

.. code-block:: sh


        $ torxakis Adder.txs
        TXS >> stepper Adder3
        TXS >> step 20
        TXS >> ...


Execute TorXakis against the actual 3 SUTs
""""""""""""""""""""""""""""""""""""""""""


Start the 3 SUTs by starting each SUT with its own specific port in a separate terminal window:

.. code-block:: sh

        # terminal window 1
        $ java -cp Adder 7891

        # terminal window 2
        $ java -cp Adder 7892

        # terminal window 3
        $ java -cp Adder 7893

Then in terminal window 4 run torxakis against the SUT:


.. code-block:: sh

        # terminal window 4
        $ torxakis Adder.txs
        TXS >> tester Adder3 Sut3
        TXS >> test 20
        TXS >> ...
        TXS >> help              # TorXakis help for more possibilities


AdderStAut.txs
--------------

This example defines same Adder model using State Automation instead of
a Procedure. Sut and Sim are exactly same with Adder.txs.

The  State Automation in the ``Adder.txs`` file is defined with the `STAUTDEF` declaration:

.. code-block:: txs

    STAUTDEF adder  [ Act :: Operation;  Res :: Int ] ( )
    ::=
      STATE  idle, calc

      VAR    statevar :: Int

      INIT   idle   { statevar := 0 }

      TRANS  idle  ->  Act ?opn [[ IF isPlus(opn) THEN    not (overflow (p1(opn)))
                                                       /\ not (overflow (p2(opn)))
                                                       /\ not (overflow (p1(opn)+p2(opn)))
                                                  ELSE False FI  ]]  { statevar := p1(opn)+p2(opn) }  ->  calc
             idle  ->  Act ?opn [[ IF isMinus(opn) THEN   not (overflow (m1(opn)))
                                                       /\ not (overflow (m2(opn)))
                                                       /\ not (overflow (m1(opn)-m2(opn)))
                                                   ELSE False FI ]]  { statevar := m1(opn)-m2(opn) }  ->  calc
             calc  ->  Res ! statevar   { }                                                           ->  idle

    ENDDEF






Observe the behaviour of model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To observe the behaviour of model, you can use the stepper

.. code-block:: sh


        $ torxakis AdderStAut.txs
        TXS >> stepper Adder
        TXS >> step 10
        TXS >> ...


Execute TorXakis against the actual SUT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To execute TorXakis against the actual SUT, the SUT must first be running and listening on
port 7890. Run in a terminal window:

.. code-block:: sh

        $ java -cp Adder 7890

Then in a different terminal window run torxakis against the SUT:

.. code-block:: sh

        $ torxakis AdderStAut.txs
        TXS >> tester Adder SutConnection
        TXS >> test 10
        TXS >> ...
        TXS >> help              # TorXakis help for more possibilities




Test Purposes
=============

.. _adderpurposestxs:

AdderPurposes.txs
-----------------

This file includes 3 example Test Purpose definitions for manipulating
inputs generated by TorXakis in order to achieve certain objectives
during testing.

:Purp1: Test Purpose with 4 Goals
:Purp2: Test Purpose with operand constraints
:Purp3: Test Purpose to continuously add 2 after a random starting value

Use the Test Purposes by loading them into torxakis together with the Model definition:

.. code-block:: sh

        $ torxakis Adder.txs AdderPurposes.txs
        TXS >> tester Adder Purp1
        TXS >> test 5
        TXS >> ...


.. _adderreplaytxs-and-replayproctxs:

AdderReplay.txs and ReplayProc.txs
----------------------------------

AdderReplay.txs includes a Test Purpose that replays a process of
predefined input values in order to replay a certain scenario. The
process has to be named as ``replayProc``. ReplayProc.txs includes such a
process with 100 steps.


Load Test Purpose and replay record together with Model definitions

.. code-block:: sh

  $ torxakis Adder.txs AdderReplay.txs ReplayProc.txs
          TXS >> tester Adder AdderReplay
          TXS >> test 101
          TXS >> ...

