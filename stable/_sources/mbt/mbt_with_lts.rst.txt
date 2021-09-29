Model-Based Testing with Labelled Transition Systems
====================================================

Labelled transition systems
---------------------------

Labelled transition systems (LTS) and
its variants constitute a powerful semantic model for describing and
reasoning about dynamic, reactive systems. An LTS is a structure
consisting of states with transitions, labelled with actions, between
them. The states model the states of the system; the labelled
transitions model the actions that a system can perform. Actions can be
inputs, outputs, or internal steps of the system. LTS-based testing
theory has developed over the years from a theory-oriented approach for
defining LTS equivalences to a theory that forms a sound basis for real
testing and industrially viable testing tools. In this section we first
sketch the evolution of LTS-based testing theory and then describe to
what extent ``TorXakis`` uses this theory.

Testing equivalences
--------------------

Testing theory for LTS started with using
testing to formalize the notion of behavioural equivalence for LTS. Two
LTSs show equivalent behaviour if there is no test that can observe the
difference between them. By defining appropriate formalizations for test
and observation this led to the theory of testing equivalences and
preorders for LTS  [R23]_. Different equivalences can then be defined by
choosing different formalizations of test and observation: more powerful
testers lead to stronger equivalences, and the other way around. In the
course of the years, many such variations were investigated, with
testers that can observe the occurrence of actions, the refusal of
actions, or the potentiality of doing actions, testers that can undo
actions, that can make copies of the system state, or that can repeat
tests indefinitely. Comparative concurrency semantics systematically
compares these and other equivalences and preorders defined over LTS [R1,
32, 33, 46, 53]. Crucial in these equivalences is the notion of
*non-determinism*, i.e., that after doing an action in an LTS the
subsequent state is not uniquely determined. For deterministic systems
almost all equivalences coincide  [R28]_.

Test generation
---------------

Whereas the theory of testing equivalences and
preorders is used to define semantic relations over LTS using all
possible tests, actual testing turns this around: given an LTS *s* (the
specification) and a relation **imp** over LTS (the implementation
relation), determine a (minimal) set of tests p **imp** (*s*) that
characterizes all implementations *i* with *i* **imp** *s*, i.e., *i*
passes p **imp** (*s*) iff *i* **imp** *s*.

First steps towards systematically constructing such a test suite (sets
of tests) from a specification LTS led to the *canonical tester* theory
for the implementation relation **conf**  [R16]_. The intuition of **conf**
is that after traces, i.e., sequences of actions, that are explicitly
specified in the specification LTS, the implementation LTS shall not
unexpectedly refuse actions, i.e., the implementation may only refuse a
set of actions if the specification can refuse this set, too. This
introduces *under-specification*, in two ways. First, after traces that
are not in the specification LTS, anything is allowed in the
implementation. Second, the implementation may refuse less than the
specification.

Inputs and outputs
------------------

The canonical tester theory and its variants
make an important assumption about the communication between the
``sut`` and the tester, viz. that this communication is synchronous and
symmetric. Each communication event is seen as a joint action of the
``sut`` and the tester, inspired by the parallel composition in process
algebra. This also means that both the tester and the ``sut`` can block
the communication, and thus stop the other from progressing. In
practice, however, it is different: actual communication between an
``sut`` and a tester takes place via inputs and outputs. Inputs are
initiated by the tester, they trigger the ``sut``, and they cannot be
refused by the ``sut``. Outputs are produced by the ``sut``, and they
are observed and cannot be refused by the tester.

A first approach to a testing theory with inputs and outputs was
developed by interpreting each action as either input or output, and by
modelling the communication medium between ``sut`` and tester
explicitly as a queue  [R63]_. Later this was generalized by just assuming
that inputs cannot be refused by the ``sut``– the ``sut`` is assumed to
be *input-enabled*, i.e., in each state there is a transition for all
input actions – and outputs cannot be refused by the tester, akin to
I/O-automata  [R48]_. Adding these assumptions to the concepts of the
canonical tester theory and **conf** – refusal sets of the
implementation shall be refusal sets of the specification, but only for
explicitly specified traces – leads to a new implementation relation
that was coined **ioconf**  [R60]_. The assumptions that the
``sut`` cannot refuse inputs and the tester cannot refuse outputs makes
that the only relevant refusal that remains is refusing all possible
outputs by the ``sut``, which is called *quiescence*  [R64]_. Intuitively,
quiescence corresponds to observing that there is no output of the
``sut``, which is an important observation in testing theory as well as
in practical testing.

Implementation relation ioco
-----------------------------

In **ioconf** the test will stop after
observing quiescence, i.e., during each test run quiescence occurs at
most once, as the last observation. Phalippou noticed that in practical
testing quiescence is observed as a time-out during which no output from
the ``sut`` is observed, and that after such a time-out testing
continues with providing a next input to the ``sut``, so that quiescence
can occur multiple times during a test run  [R52]_. Inspired by this
observation, *repetitive quiescence* was added to **ioconf**, leading to
the implementation relation **ioco**
(**i** nput-**o** utput-**co** nformance) [R61]_ [R62]_. Theoretically,
**ioco** is akin to failure-trace preorder with inputs and outputs  [R46]_.
Intuitively, **ioco** expresses that an ``sut`` conforms to its
specification if the ``sut`` never produces an output that cannot be
produced by the specification in the same situation, i.e., after the
same trace. *Quiescence* is treated as a special, virtual output,
actually expressing the absence of real outputs, which is observed in
practice as a time-out during which no output from the ``sut`` is
observed. A small modification to **ioco** is the weaker implementation
relation **uioco**  [R8]_, where not the outputs after all traces are
considered, but only after those traces where inputs in the trace cannot
be refused. The relation **uioco** was shown to enjoy much nicer
mathematical properties and to deal more accurately with
under-specification  [R43]_.

The **ioco** and **uioco**-implementation relations support partial
models, under-specification, abstraction, and non-determinism. The
testability hypothesis is that an ``sut`` is assumed to be modelled as
an *inputenabled* LTS, that is, any input to the implementation is
accepted in every state. Specifications are not necessarily
input-enabled. Inputs that are not accepted in a specification state are
considered to be underspecified: no behaviour is specified for such
inputs, implying that any behaviour is allowed in the ``sut``. Models
that only specify behaviour for a small, selected set of inputs are
partial models. Abstraction is supported by modelling actions or
activities of systems as internal steps, without giving any details.
Non-deterministic models may result from such internal steps, from
having transitions from the same state labelled with the same action, or
having states with multiple outputs (output non-determinism).
Non-determinism leads to having a set of possible, expected outputs
after a sequence of actions, and not just a single expected output. The
``sut`` is required to implement at least one of these outputs, but not
all of them, thus supporting implementation freedom.

For **ioco** and **uioco**-testing, there are test generation algorithms
that are proved to be *sound* – all **ioco**/**uioco**-correct
``sut`` s pass all generated tests – and *exhaustive* – all
**ioco**/**uioco**-incorrect ``sut`` s are eventually detected by some
generated test. Consequently, the **ioco** and **uioco**-testing theory
constitutes, on the one hand, a well-defined theory of model-based
testing, whereas, on the other hand, it forms the basis for various
practical MBT tools. In particular, the implementation relation **ioco**
is the basis for a couple of MBT tools, such as ``TGV``  [R44]_, the
``Agedis Tool Set``  [R35]_, ``TorX``  [R6]_, ``JTorX``  [R5]_, Uppaal-Tron [R38]_,
TESTOR  [R49]_, Axini Test Manager (ATM) [R3]_ [R9]_, and ``TorXakis``.

A couple of variations have been proposed for **ioco** and **uioco**,
such as **mioco** for multiple input and output channels  [R37]_, **wioco**
that diminishes the requirements on input enabledness  [R66]_, various
variants of timed-**ioco** [R15]_ [R38]_ [R45]_, **qioco** for quantitative
testing  [R10]_, and **sioco** for LTS with data [R29]_ [R30]_.

Data
----

The **ioco**/**uioco**-testing theory for labelled transition
systems mainly deals with the dynamic aspects of system behaviour, i.e.,
with state-based control flow. The static aspects, such as data
structures, their operations, and their constraints, which are part of
almost any real system, are not covered. *Symbolic Transition Systems*
(STS) add (infinite) data and data-dependent control flow, such as
guarded transitions, to LTS, founded on first order logic [R29]_  [R30]_.
Symbolic **ioco** (**sioco**) lifts **ioco** to the symbolic level. The
semantics of STS and **sioco** is given directly in terms of LTS; STS
and **sioco** do not add expressiveness but they provide a way of
representing and manipulating large and infinite transition systems
symbolically.

TorXakis
--------

``TorXakis`` is rooted in the **ioco**-testing theory for
labelled transition systems. Its implementation relation is **ioco** and
the testability hypothesis is that an ``sut`` is assumed to be modelled
as an input-enabled LTS. Test generation is sound for **ioco** and in
the exhaustive, i.e., any non-conforming ``sut`` will eventually, after
unbounded time, be detected. ``TorXakis`` implements the **ioco**-test
generation algorithm for symbolic transition systems, and it uses a
process-algebraic modelling language ``Txs`` inspired by the language
LOTOS [R11]_ [R42]_, which is supplemented with an algebraic data-type
specification formalism.
