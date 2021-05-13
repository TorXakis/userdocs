State Automaton Definition\ `¶ <#State-Automaton-Definition>`__
===============================================================

Syntax\ `¶ <#Syntax>`__
-----------------------

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

stautDef

.. raw:: html

   </td>

.. raw:: html

   <td>

“STAUTDEF” procName “[" neChannelDeclList? "]” “(” neVarDeclList? “)”
exitDecl? “::=” stautItem+ “ENDDEF”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

stautItem

.. raw:: html

   </td>

.. raw:: html

   <td>

( “STATE” stateName
\| “VAR” neVarDeclList?
\| “INIT” stateName (“{” neUpdate “}”)? \| “TRANS” transition+
)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

transition

.. raw:: html

   </td>

.. raw:: html

   <td>

statename “->” `Communications <Communications>`__ (“{” neUpdate “}”)?
“->” stateName

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neUpdate

.. raw:: html

   </td>

.. raw:: html

   <td>

neUpdate “:=” update (“;” update)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

update

.. raw:: html

   </td>

.. raw:: html

   <td>

varName “:=” `valExpr <ValExpr>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neChannelsDeclList

.. raw:: html

   </td>

.. raw:: html

   <td>

channelsDecl (“;” channelsDecl)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

channelsDecl

.. raw:: html

   </td>

.. raw:: html

   <td>

neChannelNameList (“::” neTypeNameList)?

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neChannelNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

channelName (“,” channelName)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neVarDeclList

.. raw:: html

   </td>

.. raw:: html

   <td>

varsDecl (“;” varsDecl)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

varsDecl

.. raw:: html

   </td>

.. raw:: html

   <td>

neVarNameList “::” typeName

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neVarNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

varName (“,” varName)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

exitDecl

.. raw:: html

   </td>

.. raw:: html

   <td>

“EXIT” (“::” neTypeNameList)?

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neTypeNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

typeName (“#” typeName)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

procName

.. raw:: html

   </td>

.. raw:: html

   <td>

`SmallId <SmallId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

channelName

.. raw:: html

   </td>

.. raw:: html

   <td>

`CapsId <CapsId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

typeName

.. raw:: html

   </td>

.. raw:: html

   <td>

`CapsId <CapsId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

varName

.. raw:: html

   </td>

.. raw:: html

   <td>

`SmallId <SmallId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

stateName

.. raw:: html

   </td>

.. raw:: html

   <td>

`SmallId <SmallId>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

Define a state automaton.

A state automaton is a structure consisting of states, state variables,
and transitions. A transition specifies how to go from one state to
another state, while performing communications and updating the state
variables. INIT specifies the initial state and the initial values of
the state variables. The header of a state automaton definition is
analogous to the header of `Process Definition PROCDEF <ProcDefs>`__.

Examples\ `¶ <#Examples>`__
---------------------------

.. raw:: html

   <pre>STAUTDEF  check1000 [ Add :: Int;  Sum :: Int;  Success ]  ( start_value :: Int )
    ::=
         STATE  state0, state1
         VAR    sum :: Int
         INIT   state0 { sum := start_value }

         TRANS  state0  ->  Add ? x    [[ x >= 0      ]]  { sum := sum + x }      ->  state1
                state1  ->  Sum ! sum  [[ sum <= 1000 ]]  { }                     ->  state0
                state1  ->  Success    [[ sum >= 1000 ]]  { sum := start_value }  ->  state0
   ENDDEF
   </pre>

The state automaton ``check1000`` specifies a system with two state
``state0`` and ``state1``, one state variable ``sum``, and three
transitions. The system adds positive integer inputs until the sum is at
least 1000, upon which it outputs ``success``. Then it restarts the
process starting with ``sum := start_value``. Note the non-determinism
when the ``sum`` is exactly equal to 1000.

.. raw:: html

   <pre>
   STAUTDEF m [C :: Int] () EXIT ::=
       STATE   s0, s1, s2
       INIT    s0
       TRANS   s0 -> C ! 1 -> s1
               s1 -> EXIT -> s2
   ENDDEF
   </pre>

The state automaton ``m`` communicates ``1`` over channel ``C`` and then
``EXIT``\ s.
