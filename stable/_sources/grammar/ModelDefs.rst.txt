Model Definitions\ `¶ <#Model-Definitions>`__
=============================================

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

modelDef

.. raw:: html

   </td>

.. raw:: html

   <td>

“MODELDEF” modelName “::=” “CHAN” “IN” neChannelNameList? “CHAN” “OUT”
neChannelNameList? “BEHAVIOUR” `processBehaviour <ProcessBehaviour>`__
“ENDDEF”

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

modelName

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

   </tbody>

.. raw:: html

   </table>

Semantics\ `¶ <#Semantics>`__
-----------------------------

Define a model, with its input and output channels for external
communication, and the definition of its behaviour. Input and output
channels shall be defined in a channel definition
`CHANDEF <ChanDefs>`__.

Examples\ `¶ <#Examples>`__
---------------------------

The following model synchronizes using the `Synchronized Operator
\|\| <Synchronized_Operator>`__ a specification with a sequence.

.. raw:: html

   <pre>MODELDEF  Model ::=
         CHAN IN    A, B
         CHAN OUT   C, D 
         BEHAVIOUR 
            specification[A,B,C,D](Nil) || sequence[A,B,C,D]()
   ENDDEF
   </pre>
