HIDE
===================

Syntax
-----------------------

==================== =================================================================================
hideProcessBehaviour "HIDE" "[" neChannelsDeclList? "]" "IN" :ref:`processBehaviour` "NI"
neChannelsDeclList   channelsDecl (";" channelsDecl)\*
channelsDecl         neChannelNameList ("::" neTypeNameList)?
neChannelNameList    channelName ("," channelName)\*
neTypeNameList       typeName ("#" typeName)\*
channelName          :ref:`CapsId`
typeName             :ref:`CapsId`
==================== =================================================================================

Semantics
-----------------------------

| Hide a set of channels.
| Hence, the environment can not synchronize over these channels.

Examples
---------------------------

The statement

::

   HIDE [ Channel ] IN
       A >-> Channel >-> C
   |[ Channel ]|
       B >-> Channel >-> D
   NI

| synchronizes the two processes on an internal Channel.
| The externally observable communication behaviour is equal to

::

   (A ||| B) >>> (C ||| D)

or in words, communications on channels A and B occur before
communications on channels C and D.

The statement

::

   HIDE [ Channel :: Int ] IN
       A ? x  >-> Channel ! (x + 10)
   |[ Channel ]|
       Channel ? y >-> B ! (y + 20)
   NI

| synchronizes the two processes on an internal Channel of type Int.
| The externally observable communication behaviour is equal to

::

    A ? x >-> B ! (x + 30)

Implementation
--------------

TorXakis currently requires that hidden variables have a unique
solution. For example,

::

   HIDE [ A :: Int ] IN
       A ? x >-> B ! x
   NI 

is not allowed: You either get the warning message
``unfoldCTbranch: Not unique`` or
``after: cannot find unique value for hidden variables``, depending on
whether TorXakis can determine before or after executing the action that
the hidden variables will be / are unique.

This limitiation can often be circumvented, e.g. by

::

   HIDE [ A :: Int ] IN
       A ? x | B ? y [[ y == x ]]
   NI

TorXakis might drop this requirement in the future: See
https://github.com/TorXakis/TorXakis/issues/222 for more info.
