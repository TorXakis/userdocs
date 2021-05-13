ProcessBehaviour\ `¶ <#ProcessBehaviour>`__
===========================================

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

processBehaviour

.. raw:: html

   </td>

.. raw:: html

   <td>

  processBehaviour “`>>> <Enable_Operator>`__” processBehaviour
\| processBehaviour “`>>> <Enable_Operator>`__” “ACCEPT” (“?”
`varDecl <VarDecl>`__ \| “!” `valExpr <ValExpr>`__ )\* IN
processBehaviour NI
\| processBehaviour “[`>> <Disable_Operator>`__” processBehaviour
\| processBehaviour “[`>< <Interrupt_Operator>`__” processBehaviour
\| processBehaviour “`\|\| <Synchronized_Operator>`__” processBehaviour
\| processBehaviour “`\||\| <Parallel_Operator>`__” processBehaviour
\|
`processBehavioursSynchronizedOnChannels <Synchronized_Channels_Operator>`__
\| processBehaviour “`## <Choice_Operator>`__” processBehaviour
\| `condition <Condition>`__ “`=>> <Guard_Operator>`__” processBehaviour
\| `communications <Communications>`__ (“`>-> <Sequence_Operator>`__”
processBehaviour)?
\| `STOP <STOP>`__
\| `procCall <ProcCall>`__
\| `letProcessBehaviour <LET>`__
\| `hideChannelsInProcessBehaviour <HIDE>`__
\| “(” processBehaviour “)”

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

Examples\ `¶ <#Examples>`__
---------------------------
