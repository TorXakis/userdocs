Proccess Definitions
===================================================

Syntax
-----------------------

================== ===============================================================================================================
procDefs           "PROCDEF" procDef (";" procDef )\* "ENDDEF"
procDef            procName "[" neChannelDeclList? "]" "(" neVarDeclList? ")" exitDecl? "::=" :ref:`processBehaviour`
neChannelsDeclList channelsDecl (";" channelsDecl)\*
channelsDecl       neChannelNameList ("::" neTypeNameList)?
neChannelNameList  channelName ("," channelName)\*
neVarDeclList      varsDecl (";" varsDecl)\*
varsDecl           neVarNameList "::" typeName
neVarNameList      varName ("," varName)\*
exitDecl           "EXIT" neTypeNameList?
neTypeNameList     typeName ("#" typeName)\*
procName           :ref:`SmallId`
channelName        :ref:`CapsId`
typeName           :ref:`CapsId`
varName            :ref:`SmallId`
================== ===============================================================================================================

Semantics
-----------------------------

Define processes.

Examples
---------------------------

The statement

::

   PROCDEF myProcess [ Chan :: Int # Int ] ( n :: Int ) ::=
       Chan ! n ? x >-> myProcess [ Chan ] ( n+1 )
   ENDDEF

| defines the recursive process, myProcess.
| This process communicates a tuple of two integers on the channel Chan.
| The first integer of the tuple is incremented with each communication.
| The second integer of the tuple is unconstrained.
