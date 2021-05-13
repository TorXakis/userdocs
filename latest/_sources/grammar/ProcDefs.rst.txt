Proccess Definitions\ `¶ <#Proccess-Definitions>`__
===================================================

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

procDefs

.. raw:: html

   </td>

.. raw:: html

   <td>

“PROCDEF” procDef (“;” procDef )\* “ENDDEF”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

procDef

.. raw:: html

   </td>

.. raw:: html

   <td>

procName “[" neChannelDeclList? "]” “(” neVarDeclList? “)” exitDecl?
“::=” `processBehaviour <ProcessBehaviour>`__

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

“EXIT” neTypeNameList?

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

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

Define processes.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>PROCDEF myProcess [ Chan :: Int # Int ] ( n :: Int ) ::=
       Chan ! n ? x >-> myProcess [ Chan ] ( n+1 )
   ENDDEF
   </pre>

| defines the recursive process, myProcess.
| This process communicates a tuple of two integers on the channel Chan.
| The first integer of the tuple is incremented with each communication.
| The second integer of the tuple is unconstrained.
