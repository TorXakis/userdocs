Channel Definition\ `¶ <#Channel-Definition>`__
===============================================

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

chanDefs

.. raw:: html

   </td>

.. raw:: html

   <td>

“CHANDEF” chanDefName “::=” neChannelsDeclList “ENDDEF”

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

chanDefName

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

Define all channels that are used on the highest level in the
TorXakis-file, i.e., in model definitions (`MODELDEF <ModelDefs>`__) and
in connection definitions (`CNECTDEF <CnectDefs>`__). For each channel
the types of messages communicated via that channel are defined. At the
CHANDEF level, channels do not have an I/O-direction yet; I/O is added
on the level of `MODELDEF <ModelDefs>`__ and `CNECTDEF <CnectDefs>`__.

Examples\ `¶ <#Examples>`__
---------------------------

The definition

.. raw:: html

   <pre>CHANDEF Channels
       ::=
           Action :: Operation;
           Input  :: Int # Int;
           Result :: Int
   ENDDEF
   </pre>

defines three channels: ``Action``, ``Input``, and ``Result``, with
messages of types ``Operation``, (``Int`` x ``Int``), and ``Int``,
respectively.
