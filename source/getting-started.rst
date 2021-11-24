

.. _chp_getting_started:

Getting started
===============

``TorXakis`` is a tool for Model-Based Testing (MBT). This section gives step-by-step instructions
for installation, for executing your first model-based test, and for detecting your first bug
with ``TorXakis``. As an example, we use an *integer queue*.


Get TorXakis running
---------------------

For model-based testing you first need the tool ``TorXakis``.
Download and install ``TorXakis`` for your favourite operation system using the instructions at the  :ref:`Installation chapter <installationchapter>`. After installation you can run ``TorXakis`` in a terminal window, with

.. code-block:: sh

    $ torxakis

You should get the ``TorXakis`` prompt:

.. code-block:: txscmd

    TXS >>

after which you can use various ``TorXakis`` commands; try
:ref:`h(elp) <torxakishelp>`  to get an overview of
possible commands, q(uit) to quit ``TorXakis``, and try evaluating an expression,
to check whether everything was successfully installed:

.. code-block:: txscmd

    TXS >> eval 42-17

.. _sec_testing_a_queue:

Testing a Queue
----------------

``code:``  https://github.com/TorXakis/examples/tree/main/Queue


A couple of examples for ``TorXakis`` usage
can be found on the :ref:`Examples chapter <exampleschapter>`.

One of the examples is the *Queue*, which we will now use to demonstrate the usage of ``TorXakis`` in this *getting
started* chapter.

Test architecture
~~~~~~~~~~~~~~~~~

For model-based testing you first need the tool ``TorXakis``, second, a :term:`System under Test (SUT)`
that is a Java program implementing the *queue*, third, a model specifying the behaviour
of the queue, fourth, a connection between the test tool and the ``SUT``.
When having all these ingredients, depicted
in :numref:`Image of Test architecture (Fig. %s) <figtestarchitecture>`  , then you can start running model-based tests.


.. _figtestarchitecture:
.. figure:: images/testarchitecture.*
   :alt: Test architecture
   :align: center

   Test architecture


The first thing needed for MBT is a  Model-Based Testing Tool, which in our case is ``TorXakis``.
The second thing you need for MBT is an ``SUT``, and third thing  a ``Model``.

System Under Test
~~~~~~~~~~~~~~~~~~~


``SUT`` is an abbreviation for *System under Test*, which
refers to a system that is being tested for correct operation

The *Queue* example has various models and ``SUTs``.
There is a Java implementation of the *Queue* in ``sut0/QueueServer0.java``,
which will be our ``SUT`` in these instructions.
The program is a *Queue*-implementation that offers its service via a plain old socket interface.
It accepts input ``Enq(x)`` (Enqueue) to put integer value ``x`` in the queue, and it
accepts input ``Deq`` (Dequeue) and then provides the first value from the queue as output.
See :numref:`figqueueofints`.

.. _figqueueofints:
.. figure:: images/queue.*
   :alt: A Queue of integers
   :align: center

   A Queue of integers



To experiment with the ``SUT``, compile it and run it, or use the precompiled version, and use the portnumber ``7890``.
To use the *Queue* we need to connect to it via the plain old socket interface using an application that
can communicate via sockets, e.g., ``telnet``, ``nc`` (``netcat``), or ``putty``. Start the Java-*Queue* in one window and
``telnet``, etc. in another, and connect them by choosing the same port number. |nl|


    .. parsed-literal::

                *User Window*                         *SUT Window*

           $ telnet localhost 7890             $ java -jar QueueServer0.jar 7890
           Trying 127.0.0.1...                 Waiting for tester
           Connected to localhost.             Tester connected.
           Escape character is ’ˆ]’.
                                               [ ]
           Enq(42)                             [ 42 ]
           Enq(-17)                            [ 42, -17 ]
           Deq                                 [ -17 ]
           42



.. commentblock
    .. figure:: images/test/table.*
       :alt: table from pdf
       :align: center

       table from pdf



.. https://docutils.sourceforge.io/docs/ref/rst/directives.html#table

.. .. tabularcolumns:: ll
.. commentblock
    .. table::
        :align: center
        :class: noborder

        ==========================       ==================================
        User Window                      SUT Window
        ==========================       ==================================
        $ telnet localhost 7890          $ java -jar QueueServer0.jar 7890
        Trying 127.0.0.1...              Waiting for tester
        Connected to localhost.          Tester connected.
        Escape character is ’ˆ]’.
                                         [ ]
        Enq(42)                          [ 42 ]
        Enq(-17)                         [ 42, -17 ]
        Deq                              [ -17 ]
        42
        ==========================       ==================================



.. commentblock
..   .. parsed-literal::
..
..               *User Window*                         *SUT Window*
..          --------------------------          ----------------------------------
..          $ telnet localhost 7890             $ java -jar QueueServer0.jar 7890
..          Trying 127.0.0.1...                 Waiting for tester
..          Connected to localhost.             Tester connected.
..          Escape character is ’ˆ]’.
..                                              [ ]
..          Enq(42)                             [ 42 ]
..          Enq(-17)                            [ 42, -17 ]
..          Deq                                 [ -17 ]
..          42
..


Model
~~~~~

In the *Queue*-example, there are also a couple of ``TorXakis`` models, written in the ``TorXakis`` modelling language ``Txs``.
One of them is `Queue.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Queue/modelQ/Queue.txs>`_.

You can view and edit the model in your favourite plain editor.
The model specifies an unbounded, first-in-first-out *Queue* of integers.
There are some comments in the file explaining the model; comments in ``Txs`` are either between ``{-`` and ``-}``, or
after ``--`` until end-of- line.

The state-transition system of the *queue* model is graphically represented as a ``Txs`` state automaton,
called ``STAUTDEF``, in :numref:`figqstaut`. In such a representation, the ``STAUTDEF`` declaration
is textually described and the transitions are visualized as a graph.



.. _figqstaut:
.. figure:: images/qstaut.*
   :alt: State automaton for the Queue.
   :figwidth: 70%
   :align: center

   State automaton for the Queue. (`Qstaut.graphml <https://raw.githubusercontent.com/TorXakis/examples/main/Queue/modelQ/Qstaut.graphml>`_)


You can copy the file ``Queue.txs`` to a new directory; also copy the file ``.torxakis.yaml`` that contains some ``TorXakis``
configuration information, to be modified later.
Now you can use ``TorXakis`` to step through the model, i.e., use the stepper-command on the ``TorXakis``-prompt,
followed by the ``step <n>`` command to specify how many steps you wish to make through the transitions of the
state-automaton. This will show a trace of possible of behaviour, i.e., a sequence of transitons,
as it is described in the model. The result looks like below; ’looks like’ because the sequence of actions
and the integer values are randomly chosen, so your result might differ a bit.

.. code-block:: txscmd

    $ torxakis Queue.txs

    TXS >> TorXakis :: Model-Based Testing

    TXS >> txsserver starting: "PC-21165.tsn.tno.nl" : 54888
    TXS >> Solver "z3" initialized : Z3 [4.8.5 - build hashcode b63a0e31d3e2]
    TXS >> TxsCore initialized
    TXS >> LPEOps version 2019.07.05.02 TXS >> input files parsed:
    TXS >> ["Queue0.txs"]
    TXS >> stepper Queue
    TXS >> Stepper started
    TXS >> step 7
    TXS >> .....1:NoDir:Act{{(In,[Enq(-1325)])}}
    TXS >> .....2:NoDir:Act{{(In,[Enq(0)])}}
    TXS >> .....3:NoDir:Act{{(In,[Enq(-1782)])}}
    TXS >> .....4:NoDir:Act{{(In,[Enq(-90992)])}}
    TXS >> .....5:NoDir:Act{{(In,[Enq(-75)])}}
    TXS >> .....6:NoDir:Act{{(In,[Deq])}}
    TXS >> .....7:NoDir:Act{{(Out,[-1325])}}
    TXS >> PASS
    TXS >>


Model-Based Testing of the Queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that we have a ``SUT`` - ``QueueServer0.java`` – and a model specifying the required behaviour of the ``SUT`` – ``Queue.txs`` –,
we can start testing the ``SUT`` against its model. To test the Queue, run the ``SUT`` in one window and start ``TorXakis``
with the model as input, in another window. When ``TorXakis`` gives its prompt, start testing with ``tester Queue Sut``,
that is, the tester-command with Queue as model, i.e., the ``MODELDEF`` in the model file ``Queue.txs``, and ``Sut`` as proxy
to the ``SUT``, i.e., the ``CNECTDEF`` in the model file. Upon ``tester Queue Sut`` ``TorXakis`` will connect directly to the ``SUT``,
so you do not need ``telnet``, etc. Then the command ``test 7`` specifies how many test steps will be taken; you can
easily try bigger numbers, e.g., ``test 7777``. Now you have executed your first successful test with ``TorXakis``!

.. code-block:: txscmd

    $ torxakis Queue0.txs

    TXS >> TorXakis :: Model-Based Testing

    TXS >> txsserver starting: "PC-21165.tsn.tno.nl" : 54890
    TXS >> Solver "z3" initialized : Z3 [4.8.5 - build hashcode b63a0e31d3e2]
    TXS >> TxsCore initialized
    TXS >> LPEOps version 2019.07.05.02
    TXS >> input files parsed:
    TXS >> ["Queue0.txs"]
    TXS >> tester Queue Sut
    TXS >> Tester started
    TXS >> test 7
    TXS >> .....1:In:Act{{(In,[Enq(-1953)])}}
    TXS >> .....2:In:Act{{(In,[Deq])}}
    TXS >> .....3:Out:Act{{(Out,[-1953])}}
    TXS >> .....4:In:Act{{(In,[Deq])}}
    TXS >> .....5:In:Act{{(In,[Enq(-1)])}}
    TXS >> .....6:In:Act{{(In,[Deq])}}
    TXS >> .....7:Out:Act{{(Out,[-1])}}
    TXS >> PASS
    TXS >>

A Queue Mutant
~~~~~~~~~~~~~~~

You have now tested the ``sutQueueServer0.java`` against its model, but ``QueueServer0.java`` does not
contain bugs (at least, as far as we know, but ... “testing can only show the presence of errors,
never their absence” [R24]_). Detecting bugs is probably more rewarding for testers, so we added in the
*Queue*-example three Queue mutants, small modifications in the Java program that may make the ``SUT`` buggy.
These mutants are ``sut1``, ``sut2``, and ``sut3``. You can test these ``SUT``’s with the same model to see whether
you can detect (and explain?) the bugs.

Utilities
------------

Notepad++ and Txs
~~~~~~~~~~~~~~~~~~~~~~~~

*Notepad++* is a free editor running in the MS Windows environment: `https://notepad-plus-plus.org <https://notepad-plus-plus.org>`_.
Syntax high-lighting for ``Txs`` is available for *Notepad++*.
Follow the installation instructions on: `https://github.com/TorXakis/SupportNotepadPlusPlus <https://github.com/TorXakis/SupportNotepadPlusPlus>`_ to
install the *Notepad++*-plugin for ``Txs``.


yEd and Txs
~~~~~~~~~~~~~~~~~

Models represent state-transition systems, which can intuitively be visualized as graphs. `yEd <https://www.yworks.com/products/yed>`_ is a powerfull, freely available graph editor that can be used to edit and (automatically) layout graphs, and that runs on Windows, Unix/Linux, and macOS. A translation from *yEd* to ``Txs`` is available. Follow the installation instructions on: `https://github.com/TorXakis/yed2stautdef <https://github.com/TorXakis/yed2stautdef>`_ to install the application ``yed2stautdef`` that translates *yEd*-output to a state-automaton definition ``STAUTDEF`` in ``Txs``.

For the *Queue*-example, a graph representing its state-transition system, is available in ``Qstaut.graphml``; actually, it is the graph of Fig. 2. This graph has three nodes and four edges. The edges represent the transitions in the state-transition system. Two nodes represent states and one node gives the declaration of the ``STAUTDEF``. The labels in the nodes representing states are the state names; the labels on the transitions specify actions in ``Txs`` syntax. The declaration node gives the name of the state automaton, its channels message types between ``[`` and ``]``, and optionally some parameters between ``(`` and ``)``. Moreover, there is the list of all states, the local variables with their types, and the initial state with initial values for the local variables. Nodes and edges can be formatted (colour, shape, lining, shadow, . . .) as wished; it does not matter for the transformation to ``Txs``.

The graph edited in *yEd* shall be saved in *Trivial Graph Format* ``TGF`` (``*.tgf``). The application ``yed2stautdef`` transforms a file in ``TGF``-format to a ``Txs``-file:

.. code-block:: sh

    $ yed2stautdef QueueGraph.tgf

The result is a ``STAUTDEF`` – a State Automaton Definition in the language ``Txs``:

.. code-block:: torxakis

    STAUTDEF queueStaut [ Inp :: QueueOp; Outp :: Int ] ( )
    ::=
        STATE
           qstate, qout
        VAR
           buf :: IntList
        INIT
            qstate { buf := Nil }
        TRANS
            qstate -> Inp ? qop [[ isDeq(qop) /\ not(isNil(buf)) ]] -> qout
            qout -> Outp ! hd(buf) { buf := tl(buf) } -> qstate
            qstate -> Inp ? qop [[ isEnq(qop) ]] { buf := add(val(qop),buf) } -> qstate
            qstate -> Inp ? qop [[ isDeq(qop) /\ isNil(buf) ]] -> qstate
    ENDDEF

A ``STAUTDEF`` can be included in a ``.txs``-file, or the file can be used as additional input file for ``TorXakis``; ``TorXakis``
allows multiple ``.txs`` input files. In ``Txs``, a ``STAUTDEF`` can used anywhere where a *process*, defined in a ``PROCDEF``, can be used.
Note that the graph should *also* be saved in the standard ``GRAPHML`` format (``.graphml``), because the ``TGF``-format,
as the name suggests, is a very trivial format, which does not preserve graph layout and formatting.
So, next time when you continue editing with *yEd* use the ``.graphml``-file and not the ``.tgf``-file.

The application ``yed2stautdef`` just transforms the ``.tgf``-file and does not check any syntax or static semantics.
Checking is only done on the ``.txs``-file, where error messages might appear. Finding the corresponding error spot in
the ``.graphml``-file is, for the moment, left to the user.
