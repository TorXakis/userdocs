.. _helloworld_example:

=======================================================================
TorXakis Hello World Example
=======================================================================

``code:``  https://github.com/TorXakis/examples/tree/main/HelloWorld


Traditionally, the first program, in this case the first model, made in
a new language is the famous *Hello World!* program. Since the original
*Hello World!* program is rather easy to test, we take a slight
variation: our *Hello World!* initially prints ``Hello World!``, and
then continues with waiting for a <name> as input, after which it
outputs “Hello <name>”, and then these two last actions are repeated.

In order to use ``TorXakis`` to test *Hello World!* we need a *System
Under Test* (``SUT``), i.e., an executable program showing the above
described *Hello World!* behaviour, a *model* in the ``Txs``-language
specifying the allowed behaviour of the *Hello World!* system, and a
test *adapter* to connect the ``SUT`` to ``TorXakis``; see :numref:`fig_testarchitecture_helloworld`.
We can then use ``TorXakis`` to test whether the behaviour of the
``SUT`` complies with the behaviour specified in the model.

.. _fig_testarchitecture_helloworld:
.. figure:: testarchitecture.*
   :alt: Test architecture
   :align: center

   Test architecture

SUT
---

Our ``SUT`` is an executable program that is
claimed to behave according the *Hello World!* description given above.
Our task is to test whether this ``SUT`` indeed behaves as prescribed.
The ``SUT`` can be implemented in any language: we consider black-box
testing, which means that we only consider its input-output behaviour.
Our *Hello World!* ``SUT`` is a `C-program <https://raw.githubusercontent.com/TorXakis/examples/main/HelloWorld/sutC/HelloWorld.c>`_ with a simple line-oriented
user interface that communicates via standard input/output.


.. code-block:: sh

    $ gcc -o HelloWorld HelloWorld.c $ ./HelloWorld
    Hello World!
    Jan
    Hello Jan! Pierre
    Hello Pierre! ...


Adapter
-------

We now consider a test adapter for *Hello
World!*. Since the ``SUT`` commmunicates via standard input/output and
``TorXakis`` communicates via plain old sockets, this means that we
have to convert standard input/output communication to socket
communication. In a Linux-like environment this can be done using
standard utilities like ``netcat nc`` or ``socat``:

.. code-block:: sh

    $ socat TCP4-LISTEN:7890 EXEC:"./HelloWorld"

Using ``socat``, a socket-server connection is opened on port 7890. Data
on this connection is forwarded to/from standard input/output for
executable ``HelloWorld``. So, ``socat`` constitutes the test adapter
for *Hello World!*. The ``TorXakis`` view of the *Hello World!* program
is a black box receiving names, i.e, strings of characters, on socket
with port number 7890, and sending responses, being also strings, on the
same socket.

Model
-----

Now it is time to construct a model in the
``TorXakis`` modelling language ``Txs``. The description above says
that, after an initial ``Hello World!``, the system shall repeatedly
receive names and then output ``Hello`` with that name. The behaviour
is represented in the state automaton ``STAUTDEF helloWorld`` in :numref:`fig_yed_helloworld`;
the complete model including all additional definitions is shown in :numref:`fig_txs_helloworld`.

.. _fig_yed_helloworld:
.. figure:: yed_model_helloworld.*
   :alt: State automaton for Hello World!
   :figwidth: 70%
   :align: center

   State automaton for Hello World! (`Hstaut.graphml <https://raw.githubusercontent.com/TorXakis/examples/main/HelloWorld/modelH/Hstaut.graphml>`_)


In :numref:`fig_yed_helloworld`, there are three states: the initial state ``init``, the state
``noname`` when no name has been entered yet, and state
``named`` after a name has been entered. The transition from *init* to
*noname* specifies the welcoming message: on channel ``Outp`` the
message ``"Hello World!"`` is produced. The exclamation mark
``"!"`` indicates that a fixed value, i.e., the string
``"Hello World!"``, shall be ouput. The channel ``Outp`` is an ouput
channel from the point of view of the *Hello World!* system. When
testing, it will be an input for ``TorXakis``, i.e., ``TorXakis`` will
observe this message.

Once in state ``noname``, the next possible action is an input message
on channel ``Inp`` leading to state ``named``. The part
``? n :: String`` indicates that the input message shall be of type
``String`` and that the actual input is bound to the local variable
``n``. Moreover, the input message must satisfy the constraint given
between ``[[`` and ``]]``. This is a regular-expression constraint, it
is expressed with the standard function ``strinre`` (*str* ing *in
r* egular *e* xpression), and it requires that ``n`` starts with a
capital letter followed by one or more small letters. The final part of
this input transition, ``name := n``, assigns the actual message that is
communicated, i.e., the value of ``n``, to the state variable ``name``,
so that it can be later used in other transitions. The variable
``n`` is local to the transiton, whereas the state variable
``name`` is global in the whole state automaton.

Once in state *named* the next possible transition is going back to
*noname* while emitting on output channel

``Outp`` the message, that is, the string concatenation
``"Hello " ++ name ++ "!"``, where ``name`` refers to the state
variable containing the value obtained in the preceding transition.

An additional node in :numref:`fig_yed_helloworld`, which is not a state, gives the
declaration of the state automaton as a ``STAUTDEF``. It declares the
name of the state automaton, its channels with message types,
parameters, states, state variables, initial state, and the initial
values of the state variables,


.. code-block:: txs
   :caption: Txs model of *Hello World!* (`HelloWorld.txs <https://raw.githubusercontent.com/TorXakis/examples/main/HelloWorld/modelH/HelloWorld.txs>`_)
   :name: fig_txs_helloworld

    STAUTDEF helloWorld [ Inp, Outp :: String ] ( )
    ::=
        STATE
            init, noname, named
        VAR
            name :: String
        INIT
            init { name := "" }
        TRANS
            init	-> Outp ! "Hello World!"	-> noname
            noname -> Inp ? n [[ strinre(n, REGEX(’[A-Z][a-z]+’)) ]] { name := n } -> named
            named	-> Outp ! "Hello " ++ name ++ "!"	-> noname
    ENDDEF

    CHANDEF Chans
    ::=
        Input :: String ;
        Output :: String
    ENDDEF

    MODELDEF Hello
    ::=
        CHAN IN	Input
        CHAN OUT Output
        BEHAVIOUR
            helloWorld [Input, Output] ()
    ENDDEF

    CNECTDEF Sut
    ::=
        CLIENTSOCK

        CHAN OUT Input	HOST "localhost" PORT 7890
        ENCODE	Input	? s -> ! s

        CHAN IN	Output HOST "localhost" PORT 7890
        DECODE	Output ! s <- ? s
    ENDDEF



In ``Txs``, the input language for ``TorXakis``, this model is given in
:numref:`fig_txs_helloworld`. The model contains 4 definitions. The first one, ``STAUTDEF``,
defines a *state automaton*, and is directly generated from :numref:`fig_yed_helloworld`. The
second definition ``CHANDEF`` defines two channels with messages of
type ``String``. Thirdly, the overall model is defined in
``MODELDEF Hello``. It specifies which channels are inputs, which are
outputs, and it specifies the behaviour of the model instantiating the
state automaton ``helloWorld`` with appropriate channels and
parameters.

Lastly, the ``CNECTDEF`` specifies that the tester connects as client
to the ``SUT`` (the server) via sockets. It binds the channel
``Input``, which is an input of the model and of the ``SUT``, thus an
*output* of ``TorXakis``, to the socket ``localhost:7890``.
Moreover, an encoding of actions to strings on the socket can be
defined, but in this case, the encoding is trivial. Analogously, outputs
from the ``SUT``, i.e., inputs to ``TorXakis``, are read from socket ``localhost:7890`` and decoded.

Testing
--------

Now we are ready to perform a test, by running
the ``SUT`` with its adapter and ``TorXakis`` as two separate
processes in two different windows. For the ``SUT`` we run:

.. code-block:: sh

    $ socat TCP4-LISTEN:7890 EXEC:"./HelloWorld"

For ``TorXakis`` we have:

.. code-block:: sh

    $ torxakis HelloWorld.txs
    TXS >> TorXakis :: Model-Based Testing
    TXS >> txsserver starting: "kubernetes.docker.internal" : 41873
    TXS >> Solver "z3" initialized : Z3 [4.8.5]
    TXS >> TxsCore initialized
    TXS >> LPEOps version 2019.07.05.02 TXS >> input files parsed:
    TXS >> ["HelloWorld.txs"]
    TXS >> tester Hello Sut
    TXS >> Tester started
    TXS >> test 7
    TXS >> .....1: OUT: Act { { ( Output, [ "Hello World!" ] ) } }
    TXS >> .....2: IN: Act { { ( Input, [ "Pu" ] ) } }
    TXS >> .....3: OUT: Act { { ( Output, [ "Hello Pu!" ] ) } }
    TXS >> .....4: IN: Act { { ( Input, [ "Busvccc" ] ) } }
    TXS >> .....5: OUT: Act { { ( Output, [ "Hello Busvccc!" ] ) } }
    TXS >> .....6: IN: Act { { ( Input, [ "Pust" ] ) } }
    TXS >> .....7: OUT: Act { { ( Output, [ "Hello Pust!" ] ) } }
    TXS >> PASS
    TXS >>


After having started ``TorXakis`` , we start the tester
with ``tester Hello Sut`` , expressing that we wish to test with
model ``Hello`` and ``SUT`` connection ``Sut`` , shown in the
model file in :numref:`fig_txs_helloworld`. Then we can test 7 test steps
with ``test 7`` and, indeed, after 7 test steps it stops with
verdict ``PASS`` . A test run of 7 steps is rather small; we could
have run for 100 , 000 steps or more. ``TorXakis`` generates inputs
to the ``SUT`` , such as ``( Input, [ ""Busvccc" ] )`` , with names
satisfying the regular expression constraint. These input names are
generated from the constraint by the SMT solver. Some extra
functionality has been added in ``TorXakis`` in order to generate
quasi-random inputs, which is not normally provided by an SMT solver.
Moreover, it is checked that the outputs,
such as ``( Output, [ "Hello Busvccc!" ] )`` , are correct.
