Channel Definition
===============================================

Syntax
-----------------------

================== =======================================================
chanDefs           "CHANDEF" chanDefName "::=" neChannelsDeclList "ENDDEF"
neChannelsDeclList channelsDecl (";" channelsDecl)\*
channelsDecl       neChannelNameList ("::" neTypeNameList)?
neChannelNameList  channelName ("," channelName)\*
neTypeNameList     typeName ("#" typeName)\*
chanDefName        :ref:`CapsId`
channelName        :ref:`CapsId`
typeName           :ref:`CapsId`
================== =======================================================

Semantics
-----------------------------

Define all channels that are used on the highest level in the
TorXakis-file, i.e., in model definitions (`MODELDEF <ModelDefs>`__) and
in connection definitions (`CNECTDEF <CnectDefs>`__). For each channel
the types of messages communicated via that channel are defined. At the
CHANDEF level, channels do not have an I/O-direction yet; I/O is added
on the level of `MODELDEF <ModelDefs>`__ and `CNECTDEF <CnectDefs>`__.

Examples
---------------------------

The definition

::

   CHANDEF Channels
       ::=
           Action :: Operation;
           Input  :: Int # Int;
           Result :: Int
   ENDDEF

defines three channels: ``Action``, ``Input``, and ``Result``, with
messages of types ``Operation``, (``Int`` x ``Int``), and ``Int``,
respectively.
