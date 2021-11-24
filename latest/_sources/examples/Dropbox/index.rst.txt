=======================================================================
TorXakis Dropbox Example
=======================================================================

``code:``  https://github.com/TorXakis/examples/tree/main/Dropbox

We apply model-based testing with ``TorXakis`` to test Dropbox. Our
work closely follows the work in [R40]_, where Dropbox was tested with the
model-based testing tool Quviq QuickCheck. We first briefly introduce
Dropbox, we then discuss some aspects of the testing approach, we
present a model in the ``TorXakis`` modelling language, we run some
tests, and end with discussion.

Dropbox
---------------

Dropbox is a file-synchronization service [R25]_, like Google-Drive and
Microsoft-OneDrive. A file-synchronization service maintains consistency
among multiple copies of files or a directory structure over different
devices. A user can create, delete, read, or write a file on one device
and Dropbox synchronizes this file with the other devices. One copy of
the files on a device is called a *node* . A *conflict* arises when
different nodes write to the same file: the content of the file cannot
be uniquely determined anymore. Dropbox deals with conflicts by having
the content that was written by one node in the original file, and
adding an additional file, with a new name, with the conflicting
content. Also this additional file will eventually be synchronized.

Synchronization is performed by uploading and downloading files to a
Dropbox server, i.e., a Dropbox system with *n* nodes conceptually
consists of *n* +1 components. How synchronization is performed, i.e.,
when and which (partial) files are up- and downloaded by the Dropbox
clients and how this is administered is part of the Dropbox
implementation, i.e., the Dropbox protocol. Since we concentrate on
testing the delivered synchronization service, we abstract from the
precise protocol implementation.

A file synchronizer like Dropbox is a distributed, concurrent, and
nondeterministic system. It has state (the synchronization status of
files) and data (file contents), its modelling requires abstraction,
leading to nondeterminism, because the precise protocol is not
documented and the complete internal state is not observable, and
partial modelling is needed because of its size. Altogether, file
synchronizers are interesting and challenging systems to be tested,
traditionally as well as model-based.

Testing Approach
-------------------------

We test the Dropbox synchronization service, that is, the ``sut`` is
the Dropbox behaviour as observed by users of the synchronization
service, as a black-box. We closely follow [R40]_, where a formal model
for a synchronization service was developed and used for model-based
testing of Dropbox with the tool Quviq QuickCheck [R2]_, a descendant of
Haskell QuickCheck [R19]_. This means that we use the same test setup,
make the same assumptions, and transform their model for Quviq
QuickCheck to the ``TorXakis`` modelling language. It also means that
we will not repeat the detailed discussion of Dropbox intricacies and
model refinements leading to their final model, despite that their model
rules out implementations that calculate ``clean`` and handle a
reverting write action without any communication with the server.

Like in [R40]_, we restrict testing to one file and three nodes, and we
use actions ( ``sut`` inputs) ``Read`` *N* , ``Write`` *N* ,
and ``Stabilize`` , which read the file at node *N* , (over-)write
the file at node *N* , and read all files including conflict files
when the system is stable, i.e., fully synchronized, respectively.
Initially, and after deletion, the file is represented by the special
content value ” ``$`` ” (perpendicular in [R40]_).

Our test setup consists of three Linux-virtual machines with Dropbox
clients implementing the three nodes, numbered 0, 1, and 2. The file
manipulation on the nodes is performed by plain Linux shell commands.
These commands are sent by ``TorXakis`` , which runs on the host
computer, via sockets; see Sect. 4. The adapters
connecting ``TorXakis`` to the ``sut`` consist of a one-line shell
script connecting the sockets to the shell interpreter via the standard
Linux utility ``socat`` .

For ``Stabilize`` we assume that the system has stabilized, i.e., all
file synchronizations have taken place including distribution to all
nodes of all conflict files. Like in [R40]_, we implement this by simply
waiting for at least 30 seconds. Since the ``TorXakis`` modelling
language itself does not support realtime, ``TorXakis`` sends a
command to the adapter to wait for 30 seconds.

Modelling
----------------

Our Dropbox model is a straightforward translation of "Section IV:
Formalizing the specification" in [R40]_ into the modelling language
of ``TorXakis`` . Parts of the model are shown in Listings :numref:`fig_txs_dropbox_channels_types`,
:numref:`%s <fig_txs_dropbox_channels_types>`, :numref:`%s <fig_txs_dropbox_channels_types>`,
:numref:`%s <fig_txs_dropbox_channels_types>`, :numref:`%s <fig_txs_dropbox_channels_types>`,
:numref:`%s <fig_txs_dropbox_channels_types>`, and :numref:`%s <fig_txs_dropbox_channels_types>`


.. code-block:: txs
   :caption: Dropbox model - channels and their types. (`dropbox-ceciis19.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_channels_types

    CHANDEF MyChans ::=
        In0, In1, In2 :: Cmd ;
        Out0, Out1, Out2 :: Rsp
    ENDDEF

    TYPEDEF Cmd ::=
          Read
        | Write                       { value :: Value }
        | Stabilize
    ENDDEF

    TYPEDEF Rsp ::=
          Ack
        | NAck                         { error :: String }
        | File                          { value :: Value }
    ENDDEF

    TYPEDEF Value ::=
        Value { value :: String }
    ENDDEF

    FUNCDEF isValidValue ( val :: Value ) :: Bool ::=
        strinre( value(val), REGEX(’[A-Z]{1,3}’) )
    ENDDEF


A ``TorXakis`` model is a collection of different kinds of
definitions.  The first one, ``CHANDEF`` , defines the
channels with their typed messages; see  :numref:`Fig. %s <fig_txs_dropbox_channels_types>`. ``TorXakis`` assumes
that an ``sut`` communicates by receiving and sending typed messages.
A message received by the ``sut`` is an input, and thus an action
initiated by the tester. A message sent by the ``sut`` is
an ``sut`` output, and is observed and checked by the tester. For
Dropbox there are three input channels: ``In0`` , ``In1`` ,
and ``In2`` , where commands of type ``Cmd`` are sent to
the ``sut`` , for each node, respectively. There are also three output
channels ``Out0`` , ``Out1`` , and ``Out2`` , where responses of
type ``Rsp`` are received from the ``sut`` . The commands
( ``sut`` inputs) with their corresponding responses
( ``sut`` outputs) are:

``Read``
  reads the file on the local node, which leads to a response
  consisting of the current file content ``value``

``Write(value)``
  writes the new value ``value`` to the file while the
  response gives the old value

``Stabilize``
  reads all file values, i.e., the original file and all
  conflict files, after stabilization, i.e., after all file
  synchronizations have taken place.


.. _fig_dropbox_structure:
.. figure:: dropbox_structure.*
   :alt: Dropbox structure
   :align: center

   Dropbox structure.



In addition to these visible actions, there are hidden actions. If a
user modifies a file, Dropbox will upload it to the Dropbox server, and
then later download this file to the other nodes. But a Dropbox user,
and thus also the (black-box) tester cannot observe these actions, and
consequently, they do not occur in the ``CHANDEF`` definition. Yet,
these actions do occur and they do change the state of the Dropbox
system. We use six
channels ``Down0`` , ``Down1`` , ``Down2`` , ``Up0`` , ``Up1`` ,
and ``Up2`` to model these actions, and later it will be shown how we
can explicitly *hide* these channels. The conceptual structure of
Dropbox with nodes, server, and channels is given in Fig. 11. The outer
box is our ``sut`` .



.. code-block:: txs
   :caption: Dropbox model - main process ``dropbox`` with transitions ``Read`` and ``Write``. (`dropbox-ceciis19_.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_main_process

    PROCDEF dropBox [ In0,  In1,  In2     :: Cmd
                    ; Out0, Out1, Out2    :: Rsp
                    ; Down0, Down1, Down2
                    ; Up0, Up1, Up2
                    ]
                    ( serverVal :: Value
                    ; conflicts :: ValueList
                    ; localVal  :: ValueList
                    ; fresh     :: BoolList
                    ; clean     :: BoolList
                    )
      ::=
                In0     !Read
            >-> Out0    !File(lookup(localVal,Node(0)))
            >-> dropBox [ In0,In1,In2,Out0,Out1,Out2
                        , Down0,Down1,Down2,Up0,Up1,Up2
                        ]
                        ( serverVal
                        , conflicts
                        , localVal
                        , fresh
                        , clean
                        )
        ##
                In0     ?cmd [[ IF   isWrite(cmd)
                                THEN isValidValue(value(cmd))
                                ELSE False
                                FI ]]
            >-> Out0    !File(lookup(localVal,Node(0)))
            >-> dropBox [ In0,In1,In2,Out0,Out1,Out2
                        , Down0,Down1,Down2,Up0,Up1,Up2
                        ]
                        ( serverVal
                        , conflicts
                        , update(localVal,Node(0),value(cmd))
                        , fresh
                        , update(clean,Node(0),False)
                        )
        ##
             .......





The next step is to define the processes that model state behaviour. The
main process is ``PROCDEF dropbox`` which models the behaviour of
Dropbox, combining the commands ( ``sut`` inputs), responses
( ``sut`` outputs), and the checks on them in one state machine; see
Figs. 12, 13, and 14. The state machine is defined as a recursive
process ``dropbox`` with channel
parameters ``In0`` , *...* , ``Up2`` , and with state variables
exactly as in [R40]_:

* a global stable value ``serverVal`` represents the file value
  currently held on the server;

* a global set ``conflicts`` holds the conflicting file values,
  represented as a ``ValueList`` ;

* for each node *N* , there is a local file value ``localVal`` *N* ,
  where all local file values together are represented as a list of values
  with three elements, the first element
  representing ``localVal`` :sub:`0` , etc.;

* for each node *N* , there is a freshness value ``fresh`` *N* ,
  indicating whether node *N* has downloaded the latest value
  of ``serverVal`` ; all freshness values together are represented as a
  list of Booleans with three elements, the second element
  representing ``fresh`` :sub:`1` , etc.;

* for each node *N* , there is a cleanliness value ``clean`` *N* ,
  indicating whether the latest local modification has been uploaded;
  together they are represented as a list of Booleans with three elements,
  the third element representing ``clean`` :sub:`2` , etc.

The recursive process ``dropbox`` defines for each node transitions
for reading, writing, uploading, and downloading the file, and one
transition for ``Stabilize`` . The different transitions are separated
by ``’##’`` , the ``TorXakis`` *choice* operator. The transitions
for reading and writing consist of two steps: first a command
( ``sut`` input) followed by an ``sut`` output. ”Followed by” is
expressed by the ``TorXakis`` *action-prefix* operator ``’>->’`` .
After the response, ``dropbox`` is recursively called with updated
state variables.




.. code-block:: txs
   :caption: Dropbox model - transitions ``Down`` and ``Up`` in the main process ``dropbox``. (`dropbox-ceciis19__.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_main_transitions_down_up

          .....
        ##
            [[ not(lookup(fresh,Node(0)))
               /\  lookup(clean,Node(0)) ]]
            =>> Down0
            >-> dropBox [ In0,In1,In2,Out0,Out1,Out2
                        , Down0,Down1,Down2,Up0,Up1,Up2
                        ]
                        ( serverVal
                        , conflicts
                        , update(localVal,Node(0),serverVal)
                        , update(fresh,Node(0),True)
                        , clean
                        )
        ##
            [[ not(lookup(clean,Node(0))) ]]
            =>> Up0
            >-> dropBox [ In0,In1,In2,Out0,Out1,Out2
                        , Down0,Down1,Down2,Up0,Up1,Up2
                        ]
                        ( IF   lookup(fresh,Node(0))
                            /\ (lookup(localVal,Node(0)) <> serverVal)
                          THEN lookup(localVal,Node(0))
                          ELSE serverVal
                          FI
                        , IF   not(lookup(fresh,Node(0)))
                            /\ (lookup(localVal,Node(0)) <> serverVal)
                            /\ (lookup(localVal,Node(0)) <> Value("$"))
                          THEN Values(lookup(localVal,Node(0)),conflicts)
                          ELSE conflicts
                          FI
                        , localVal
                        , IF   lookup(fresh,Node(0))
                            /\ (lookup(localVal,Node(0)) <> serverVal)
                          THEN othersUpdate(fresh,Node(0),False)
                          ELSE fresh
                          FI
                        , update(clean,Node(0),True)
                        )
        ##
          .....




Consider file-reading for node 0 (Fig. 12). The first action is
input ``Read`` on channel ``In0`` . Then the ``sut`` will produce
output ``File(lookup(localVal,Node(0)))`` , i.e., the ``File`` made
by looking up the ``localVal`` value of ``Node(0)`` . This is an
expression in the data specification language of ``TorXakis`` , which
is based on algebraic data types (ADT) and functions like in functional
languages. This data language is very powerful, but also very
rudimentary. Data types such as ``ValueList`` have to be defined
explicitly as recursive types (Fig. 15), consisting of either an empty
list ``NoValues`` , or a non-empty list ``Values`` with as fields a
head value ``hd`` and a tail ``tl`` , which is again
a ``ValueList`` . Functions like ``lookup`` have to be defined
explicitly, too, in a functional (recursive) style. Fig. 15 gives as
examples the functions ``lookup`` and ``update`` ; other functions
are included in the full model [R58]_. After the output there is the
recursive call of process ``dropbox`` , where state parameters are not
modified in case of file-reading.


.. code-block:: txs
   :caption: Dropbox model - transition ``Stabilize`` and and process ``fileAndConflicts``. (`dropbox-ceciis19___.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_main_transitions_stabilize

    .....
        ##
            [[ allTrue(fresh) /\ allTrue(clean) ]]
            =>> (         In0  !Stabilize
                      >-> fileAndConflicts [Out0] (Values(serverVal,conflicts))
                  >>> dropBox [ In0,In1,In2,Out0,Out1,Out2
                              , Down0,Down1,Down2,Up0,Up1,Up2
                              ]
                              ( serverVal
                              , conflicts
                              , localVal
                              , fresh
                              , clean
                              )
                )
    ENDDEF   -- dropBox

    PROCDEF fileAndConflicts [ Out :: Rsp ] ( values :: ValueList ) EXIT
     ::=
                Out ?rsp [[ IF   isFile(rsp)
                            THEN isValueInList(values,value(rsp))
                            ELSE False
                            FI ]]
            >-> fileAndConflicts [Out] (removeListValue(values,value(rsp)))
        ##
            [[ isNoValues(values) ]]
            =>> Out !Ack
            >-> EXIT
    ENDDEF   -- fileAndConflicts


Writing a file for node 0 is analogous, but with two differences (Fig.
12). First, the action of writing is not a unique action, but it is
parameterized with the new file value. This is expressed by ``?cmd`` ,
stating that on channel ``In0`` any value, represented by
variable ``cmd`` , can be communicated, which satisfies the constraint
between ``’[[’`` and ``’]]’`` . This constraint expresses
that ``cmd`` must be a ``Write`` command, referring to the
constructor ``Write`` in type ``Cmd`` . Moreover, the ``value`` of
the ``write`` -command must be a valid value, which means (see Fig.
10) that it shall be a string contained in the regular
expression ``REGEX(’[A-Z]`` { ``1,3`` } ``’)`` , i.e., a string of
one to three capital letters. Using this constraint, ``TorXakis`` will
automatically generate valid input values, using an SMT solver.

The second difference concerns the updates to the state parameters in
the recursive call of ``dropbox`` . We see
that ``localVal`` for ``node(0)`` is updated with the new file value
that was used as input in the communication on channel ``In0`` .
Moreover, ``node(0)`` is not ``clean`` anymore.

The transitions for uploading and downloading will be hidden, so they do
not have communication with the ``sut`` . They just deal with
constraints and updates on the state. Downloading to node 0 (Fig. 13)
can occur if node 0 is not ``fresh`` yet ``clean`` , as is modelled
in the guard (precondition) between ``’[[’`` and ``’]] =>>’`` ,
before execution of action ``Down0`` . The effect of the action is an
update of the ``localVal`` of ``Node(0)`` with ``serverVal`` , and
re-established freshness.

Uploading can occur if a node is not ``clean`` . The state update is
rather intricate, which has to do with conflicts that can occur when
uploading, and with special cases if the upload is actually a delete
(represented by file value ``"$"`` ) and if the upload is equal
to ``serverVal`` . The state update has been directly copied from [R40]_
where it is very well explained, so for more details we refer there.


.. code-block:: txs
   :caption: Dropbox model - data types and functions. (`dropbox-ceciis19____.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_data_types_and_functions

    TYPEDEF Node
     ::=
          Node { node :: Int }
    ENDDEF

    TYPEDEF ValueList
     ::=
          NoValues
        | Values   { hd :: Value
                   ; tl :: ValueList
                   }
    ENDDEF

    FUNCDEF lookup ( vals :: ValueList; n :: Node ) :: Value
     ::=
        IF   isNoValues(vals)
        THEN Value("$")
        ELSE IF   node(n) == 0
             THEN hd(vals)
             ELSE lookup(tl(vals),Node(node(n)-1))
             FI
        FI
    ENDDEF

    FUNCDEF update ( vals :: ValueList; n :: Node; v :: Value ) :: ValueList
     ::=
        IF   isNoValues(vals)
        THEN NoValues
        ELSE IF   node(n) == 0
             THEN Values(v,tl(vals))
             ELSE Values(hd(vals),update(tl(vals),Node(node(n)-1),v))
             FI
        FI
    ENDDEF




We have discussed reading, writing, uploading, and downloading for node
0. Similar transitions are defined for nodes 1 and 2. Of course, in the
final model, parameterized transitions are defined for node *N* ,
which can then be instantiated. Since this parameterization is not
completely trivial because of passing of state variable values, we do
not discuss it here.

The last action is ``Stabilize`` , which can occur if all nodes
are ``fresh`` and ``clean`` ; see Fig. 14. Since all nodes are
assumed to have synchronized it does not matter which node we use; we
choose node 0. ``Stabilize`` produces all file content values that are
currently available including the conflict files. These content values
are produced one by one, in arbitrary order, as responses on
channel ``Out0`` with an acknowledge ``Ack`` after the last one.
Process ``fileAndConflicts`` models that all these content values
indeed occur once in the list of ``serverVal`` and ``conflicts`` .
It removes from ``Values`` (which is of type ``ValueList`` ) each
content value ``value(rsp)`` that has been observed on ``Out0`` ,
until the list is empty, i.e., ``isNoValues(values)`` holds. Then the
acknowledge ``Ack`` is sent, and the process ``EXIT`` s, which is
the trigger for the recursive call
of ``dropbox`` after ``fileAndConflicts`` .

The next step is to define the complete model in the ``MODELDEF`` ;
see Fig. 16. The ``MODELDEF`` specifies which channels are inputs,
which are outputs, and what the ``BEHAVIOUR`` of the model is using
the previously defined processes. In our case it is a call of
the ``dropbox`` process with appropriate instantiation of the state
variables ``serverVal`` , ``conflicts`` , ``localVal`` , ``fresh`` ,
and ``clean`` . Moreover, this is the place where the
channels ``Down0`` , *...* , ``Up2`` are hidden with the
construct ``HIDE[`` *channels* ``]IN`` *...* ``NI`` . Actions that
occur on hidden channels are *internal actions* (in process-algebra
usually denoted by *tau* ). They are not visible to the system
environment, but they do lead to state changes of which the consequences
can be visible, e.g., when a transition that is enabled before the
occurrence of *tau* is no longer enabled in the state after
the *tua* -occurrence. Visible actions, that is inputs and outputs, are
visible to the system environment. They lead to state changes both in
the system and in its environment.


.. code-block:: txs
   :caption: Dropbox model - definition of the model that specifies the behaviour over the observable channels. (`dropbox-ceciis19_____.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_def_model

    MODELDEF Mod
     ::=
        CHAN IN   In0,  In1,  In2
        CHAN OUT  Out0, Out1, Out2

        BEHAVIOUR
            preAmble [In0,In1,In2,Out0,Out1,Out2] ()
        >>>
            HIDE  [ Up0, Up1, Up2, Down0, Down1, Down2 ]
            IN
                dropBox [ In0,   In1,   In2
                        , Out0,  Out1,  Out2
                        , Down0, Down1, Down2
                        , Up0,   Up1,   Up2
                        ]
                        ( Value("$")
                        , NoValues
                        , Values(Value("$")
                                ,Values(Value("$")
                                       ,Values(Value("$"),NoValues)))
                        , Bools(True,Bools(True,Bools(True,NoBools)))
                        , Bools(True,Bools(True,Bools(True,NoBools)))
                        )
            NI
    ENDDEF







The last definition ``CNECTDEF`` specifies how the tester connects to
the external world via sockets; see Fig. 17. In the Dropbox
case, ``TorXakis`` connects as socket client, ``CLIENTSOCK`` , to
the ``sut`` , that shall act as the socket server.
The ``CNECTDEF`` binds the abstract model channel ``In0`` , which is
an input of the model and of the ``sut`` , thus
an *output* of ``TorXakis`` , to the socket on host ``txs0-pc`` ,
one of the virtual machines running Dropbox, and port
number ``7890`` . Moreover, the encoding of abstract messages of
type ``Cmd`` on channel ``In0`` to strings on the socket is
elaborated with function ``encodeCmd`` : a command is encoded as a
string of one or more Linux commands, which can then be sent to and
executed by the appropriate virtual machine. Analogously, outputs from
the ``sut`` , i.e., inputs to ``TorXakis`` , are read from socket
h ``txs0-pc`` *,* ``7890`` i and decoded to responses of
type ``Rsp`` on channel ``Out0`` using function ``decodeRsp`` .
Analogous bindings of abstract channels to real-world socksets are
specified for ``In1`` , ``Out1`` , ``In2`` , and ``Out2`` .


Model-Based Testing
----------------------------

Now that we have an ``sut`` and a model, we can start generating tests
and executing them. First, we start the ``sut`` , that is, the virtual
machines, start the Dropbox client on these machines, and start the
adapter scripts. Then we can start ``TorXakis`` and run a test; see
Fig. 18. User inputs to ``TorXakis`` are marked ``TXS <<`` ;
responses from ``TorXakis`` are marked ``TXS >>`` .

We start the tester with ``tester DropboxModel DropboxSut`` ,
expressing that we wish to test
with ``MODELDEF DropboxModel`` and ``CNECTDEF DropboxSut`` . Then we
test for 100 test steps with ``test 100`` , and indeed, after 100 test
steps it stops with verdict ``PASS`` .

``TorXakis`` generates inputs to the ``sut`` , such as on line
7: ``In0, [ Write(Value("SHK")) ] )`` , indicating that on
channel ``In0`` an input action ``Write`` with file
value ``"SHK"`` has occurred. The input file value is generated
by ``TorXakis`` from the ``isValidValue`` constraint, using the SMT
solver. This action is followed, on line 8, by an output from
the ``sut`` on channel ``Out0`` , which is the old file value of
Node 0, which is ``"$"`` , representing the empty
file. ``TorXakis`` checks that this is indeed the correct response.

Only visible input and output actions are shown in this trace. Hidden
actions are not shown, but they do occur internally, as can be seen, for
example, from line 24: the old file value on Node 2 was ``"X"`` , but
this value was only written to node 0 (line 11), so node 0 and node 2
must have synchronized the value ``"X"`` via
internal ``Up`` and ``Down`` actions. Also just
before ``Stabilize`` , lines 67–74, synchronization has obviously
taken place, which can only happen using
hidden ``Up`` and ``Down`` actions. Due to the distributed nature of
Dropbox and its nondeterminism it
is not so easy to check the response of the ``Stabilize`` command on
line 75. It is left to the reader to check that the outputs on lines
76–80 are indeed all conflict-file contents together with the server
file, and that ``TorXakis`` correctly assigned the
verdict ``PASS`` .




.. code-block:: txs
   :caption: Dropbox model - connection to the external world. (`dropbox-ceciis19______.txs <https://raw.githubusercontent.com/TorXakis/examples/main/Dropbox/dropbox-ceciis19.txs>`_)
   :name: fig_txs_dropbox_world

    CNECTDEF Sut
     ::=
         CLIENTSOCK

         CHAN OUT  In0   HOST "lubu0" PORT 7890
         ENCODE    In0   ?cmd            ->  !encodeCmd(cmd)

         CHAN IN   Out0  HOST "lubu0" PORT 7890
         DECODE    Out0  !decodeRsp(s)  <-  ?s

         CHAN OUT  In1   HOST "lubu1" PORT 7891
         ENCODE    In1   ?cmd            ->  !encodeCmd(cmd)

         CHAN IN   Out1  HOST "lubu1" PORT 7891
         DECODE    Out1  !decodeRsp(s)  <-  ?s

         CHAN OUT  In2   HOST "lubu2" PORT 7892
         ENCODE    In2   ?cmd            ->  !encodeCmd(cmd)

         CHAN IN   Out2  HOST "lubu2" PORT 7892
         DECODE    Out2  !decodeRsp(s)  <-  ?s
    ENDDEF

    FUNCDEF encodeCmd ( cmd :: Cmd ) :: String
     ::=
        IF   isRead(cmd)
        THEN "cat " ++ testfile
        ELSE
        IF   isWrite(cmd)
        THEN "cat " ++ testfile ++ " ; "
             ++ "echo \"" ++ value(value(cmd)) ++ "\" > " ++ testfile
        ELSE
        IF   isStabilize(cmd)
        THEN "sleep 30 ; cat * ; echo "
        ELSE
        IF   isChangeDir(cmd)
        THEN "cd " ++ testdir ++ " ; echo "
        ELSE ""
        FI FI FI FI
    ENDDEF

    FUNCDEF decodeRsp ( s :: String ) :: Rsp
     ::=
        IF   s == ""
        THEN Ack
        ELSE IF   s == "$"
             THEN File(Value("$"))
             ELSE IF   strinre(s,REGEX('[A-Z]+'))
                  THEN File(Value(s))
                  ELSE NAck(s)
                  FI
             FI
        FI
    ENDDEF



Many more test cases can be generated and executed
on-the-fly. ``TorXakis`` generates random test cases, so each time
another test case is generated, and appropriate responses are checked
on-the-fly. It should be noted that ``TorXakis`` is not very fast.
Constraint solving, nondeterminism, and dealing with internal (hidden)
actions (exploring all possible ’explanations’ in terms of [R40]_) can
make that computation of the next action takes a minute.


.. code-block::

    $ torxakis Dropbox.txs
    TXS >> TorXakis :: Model-Based Testing
    TXS >> txsserver starting: "PC-31093.tsn.tno.nl" : 60275
    TXS >> Solver "z3" initialized : Z3 [4.6.0]
    TXS >> TxsCore initialized
    TXS >> input files parsed:
    TXS >> ["Dropbox.txs"]
    TXS >> tester DropboxModel DropboxSut
    TXS >> tester started
    TXS >> test 100
    TXS >> .....1: IN: Act{{(In1,[Read])}}
    TXS >> .....2: OUT: Act { { ( Out1, [ File(Value("$")) ]
    TXS >> .....3: IN: Act{{(In2,[Read])}}
    TXS >> .....4: OUT: Act { { ( Out2, [ File(Value("$")) ]
    TXS >> .....5: IN: Act { { ( In1, [ Write(Value("P")) ]
    TXS >> .....6: OUT: Act { { ( Out1, [ File(Value("$")) ]
    TXS >> .....7: IN: Act { { ( In0, [ Write(Value("SHK"))
    TXS >> .....8: OUT: Act { { ( Out0, [ File(Value("$")) ]
    TXS >> .....9: IN: Act{{(In1,[Read])}}
    TXS >> ....10: OUT: Act { { ( Out1, [ File(Value("P")) ]
    TXS >> ....11: IN: Act { { ( In0, [ Write(Value("X")) ]
    TXS >> ....12: OUT: Act { { ( Out0, [ File(Value("SHK"))
    TXS >> ....13: IN: Act { { ( In2, [ Write(Value("A")) ]
    TXS >> ....14: OUT: Act { { ( Out2, [ File(Value("$")) ]
    TXS >> ....15: IN: Act { { ( In2, [ Write(Value("SP")) ] ) } }
    TXS >> ....16: OUT: Act { { ( Out2, [ File(Value("A")) ] ) } }
    TXS >> ....17: IN: Act { { ( In1, [ Write(Value("BH")) ] ) } }
    TXS >> ....18: OUT: Act { { ( Out1, [ File(Value("P")) ] ) } }
    TXS >> ....19: IN: Act{{(In2,[Read])}}
    TXS >> ....20: OUT: Act { { ( Out2, [ File(Value("SP")) ] ) } }
    TXS >> ....21: IN: Act{{(In0,[Read])}}
    TXS >> ....22: OUT: Act { { ( Out0, [ File(Value("X")) ] ) } }
    TXS >> ....23: IN: Act { { ( In2, [ Write(Value("PXH")) ] ) } }
    TXS >> ....24: OUT: Act { { ( Out2, [ File(Value("X")) ] ) } }
    TXS >> ....25: IN: Act{{(In2,[Read])}}
    TXS >> ....26: OUT: Act { { ( Out2, [ File(Value("PXH")) ] ) } }
    TXS >> ....27: IN: Act { { ( In0, [ Write(Value("AX")) ] ) } }
    TXS >> ....28: OUT: Act { { ( Out0, [ File(Value("PXH")) ] ) } }
    TXS >> ....29: IN: Act{{(In2,[Read])}}
    TXS >> ....30: OUT: Act { { ( Out2, [ File(Value("AX")) ] ) } }
    TXS >> ....31: IN: Act{{(In1,[Read])}}
    TXS >> ....32: OUT: Act { { ( Out1, [ File(Value("AX")) ] ) } }
    TXS >> ....33: IN: Act{{(In0,[Read])}}
    TXS >> ....34: OUT: Act { { ( Out0, [ File(Value("AX")) ] ) } }
    TXS >> ....35: IN: Act { { ( In2, [ Write(Value("TPH")) ] ) } }
    TXS >> ....36: OUT: Act { { ( Out2, [ File(Value("AX")) ] ) } }
    TXS >> ....37: IN: Act { { ( In0, [ Write(Value("X")) ] ) } }
    TXS >> ....38: OUT: Act { { ( Out0, [ File(Value("AX")) ] ) } }
    TXS >> ....39: IN: Act { { ( In2, [ Write(Value("CPH")) ] ) } }
    TXS >> ....40: OUT: Act { { ( Out2, [ File(Value("TPH")) ] ) } }
    TXS >> ....41: IN: Act { { ( In1, [ Write(Value("HX")) ] ) } }
    TXS >> ....42: OUT: Act { { ( Out1, [ File(Value("CPH")) ] ) } }
    TXS >> ....43: IN: Act{{(In1,[Read])}}
    TXS >> ....44: OUT: Act { { ( Out1, [ File(Value("HX")) ] ) } }
    TXS >> ....45: IN: Act{{(In1,[Read])}}
    TXS >> ....46: OUT: Act { { ( Out1, [ File(Value("HX")) ] ) } }
    TXS >> ....47: IN: Act { { ( In2, [ Write(Value("Q")) ] ) } }
    TXS >> ....48: OUT: Act { { ( Out2, [ File(Value("HX")) ] ) } }
    TXS >> ....49: IN: Act{{(In0,[Read])}}
    TXS >> ....50: OUT: Act { { ( Out0, [ File(Value("Q")) ] ) } }
    TXS >> ....51: IN: Act{{(In0,[Read])}}
    TXS >> ....52: OUT: Act { { ( Out0, [ File(Value("Q")) ] ) } }
    TXS >> ....53: IN: Act{{(In2,[Read])}}
    TXS >> ....54: OUT: Act { { ( Out2, [ File(Value("Q")) ] ) } }
    TXS >> ....55: IN: Act { { ( In0, [ Write(Value("K")) ] ) } }
    TXS >> ....56: OUT: Act { { ( Out0, [ File(Value("Q")) ] ) } }
    TXS >> ....57: IN: Act{{(In2,[Read])}}
    TXS >> ....58: OUT: Act { { ( Out2, [ File(Value("K")) ] ) } }
    TXS >> ....59: IN: Act{{(In0,[Read])}}
    TXS >> ....60: OUT: Act { { ( Out0, [ File(Value("K")) ] ) } }
    TXS >> ....61: IN: Act { { ( In2, [ Write(Value("ABL")) ] ) } }
    TXS >> ....62: OUT: Act { { ( Out2, [ File(Value("K")) ] ) } }
    TXS >> ....63: IN: Act{{(In2,[Read])}}
    TXS >> ....64: OUT: Act { { ( Out2, [ File(Value("ABL")) ] ) } }
    TXS >> ....65: IN: Act { { ( In2, [ Write(Value("P")) ] ) } }
    TXS >> ....66: OUT: Act { { ( Out2, [ File(Value("ABL")) ] ) } }
    TXS >> ....67: IN: Act{{(In0,[Read])}}
    TXS >> ....68: OUT: Act { { ( Out0, [ File(Value("P"))
    TXS >> ....69: IN: Act{{(In2,[Read])}}
    TXS >> ....70: OUT: Act { { ( Out2, [ File(Value("P"))
    TXS >> ....71: IN: Act{{(In1,[Read])}}
    TXS >> ....72: OUT: Act { { ( Out1, [ File(Value("P"))
    TXS >> ....73: IN: Act{{(In0,[Read])}}
    TXS >> ....74: OUT: Act { { ( Out0, [ File(Value("P"))
    TXS >> ....75: IN: Act{{(In0,[Stabilize])}}
    TXS >> ....76: OUT: Act { { ( Out0, [ File(Value("P"))
    TXS >> ....77: OUT: Act { { ( Out0, [ File(Value("X"))
    TXS >> ....78: OUT: Act { { ( Out0, [ File(Value("BH")) ] ) } }
    TXS >> ....79: OUT: Act { { ( Out0, [ File(Value("SP")) ] ) } }
    TXS >> ....80: OUT:Act{{(Out0,[Ack])}}
    TXS >> ....81: IN: Act { { ( In1, [ Write(Value("AB")) ] ) } }
    TXS >> ....82: OUT: Act { { ( Out1, [ File(Value("P")) ] ) } }
    TXS >> ....83: IN: Act { { ( In1, [ Write(Value("X")) ] ) } }
    TXS >> ....84: OUT: Act { { ( Out1, [ File(Value("AB")) ] ) } }
    TXS >> ....85: IN: Act{{(In0,[Read])}}
    TXS >> ....86: OUT: Act { { ( Out0, [ File(Value("P")) ] ) } }
    TXS >> ....87: IN: Act { { ( In2, [ Write(Value("PNB")) ] ) } }
    TXS >> ....88: OUT: Act { { ( Out2, [ File(Value("P")) ] ) } }
    TXS >> ....89: IN: Act { { ( In1, [ Write(Value("D")) ] ) } }
    TXS >> ....90: OUT: Act { { ( Out1, [ File(Value("X")) ] ) } }
    TXS >> ....91: IN: Act { { ( In1, [ Write(Value("L")) ] ) } }
    TXS >> ....92: OUT: Act { { ( Out1, [ File(Value("D")) ] ) } }
    TXS >> ....93: IN: Act{{(In2,[Read])}}
    TXS >> ....94: OUT: Act { { ( Out2, [ File(Value("PNB")) ] ) } }
    TXS >> ....95: IN: Act { { ( In1, [ Write(Value("KK")) ] ) } }
    TXS >> ....96: OUT: Act { { ( Out1, [ File(Value("PNB")) ] ) } }
    TXS >> ....97: IN: Act { { ( In2, [ Write(Value("P")) ] ) } }
    TXS >> ....98: OUT: Act { { ( Out2, [ File(Value("PNB")) ] ) } }
    TXS >> ....99: IN: Act{{(In0,[Read])}}
    TXS >> ...100: OUT: Act { { ( Out0, [ File(Value("KK")) ] ) } }
    TXS >> PASS
    TXS >>




Discussion and Comparison
-----------------------------------

We showed that model-based testing of a file synchronizer that is
distributed, concurrent, and nondeterministic, that combines state and
data, and that has internal state transitions that cannot be observed by
the tester, is possible with ``TorXakis`` , just as with Quviq
QuickCheck. The model used for ``TorXakis`` is a direct translation of
the QuickCheck model.

As opposed to the work with Quviq QuickCheck, we did not yet try to
reproduce the detected ’surprises’, i.e., probably erroneous behaviours
of Dropbox. More testing and analysis is needed, probably with steering
the test generation into specific corners of behaviour. Moreover, some
of these ’surprises’ require explicit deletion of files, which we
currently do not do. For steering, ``TorXakis`` has a feature
called *test purposes* , and future work will include using test
purposes to reproduce particular behaviours. But it might be that these
Dropbox ’surprises’ have been repaired in the mean time, as was
announced in [R40]_.

A difference between the Quviq QuickCheck approach and ``TorXakis`` is
the treatment of hidden actions. Whereas Quviq QuickCheck needs explicit
reasoning about possible ’explanations’ on top of the state machine
model using a specifically developed technique, the process-algebraic
language of ``TorXakis`` has ``HIDE`` as an abstraction operator
built into the language, which allows to turn any action into an
internal action. Together with the ioco-conformance relation, which
takes such internal actions into consideration, it makes the
construction of ’explanations’ completely automatic and an integral part
of test generation and observation analysis. Although no real speed
comparisons were made, it looks like the general solution of dealing
with hidden actions and nondeterminism in ``TorXakis`` has a price to
be paid in terms of computation speed.

``TorXakis`` has its own modelling language based on process algebra
and algebraic data types and with symbolic transition system semantics.
This allows to precisely define what a conforming ``sut`` is using the
ioco-conformance relation, in a formal testing framework which enables
to define soundness and exhaustiveness of generated test cases. Quviq
QuickCheck is embedded in the Erlang programming language, that is,
specifications are just Erlang programs that call libraries supplied by
QuickCheck and the generated tests invoke the ``sut`` directly via
Erlang function calls. A formal notion of ’conformance’ of
a ``sut`` is missing.

A powerful feature of Quviq QuickCheck for analysis and diagnosis is
shrinking. It automatically reduces the length of a test after failure
detection, which eases analysis. Currently, ``TorXakis`` has no such
feature.

Several extensions of the presented work are possible. One of them is
applying the same model to test other file synchronizers. Another is
adding additional Dropbox behaviour to the model, such as working with
multiple, named files and folders. This would complicate the model, but
not necessarily fundamentally change the model: instead of keeping a
single file value we would have to keep a (nested) map of file names to
file values, and read and write would be parameterized with file or
folder names.

Another, more fundamental question concerns the quality of the generated
test cases. How good are the test suites in detecting bugs, what is
their coverage, and to what extent can we be confident that
an ``sut`` that passes the tests is indeed correct? Can we compare
different (model-based) test generation strategies, e.g., the one of
Quviq QuickCheck with the one of ``TorXakis`` , and assign a measure
of quality or coverage to the generated test suites, and thus,
indirectly, a measure to the quality of the tested ``sut`` ?

