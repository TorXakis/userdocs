Model Definitions
=============================================

Syntax
-----------------------

================= ===================================================================================================================================================
modelDef          "MODELDEF" modelName "::=" "CHAN" "IN" neChannelNameList? "CHAN" "OUT" neChannelNameList? "BEHAVIOUR" :ref:`processBehaviour` "ENDDEF"
neChannelNameList channelName ("," channelName)\*
modelName         :ref:`CapsId`
channelName       :ref:`CapsId`
================= ===================================================================================================================================================

Semantics
-----------------------------

Define a model, with its input and output channels for external
communication, and the definition of its behaviour. Input and output
channels shall be defined in a channel definition
`CHANDEF <ChanDefs>`__.

Examples
---------------------------

The following model synchronizes using the `Synchronized Operator
\|\| <Synchronized_Operator>`__ a specification with a sequence.

::

   MODELDEF  Model ::=
         CHAN IN    A, B
         CHAN OUT   C, D 
         BEHAVIOUR 
            specification:ref:`A,B,C,D` || sequence:ref:`A,B,C,D`
   ENDDEF
