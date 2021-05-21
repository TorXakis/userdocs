HIDE
=====

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

hideProcessBehaviour

.. raw:: html

   </td>

.. raw:: html

   <td>

“HIDE” “[" neChannelsDeclList? "]” “IN”
`processBehaviour <ProcessBehaviour>`__ “NI”

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

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

| Hide a set of channels.
| Hence, the environment can not synchronize over these channels.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>HIDE [ Channel ] IN
       A >-> Channel >-> C
   |[ Channel ]|
       B >-> Channel >-> D
   NI
   </pre>

| synchronizes the two processes on an internal Channel.
| The externally observable communication behaviour is equal to

.. raw:: html

   <pre>(A ||| B) >>> (C ||| D)
   </pre>

or in words, communications on channels A and B occur before
communications on channels C and D.

The statement

.. raw:: html

   <pre>HIDE [ Channel :: Int ] IN
       A ? x  >-> Channel ! (x + 10)
   |[ Channel ]|
       Channel ? y >-> B ! (y + 20)
   NI
   </pre>

| synchronizes the two processes on an internal Channel of type Int.
| The externally observable communication behaviour is equal to

.. raw:: html

   <pre> A ? x >-> B ! (x + 30)
   </pre>

Implementation
--------------

TorXakis currently requires that hidden variables have a unique
solution. For example,

.. raw:: html

   <pre>HIDE [ A :: Int ] IN
       A ? x >-> B ! x
   NI 
   </pre>

is not allowed: You either get the warning message
``unfoldCTbranch: Not unique`` or
``after: cannot find unique value for hidden variables``, depending on
whether TorXakis can determine before or after executing the action that
the hidden variables will be / are unique.

This limitiation can often be circumvented, e.g. by

.. raw:: html

   <pre>HIDE [ A :: Int ] IN
       A ? x | B ? y [[ y == x ]]
   NI
   </pre>

TorXakis might drop this requirement in the future: See
https://github.com/TorXakis/TorXakis/issues/222 for more info.
