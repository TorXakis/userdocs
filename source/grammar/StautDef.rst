State Automaton Definition
===============================================================

Syntax
-----------------------

================== ============================================================================================================
stautDef           "STAUTDEF" procName "[" neChannelDeclList? "]" "(" neVarDeclList? ")" exitDecl? "::=" stautItem+ "ENDDEF"
stautItem          ( "STATE" stateName \| "VAR" neVarDeclList? \| "INIT" stateName ("{" neUpdate "}")? \| "TRANS" transition+ )
transition         statename "->" :ref:`Communications` ("{" neUpdate "}")? "->" stateName
neUpdate           neUpdate ":=" update (";" update)\*
update             varName ":=" :ref:`valExpr`
neChannelsDeclList channelsDecl (";" channelsDecl)\*
channelsDecl       neChannelNameList ("::" neTypeNameList)?
neChannelNameList  channelName ("," channelName)\*
neVarDeclList      varsDecl (";" varsDecl)\*
varsDecl           neVarNameList "::" typeName
neVarNameList      varName ("," varName)\*
exitDecl           "EXIT" ("::" neTypeNameList)?
neTypeNameList     typeName ("#" typeName)\*
procName           :ref:`SmallId`
channelName        :ref:`CapsId`
typeName           :ref:`CapsId`
varName            :ref:`SmallId`
stateName          :ref:`SmallId`
================== ============================================================================================================

Semantics
-----------------------------

Define a state automaton.

A state automaton is a structure consisting of states, state variables,
and transitions. A transition specifies how to go from one state to
another state, while performing communications and updating the state
variables. INIT specifies the initial state and the initial values of
the state variables. The header of a state automaton definition is
analogous to the header of `Process Definition PROCDEF <ProcDefs>`__.

Examples
---------------------------

::

   STAUTDEF  check1000 [ Add :: Int;  Sum :: Int;  Success ]  ( start_value :: Int )
    ::=
         STATE  state0, state1
         VAR    sum :: Int
         INIT   state0 { sum := start_value }

         TRANS  state0  ->  Add ? x    [[ x >= 0      ]]  { sum := sum + x }      ->  state1
                state1  ->  Sum ! sum  [[ sum <= 1000 ]]  { }                     ->  state0
                state1  ->  Success    [[ sum >= 1000 ]]  { sum := start_value }  ->  state0
   ENDDEF

The state automaton ``check1000`` specifies a system with two state
``state0`` and ``state1``, one state variable ``sum``, and three
transitions. The system adds positive integer inputs until the sum is at
least 1000, upon which it outputs ``success``. Then it restarts the
process starting with ``sum := start_value``. Note the non-determinism
when the ``sum`` is exactly equal to 1000.

::

   STAUTDEF m [C :: Int] () EXIT ::=
       STATE   s0, s1, s2
       INIT    s0
       TRANS   s0 -> C ! 1 -> s1
               s1 -> EXIT -> s2
   ENDDEF

The state automaton ``m`` communicates ``1`` over channel ``C`` and then
``EXIT``\ s.
