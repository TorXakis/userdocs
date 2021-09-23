TorXakis: A Model-Based Testing Tool
====================================

``TorXakis`` is a tool for model-based testing. This section gives a
high-level overview of ``TorXakis``. The next sections will illustrate
``TorXakis`` with a couple of examples. ``TorXakis`` is open source
software and is freely available under a BSD3 license  [R58]_.

Basics
------

Features
~~~~~~~~

``TorXakis`` implements the **ioco**-testing theory for
labelled transition systems. More specifically, it implements test
generation for symbolic transition systems (STS) following the
on-the-fly **sioco** test generation algorithm described in  [R29]_. This
means that conformance in ``TorXakis`` is precisely defined by the
**ioco**-implementation relation, the testability hypothesis is that
``sut`` s behave as inputenabled labelled transition systems, and test
generation is sound and, in the limit, exhaustive. Being based on the
**ioco**-theory, ``TorXakis`` supports uncertainty and abstraction
through non-determinism, and partial and under-specification.

``TorXakis`` emphasizes *formal*, *specification-based*, *active*,
*black-box* model-based testing of *functionality* of *dynamic,
data-intensive, reactive systems*. Reactive systems react to external
events (stimuli, triggers, inputs) with output events (responses,
actions, outputs)  [R54]_. In dynamic systems, outputs depend on inputs as
well as on the system state. Data-intensive means that instances of
complex data structures are communicated in inputs and outputs, and that
state transitions may involve complex computations and constraints.

``TorXakis`` is an on-the-fly (on-line) MBT tool which means that it
combines test generation and test execution: generated test steps are
immediately executed on the ``sut`` and responses from the ``sut`` are
immediately checked and used when calculating the next step in test
generation.

Currently, only random test selection is supported, i.e.,
``TorXakis`` chooses a random action among the possible inputs to the
``sut`` in the current state. This involves choosing among the
transitions of the STS and choosing a value from the (infinite,
constrained) data items attached to the transition. The latter involves
constraint solving. To direct and set goals for testing, the selection
can be restricted using user-specified *test purposes*  [R67]_.

``TorXakis`` is an experimental MBT tool, used in research, education,
and some case studies and experiments in industry.
``TorXakis`` currently misses good usability, scalability does not
always match the requirements of complex systems, and test selection is
still mainly random, but more sophisticated selection strategies are
being investigated [R12]_ [R13]_. ``TorXakis`` does not support
probabilities, real-time, or hybrid properties in system models.

Modelling
~~~~~~~~~

Labelled transition systems or symbolic transition
systems form a well-defined semantic basis for modelling and model-based
testing, but they are not directly suitable for writing down models
explicitly. Typically, realistic systems have more states than there are
atoms on earth (which is estimated to be approximately 10 :sup:`50`) so
an explicit representation of states is impossible. What is needed is a
language to represent large labelled transition systems. *Process
algebras* have semantics in terms of labeled transition systems, they
support different ways of composition, such as choice, parallelism,
concurrency, sequencing, etc., and they were heavily investigated in the
eighties  [R50]_ [R39]_ [R42]_. They are a good candidate to serve as a notation
for LTS models.

``TorXakis`` uses its own process-algebraic language
``Txs`` (pronounced *t`ex`es*) to express models. The language is
strongly inspired by the process-algebraic language ``Lotos`` [R11]_ [R42]_,
and incorporates ideas from ``Extended Lotos``  [R16]_ and mCRL2  [R34]_,
combined with plain state-transition systems. The semantics is based on
STS, which in turn has semantics in LTS. Having its roots in process
algebra, the language is compositional. It has several operators to
combine transition systems: sequencing, choice, parallel composition
with and without communication, interrupt, disable, and abstraction
(hiding). Communication between processes can be multi-way, and actions
can be built using multiple labels.

Since symbolic transition systems (STS) combine state-based control flow
with possibly infinite, complex data structures  [R30]_, the
process-algebraic part is complemented with a data specification
language based on algebraic data types (ADT) and functions like in
functional languages. In addition to user-defined ADTs, predefined data
types such as booleans, unbounded integers, and strings are provided.

Implementation
~~~~~~~~~~~~~~

``TorXakis`` is based on the model-based testing
tools ``TorX``  [R6]_ and ``JTorX``  [R5]_. The main additions are data
specification and manipulation with algebraic data types, and its own,
welldefined modelling language. Like ``TorX`` and ``JTorX``,
``TorXakis`` generates tests by first unfolding the process expressions
from the model into a *behaviour tree*, on which primitives are defined
for generating test cases. Unlike ``TorX`` and ``JTorX``,
``TorXakis`` does not unfold data into all possible concrete data
values, but it keeps data symbolically. Unfolding of process expressions
is similar to the LOTOS simulators HIPPO [R27]_ [R59]_ and SMILE  [R26]_.

In order to manipulate symbolic data and solve constraints for test-data
generation, ``TorXakis`` uses SMT solvers (Satisfaction Modulo
Theories)  [R22]_. Currently, Z3 and CVC4 are used via the SMT-LIBv2.5
standard interface  [R21]_  [R4]_ [R20]_. Term rewriting is used to evaluate data
expressions and functions.

The well-defined process-algebraic basis with **ioco** semantics makes
it possible to perform optimizations and reductions based on equational
reasoning with testing equivalence, which implies **ioco**-semantics.

The core of ``TorXakis`` is implemented in the functional language
Haskell  [R36]_, while parts of ``TorXakis`` itself have been tested with
the Haskell MBT tool QuickCheck  [R19]_.

Innovation
~~~~~~~~~~

Compared to other model-based testing tools
``TorXakis`` deals with some of the important challenges posed in Sect.
2: it offers support for test generation from non-deterministic models,
it deals with abstraction, partial models and under-specification, it
supports concurrency and parallelism, it enables composition of complex
models from simpler models, and it combines constructive modelling in
transition systems with property-oriented specification via data
constraints.

Usage overview
--------------

In this section we give  an overview of the general usage of ``TorXakis``.
In later chapters we discuss its usage in more details, and in the Examples
chapter we discuss the usage of ``TorXakis`` to learn a specific example in detail.


Test architecture
~~~~~~~~~~~~~~~~~

In order to use ``TorXakis``, we need a *System Under Test* (``sut``), a
*model* specifying the required and allowed behaviour of the ``sut``,
and an *adapter* (also called test harness, wrapper, testing glue, or
test scaffolding) to connect the actual ``sut`` to the test tool
``TorXakis``; see in :numref:`Image of Test architecture (Fig. %s) <fig_usage_testarchitecture>`.


.. _fig_usage_testarchitecture:
.. figure:: images/testarchitecture.*
   :alt: Test architecture
   :align: center

   Test architecture


System under test
~~~~~~~~~~~~~~~~~

The ``sut`` is the actual program, compoenent,
or system that we wish to test. The ``TorXakis`` view of an ``sut`` is
a black-box communicating with messages on its interfaces. Interfaces
can be distinguished as either an input interface, where the environment
takes the initiative and the system always accepts the action
(input-enabledness; black arrows going into the ``sut`` in Fig. 4), or
an output interface, where the system takes the initiative and the
environment always accepts (input-enabledness of the environment for the
output actions of the system; black arrows going out of the ``sut`` in
Fig. 4). Interfaces are modelled as *channels* in ``Txs``. So, an input
is a message sent by the tester to the ``sut`` on an input channel; an
output is the observation by the tester of a message from the
``sut`` on an output channel.

An instance of behaviour of the ``sut`` is a possible sequence of input
and output actions. The goal of testing is to compare the actual
behaviour that the ``sut`` exhibits with the behaviour specified in the
model.

Figure 4: Test architecture.

Technically, channels are implemented as plain old sockets where
messages are line-based strings, or string-encodings of some typed data.
So, technically, the ``TorXakis`` view of an ``sut`` is a black-box
communicating with strings on a couple of sockets.

Model
~~~~~

The model is written in the ``TorXakis`` modelling language
``Txs``. A model consists of a collection of definitions. There are
channel, data-type, function, constant, process, and state-automaton
definitions, which are contained in one or multiple files. In addition,
there are some testing-specific definition: connections and
en/decodings. A connection definition defines how ``TorXakis`` will
connect to the ``sut`` for test execution. It can been as a proxy for
the ``sut``: it specifies the binding of abstract channels in the model
to concrete sockets. En/decodings specify the mapping of abstract
messages (ADTs) to strings and vice versa. The next sections will
explain the details of modelling using some examples.

The model shall specify the allowed behaviour of the ``sut``, i.e., the
allowed sequences of input and output actions exchanged on its channels.
The basic structure to describe the allowed sequences is a
state-transition system with data, called *state-automaton* in ``Txs``.
These state-transition systems can be composed using combinators
(process-algebraic operators), so that complex state-transition systems
can be constructed from simple ones. Combinators include sequencing of
transition systems, choice, guards, parallelism, synchronization,
communication, interrupt, disable, and abstraction (hiding of actions).

The data items used in these state-transition systems are either of
standard data types such as integer, boolean, or string, or they are
user-defined algebraic data-type definitions. Also functions and
constants over data can be defined.

Adapter
~~~~~~~

``TorXakis`` communicates with the ``sut`` via sockets,
so either the ``sut`` must offer a socket interface – which a lot of
real-life ``sut`` s don’t do – or the ``sut`` must be connected via an
adapter, wrapper, test harness, or glueing software, that interfaces the
``sut`` to ``TorXakis``, and that transforms the native communication
of the ``sut`` to the socket communication that ``TorXakis`` requires.
Usually, such an adapter must be manually developed. Sometimes it is
simple, e.g., transforming standard I/O into socket communication using
standard (Unix) tools like ``netcat`` or ``socat``. Sometimes, building
an adapter can be quite cumbersome, e.g., when the ``sut`` provides a
GUI. In this case tools like ``Selenium``  [R56]_ or ``Sikuli``  [R57]_ may
be used to adapt a GUI or a web interface to socket communication. An
adapter is not specific for MBT but is required for any form of
automated test execution. If traditional test automation is in place
then this infrastructure can quite often be reused as adapter for MBT.

Even when a ``sut`` communicates over sockets, there is still a caveat:
sockets have asynchronous communication whereas models and test
generation assume synchronous communication. This may lead to race
conditions if a model offers the choice between an input and an output.
If this occurs the asynchronous communication of the sockets must be
explicitly modelled, e.g., as queues in the model.

Testing
~~~~~~~

Once we have an ``sut``, a model, and an adapter, we can
use ``TorXakis`` to run tests. The tool performs on-the-fly testing of
the ``sut`` by automatically generating test steps from the model and
immediately executing these test steps on the ``sut``, while observing
and checking the responses from the ``sut``. A test case may consist of
thousands of such test steps, which makes it also suitable for
reliability testing, and it will eventually lead to a verdict for the
test case.

Other features
~~~~~~~~~~~~~~

Other functionality of ``TorXakis`` includes
calculation of data values, constraint solving for data variables,
exploration of a model without connecting to an ``sut`` (closed
simulation), and simulation of a model in an environment, i.e.,
simulation while connected to the outside world (open simulation).
