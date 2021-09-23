Introduction to Model-Based Testing
====================================

Software Testing
-----------------
Software quality is a matter of increasing
importance and growing concern. Systematic testing plays an important
role in the quest for improved quality and reliability of software
systems. Software testing, however, is often an error-prone, expensive,
and time-consuming process. Estimates are that testing consumes 30-50%
of the total software development costs. The tendency is that the effort
spent on testing is still increasing due to the continuing quest for
better software quality, and the ever growing size and complexity of
systems. The situation is aggravated by the fact that the complexity of
testing tends to grow faster than the complexity of the systems being
tested, in the worst case even exponentially. Whereas development and
construction methods for software allow the building of ever larger and
more complex systems, there is a real danger that testing methods cannot
keep pace with these construction and development methods, so that these
new systems cannot sufficiently fast and thoroughly be tested anymore.
This may seriously hamper the development and testing of future
generations of software systems.

Model-Based Testing
-------------------

Model-Based Testing (MBT) is one of the
technologies to meet the challenges imposed on software testing. With
MBT a System Under Test (``sut``) is tested against an abstract model of
its required behaviour. This model serves as the system specification
and is the starting point for testing. It prescribes what the
``sut`` should, and what it should not do, that is, the behaviour of
the ``sut`` shall conform to the behaviour prescribed in the model. The
model itself is assumed to be correct and valid; it is not the direct
subject of testing or validation.

The main virtue of MBT is that the model is a perfect basis for the
generation of test cases, allowing test automation that goes well beyond
the mere automatic execution of manually crafted test cases. MBT allows
for the algorithmic generation of large amounts of test cases, including
test oracles for the expected results, completely automatically, from
the model of required behaviour. Moreover, if this model is valid, i.e.,
expresses precisely what the system under test should do, all these
generated tests are provably valid, too.

From an industrial perspective, model-based testing is a promising
approach to detect more bugs faster and cheaper. The current state of
practice is that test automation mainly concentrates on the automatic
execution of tests, but that the problem of test generation is not
addressed. Model-based testing aims at automatically generating
high-quality test suites from models, thus complementing automatic test
execution.

From an academic perspective, model-based testing is a formal-methods
approach to testing that complements formal verification and model
checking. Formal verification and model checking intend to show that a
system has specified properties by proving that a model of that system
satisfies these properties. Thus, any verification is only as good as
the validity of the model on which it is based. Model-based testing, on
the other hand, starts with a (verified) model, and then aims at showing
that the real, physical implementation of the system behaves in
compliance with this model. Due to the inherent limitations of testing,
such as the limited number of tests that can be performed in a
reasonable time, testing can never be complete: ”testing can only show
the presence of errors, not their absence”  [R24]_.

Benefits of model-based testing
-------------------------------

Model-based testing makes it
possible to generate test cases automatically, enabling the next step in
test automation. It makes it possible to generate more, longer, and more
diversified test cases with less effort, whereas, being based on sound
algorithms, these test cases are provably valid. Since a model specifies
both the possibe stimuli (inputs) to the ``sut`` and the allowed
responses (outputs), the generated test cases contain inputs to be
provided to the ``sut`` as well as outputs expected from the ``sut``,
which leads to better test oracles and less misinterpretation of test
results.

Creating models for MBT usually already leads to better understanding of
system behaviour and requirements and to early detection of
specification and design errors. Moreover, constructing models for MBT
paves the way for other model-based methods, such as model-based
analysis, model checking, and simulation, and it forms the natural
connection to model-based system development that is becoming an
important driving force in the software industry.

Test suite maintenance, i.e., continuously adapting test cases when
systems are modified, is an important challenge of any testing process.
In MBT, maintenance of a multitude of test cases is replaced by
maintenance of a model. Also diagnosis, i.e., localizing the fault when
a failure is detected, is facilated through model-based diagnostic
analysis. Finally, various notions of (model-) coverage can be
automatically computed, expressing the level of completeness of testing,
and allowing better selection of test cases.

Altogether, MBT is a promising approach to detect more bugs faster and
cheaper, and thus to improve the quality and reliability of the system
under test.

Sorts of model-based testing
----------------------------

There are different kinds of testing,
and thus of model-based testing, depending on the kind of models being
used, the quality characteristics being tested, the level of formality
involved, the degree of accessibility and observability of the system
being tested, and the kind of system being tested. Here, we consider
model-based testing as *formal*, *specification-based*, *active*,
*black-box*, *functionality testing* of *reactive systems*.

It is *testing*, because it involves checking some properties of the
``sut`` by systematically performing experiments on the real, running
``sut``. as opposed to, e.g., formal verification, where properties are
checked on a model of the system. The kind of properties being checked
are concerned with *functionality*, i.e., testing whether the system
correctly does what it should do in terms of correct responses to given
stimuli. as opposed to, e.g., performance, usability, reliability, or
maintainability properties. Such classes of properties are often
referred to as *quality characteristics*  [R41]_.

We do *specification-based*, *black-box* testing. The ``sut`` is seen
as a black box without internal detail, which can only be accessed and
observed through its external interfaces, as opposed to white-box
testing, where the internal structure of the ``sut``, i.e., the code, is
the basis for testing. The externally observable behaviour of the system
is compared with what has been specified in the model.

The testing is *active*, in the sense that the tester controls and
observes the ``sut`` in an active way by giving stimuli and triggers to
the ``sut``, and observing its responses, as opposed to passive testing,
or monitoring. Our ``sut`` s are *dynamic, data-intensive, reactive
systems*. Reactive systems react to external events (stimuli, triggers,
inputs) with output events (responses, actions, outputs). In dynamic
systems, outputs depend on inputs as well as on the system state.
Data-intensive means that instances of complex data structures are
communicated in inputs and outputs, and that state transitions may
involve complex computations and constraints.

Finally, we deal with *formal testing*: the model, which serves as
specification prescribing the desired behaviour is written in some
formal language with precisely defined syntax and semantics. Moreover,
there is a formal, well-defined theory underpinning these models,
``sut`` s, tests, and their relations, in particular, the correctness
(conformance) of ``sut`` s with respect to models, and the validity of
tests with respect to models. This enables formal reasoning about
*soundness* and *exhaustiveness* of test generation algorithms and the
generated test suites, i.e., that tests exactly test what they should
test.

In another form of model-based testing, called *statistical model-based
testing*, models do not prescribe required behaviour of the ``sut``, but
they describe how users use a system. Such models are called
*statistical usage profiles*, operational profiles, or customer
profiles. The idea is that tests are selected based on the expected
usage of the ``sut``, so that behaviours that are more often used, are
more thoroughly tested  [R55]_. Such models are derived from usage
information such as usage logs. Statistical model-based testing enables
the comprehensive field of statistics to be used with the goal of
assessing the reliability of systems.

Theory for model-based testing
-------------------------------

A theory for model-based testing
must, naturally, first of all define the models that are considered. The
modelling formalism determines the kind of properties that can be
specified, and, consequently, the kind of properties for which test
cases can be generated. Secondly, it must be precisely defined what it
means for an ``sut`` to conform to a model. Conformance can be
expressed using an *implementation relation*, also called *conformance
relation*  [R17]_. Since the ``sut`` is considered as a black box, its
behaviour is unknown and we cannot construct a model that precisely
describes the behaviour of the ``sut``, yet, we do assume that such a
model, though unknown, exists in a domain of implementation models. This
assumption is commonly referred to as the *testability hypothesis*, or
*test assumption*  [R31]_. The testability hypothesis allows reasoning
about ``sut`` s as if they were formal models, and it makes it possible
to define the implementation relation as a formal relation between the
domain of specification models and the domain of implementation models.
Soundness of test suites, i.e., do all correct ``sut`` s pass, and
exhaustiveness, i.e., do all incorrect ``sut`` s fail, are defined with
respect to an implementation relation.

In the domain of testing reactive systems there are two prevailing
‘schools’ of formal model-based testing. The oldest one uses
Mealy-machines, also called finite-state machines (FSM); see [R18]_  [R47]_,
51]. Here, we concentrate on the other one that uses *labelled
transition systems* (LTS) for modelling. A labelled transition system is
a structure consisting of states with transitions, labelled with
actions, between them. The states model the system states; the labelled
transitions model the actions that a system can perform. There is a rich
and well-understood theory for MBT with LTS, which is elaborated in
Sect. 3. Other approaches to MBT for non-reactive systems include
abstract-data-type based testing  [R7]_ and *property-based testing*, of
which the tool ``QuickCheck`` is the prime example  [R19]_. Originally
developed for ``Haskell``, property-based testing is now applied for
many languages.

Labelled transition systems form a well-defined semantic basis for
modelling and model-based testing, but they are not suitable for writing
down models explicitly. Typically, realistic systems have more states
than there are atoms on earth (which is approximately 10 :sup:`50`) so
an explicit representation of states is impossible. What is needed is a
language to represent large labelled transition systems. *Process
algebras* have semantics in terms of labeled transition systems, they
support different ways of composition such as choice, parallelism,
sequencing, etc., and they were heavily investigated in the eighties
[R50]_ [R39]_ [R42]_. They are a good candidate to serve as a notation for LTS
models.

Model-based testing challenges
------------------------------

Software is anywhere, and ever more
systems depend on software: software controls, connects, and monitors
almost every aspect of systems, be it a car, an airplane, a pacemaker,
or a refrigerator. Consequently, overall system quality and reliability
are more and more determined by the quality of the embedded software.
Typically, such software consists of several million lines of code, with
complex behavioural control-flow as well as intricate data structures,
with distribution and a lot of parallelism, having complex and
heterogeneous interfaces, and controlling diverse, multidisciplinary
processes. Moreover, this software often comes in many variants with
different options and for different platforms. It is continuously
evolving and being modified to adapt to different environments and new
user requirements, while increasing in size, complexity, connectivity,
and variability. Software is composed into larger systems and
systems-of-systems, whereas system components increasingly originate
from heterogeneous sources: there can be legacy, third-party,
out-sourced, off-the-shelf, open source, or newly developed components.

For model-based testing, these trends lead to several challenges. First,
the size of the systems implies that making complete models is often
infeasible so that MBT must deal with partial and under-specified models
and abstraction, and that partial knowledge and uncertainty cannot be
avoided. Secondly, the combination of complicated state-behaviour and
intricate input and output-data structures, and their dependencies, must
be supported in modelling. Thirdly, distribution and parallelism imply
that MBT must deal with concurrency in models, which introduces
additional uncertainty and non-determinism. In the fourth place, since
complex systems are built from sub-systems and components, and systems
themselves are more and more combined into systems-of-systems, MBT must
support compositionality, i.e., building complex models by combining
simpler models. Lastly, since complexity leads to an astronomical number
of potential test cases, test selection, i.e., how to select those tests
from all potential test cases that can catch most, and most important
failures, within constraints of testing time and budget, is a key issue
in model-based testing.

In short, to be applicable to testing of modern software systems, MBT
shall support partial models, underspecification, abstraction,
uncertainty, state & data, concurrency, non-determinism,
compositionality, and test selection. Though several academic and
commercial MBT tools exist, there are not that many tools that support
all of these aspects.

Model-based testing tools
-------------------------

Model-based testing activities are too
laborious to be performed completely manually, so, for MBT to be
effective and efficient, tool support is necessary. A large number of
MBT tools exist, as a Web-search will immediately show. ``TorXakis`` is
one of these MBT tools.

``TorXakis`` is a proof-of-concept, research tool that is being
developed by the Radboud University Nijmegen, the University of Twente,
and ESI (TNO) in the Netherlands. It is an on-line (on-the-fly) MBT tool
for formal, specification-based, active, black-box, functionality
testing of reactive systems, rooted in the **ioco**-testing theory for
labelled-transition systems [R61]_ [R62]_. It implements the **ioco**-test
generation algorithm for symbolic transition systems  [R30]_, and it uses a
process-algebraic modelling language ``Txs`` inspired by the language
LOTOS [R11]_ [R42]_, which is supplemented with an algebraic data-type
specification formalism, for which rewriting and SMT solvers are used
for calculation and manipulation  [R22]_. Moreover, ``TorXakis`` deals
with most of the challenges posed in the previous paragraph: it supports
modelling of state-based control flow together with complex data, it
deals with non-determinism, abstraction, partial models and
under-specification, concurrency, and composition of complex models from
simpler models. ``TorXakis`` supports state & data but no
probabilities, real-time, or hybrid systems. Test selection is primarily
random, but guidance can be provided using *test purposes*.
``TorXakis`` is an experimental MBT tool, used in (applied) research,
education, and industrial case studies and experiments.
``TorXakis`` currently misses good usability, scalability does not
always match the requirements of complex systems-of-systems, and more
sophisticated test selection strategies are necessary but these are
being investigated  [R14]_.

Future developments
-------------------

Current MBT algorithms and tools can
potentially generate many more tests from a model than can ever be
executed. Consequently, *test selection* is one of the major research
issues in model-based testing. Test selection concerns the problem of
finding criteria for selecting from the astronomical number of potential
test cases those tests that have the largest chance of detecting most,
and the most important bugs, with the least effort. Random approaches,
which are often used for small systems, do not suffice for large and
complex systems: the probability of completely randomly selecting an
important test case within the space of all possible behaviours
converges to zero. At the other end from random there is the explicit
specification of test purposes, i.e., a tester specifies explicitly what
she wishes to test, but that requires a lot of manual effort, and,
moreover, how should the tester know what to test. Different approaches
have been identified for determining what the “most important
behaviours” are, such as testing based on system requirements, code
coverage, model coverage, risk analysis, error-impact analysis, or
expected user behaviour (statistical usage profiles, or operational
profiles).

Related to apriori test selection, is aposteriori coverage, quality, and
confidence in the tested system. Since exhaustive testing is practically
impossible, the question pops up what has been achieved after testing:
can the coverage of testing, the quality of the tested ``sut``, or the
confidence in correct functioning of the ``sut``, somehow be formalized
and quantified? It is not to be expected that these fundamental research
questions will soon be completely solved.

MBT is an interesting technique once a model of the ``sut`` is
available. Availability of behavioural models, however, is one of the
issues that currently prohibits the widespread application of MBT. In
the first place, there is the question of making and investing in
models: there is reluctance against investing in making models, being
considered as yet another software artifact. Secondly, mastering the art
of behavioural modeling requires education and experience that is not
always available. Thirdly, the information necessary to construct a
model, in particular for legacy, third-party, or out-sourced systems or
components, is not always (easily) available.

These issues lead to the question whether models can be generated
automatically, e.g., for use in regression testing or testing systems
after refactoring. Model generation from an ``sut``, a kind of black-box
reverse engineering, (re)constructs a model by observing the behaviour
of the ``sut``, either passively from system logs, or actively by
performing special tests. This activity is called *model learning*, also
known as testbased modeling, automata learning, or grammatical
inference, and it is currently a popular research topic [R65]_.

New software testing methodologies are needed if testing shall keep up
with software development and meet the challenges imposed on it,
otherwise we may not be able to test future generations of systems.
systems. Model-based testing may be one of them.
