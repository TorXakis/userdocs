Modelling Example: Stimulus Response
====================================

We want to test our `java
program <https://github.com/TorXakis/TorXakis/wiki/Java_program>`__
`StimulusResponse.java <StimulusResponse.java>`__. This is a simple
program that receives an input (Stimulus) and responds to it (Response).
All the files used in this example can be found at `the example
folder <https://github.com/TorXakis/TorXakis/tree/develop/examps/StimulusResponse>`__.

Channels
--------

This program (our System Under Test - SUT) receives a stimulus and
responds to it. Let's `define the
channels <https://github.com/TorXakis/TorXakis/wiki/ChanDefs>`__ needed
for modelling this behaviour:

::

   CHANDEF  Chans ::=  Stimulus; Response
   ENDDEF

Model
-----

The model should specify that the system uses two channels, one incoming
for the stimulus and one outgoing for the response. It should also
specify that first a stimulus and then a response are communicated. The
`Model
Definition <https://github.com/TorXakis/TorXakis/wiki/ModelDefs>`__ of
this system in TorXakis is as follows:

::

   MODELDEF Model ::=
       CHAN IN    Stimulus
       CHAN OUT   Response

       BEHAVIOUR
           Stimulus >-> Response
   ENDDEF

SUT Connection
--------------

Our SUT communicates with the outside world by sending and receiving
lines i.e. strings terminated by a line feed, over a socket at port
7890. When TorXakis and the SUT run on the same machine (localhost) the
`SUT connection <https://github.com/TorXakis/TorXakis/wiki/CnectDefs>`__
can be defined in TorXakis as follows:

::

   CNECTDEF  Sut ::=
       CLIENTSOCK

       CHAN  OUT  Stimulus            HOST "localhost"  PORT 7890
       ENCODE     Stimulus            ->  ! ""

       CHAN  IN   Response            HOST "localhost"  PORT 7890
       DECODE     Response            <-   ? s
   ENDDEF

Model Based Testing
-------------------

1. Start the SUT: run the `Java
   program <https://github.com/TorXakis/TorXakis/wiki/Java_program>`__
   in a command window.

``$> java StimulusResponse``

2. Start TorXakis: run the
   `TorXakis <https://github.com/TorXakis/TorXakis/wiki/TorXakis>`__
   with the StimulusResponse model describe above in another command
   window.

``$> torxakis StimulusResponse.txs``

3. Set the Model and SUT for testing: In TorXakis type the following
   commands:

``tester Model Sut``

4. Test the SUT: In TorXakis type the following command:

``test 3``

TorXakis will perform the two communication actions, Stimulus and
Response, observe that the system under test communicates no additional
output until TorXakis times out (as expected), and finally conclude:

::

   TXS >>  .....1: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....2: OUT: Act { { ( Response, [] ) } }
   TXS >>  .....3: OUT: No Output (Quiescence)
   TXS >>  PASS

Errorneous SUT
~~~~~~~~~~~~~~

1. Start the errorneous SUT: run the errorneous `Java
   program <https://github.com/TorXakis/TorXakis/wiki/Java_program>`__
   `StimulusNoResponse.java <StimulusNoResponse.java>`__ in a command
   window.

``$> java StimulusNoResponse``

2. Start TorXakis: run the
   `TorXakis <https://github.com/TorXakis/TorXakis/wiki/TorXakis>`__
   with the StimulusResponse model describe above in another command
   window.

``$> torxakis StimulusResponse.txs``

3. Set the Model and SUT for testing: In TorXakis type the following
   commands

``tester Model Sut``

4. Test the erroneous SUT: In TorXakis type the following command:

``test 3``

TorXakis will perform the first communication action: Stimulus. TorXakis
will observe that the expected second communication action (Response)
doesn't occur, causing the step to time out, so conclude:

::

   TXS >>  .....1: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....2: OUT: No Output (Quiescence)
   TXS >>  Expected:
   TXS >>  [ ( { Response[] }, [], [] ) ]
   TXS >>  FAIL: No Output (Quiescence)

Stimulus Response - Loop
------------------------

Let's change our system to run in a loop of waiting for next Stimulus,
instead of exiting after the first one. See
`StimulusResponseLoop.java <StimulusResponseLoop.java>`__ for the
updated Java code.

Our `channel
definitions <https://github.com/TorXakis/TorXakis/wiki/ChanDefs>`__
don't change:

::

   CHANDEF Model ::=   Stimulus, Response
   ENDDEF

Our `SUT
connection <https://github.com/TorXakis/TorXakis/wiki/CnectDefs>`__
stays the same, too:

::

   CNECTDEF  Sut ::=
       CLIENTSOCK

       CHAN  OUT  Stimulus            HOST "localhost"  PORT 7890
       ENCODE     Stimulus            ->  ! ""

       CHAN  IN   Response            HOST "localhost"  PORT 7890
       DECODE     Response            <-   ? s
   ENDDEF

In our `model
definition <https://github.com/TorXakis/TorXakis/wiki/ModelDefs>`__, we
need a way to define the looping behaviour. We can make use of a
recursive `procedure
definition <https://github.com/TorXakis/TorXakis/wiki/ProcDefs>`__ for
this:

::

   PROCDEF stimResp [ Stimulus, Response ] ()
       ::=
           Stimulus  >->  Response  >->  stimResp [Stimulus,Response] ()
   ENDDEF

Now we can use this `procedure
definition <https://github.com/TorXakis/TorXakis/wiki/ProcDefs>`__ in
our `Model <https://github.com/TorXakis/TorXakis/wiki/ModelDefs>`__:

::

   MODELDEF Model ::=
       CHAN IN    Stimulus
       CHAN OUT   Response

       BEHAVIOUR
           stimResp [Stimulus,Response] ()
   ENDDEF

Now we can run model based tests on test our new SUT:

1. Start the SUT: run the `Java
   program <https://github.com/TorXakis/TorXakis/wiki/Java_program>`__
   in a command window.

``$> java StimulusResponseLoop``

2. Start TorXakis: run the
   `TorXakis <https://github.com/TorXakis/TorXakis/wiki/TorXakis>`__
   with the StimulusResponse model describe above in another command
   window.

``$> torxakis StimulusResponseLoop.txs``

3. Set the Model and SUT for testing: In TorXakis type the following
   commands:

``tester Model Sut``

4. Test the SUT: In TorXakis type the following command:

``test 10``

TorXakis will perform the two communication actions, Stimulus and
Response, over and over again for as many test steps as we tell it to
(in this example: 10). Observing that SUT communicates a Response for
every Stimulus as expected, it will finally conclude:

::

   TXS >>  .....1: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....2: OUT: Act { { ( Response, [] ) } }
   TXS >>  .....3: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....4: OUT: Act { { ( Response, [] ) } }
   TXS >>  .....5: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....6: OUT: Act { { ( Response, [] ) } }
   TXS >>  .....7: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  .....8: OUT: Act { { ( Response, [] ) } }
   TXS >>  .....9: IN: Act { { ( Stimulus, [] ) } }
   TXS >>  ....10: OUT: Act { { ( Response, [] ) } }
   TXS >>  PASS
