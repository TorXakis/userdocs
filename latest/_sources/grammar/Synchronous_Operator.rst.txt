Synchronous Operator\ `¶ <#Synchronous-Operator>`__
===================================================

Syntax\ `¶ <#Syntax>`__
-----------------------

`communications <Communications>`__ “\|”
`communications <Communications>`__

Semantics\ `¶ <#Semantics>`__
-----------------------------

communication1 \| communication2

| Both communication1 and communication2 are execute at the same time.
| These communications can only occur when both have a set of matching
  processes to communicate with.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>ChannelId1 ? x | ChannelId2 ? y
   </pre>

desribe the process that at the same time

-  communicates variable x over ChannelId1 and
-  communicates variable y over ChannelId2

For this, both communications must, of course, be possible.

The statement

.. raw:: html

   <pre>CreateAccount ? account | CreateUser ? id ? pw1 ? pw2 [[ (id(account) == id) /\ (pw(account) == pw1) /\ (pw(account) == pw2) ]]
   </pre>

| desribe the process that at the same time creates an account using a
  data type and by the triplet of id, password, and confirm password.
| Thus the synchronous operator is used to link the different levels of
  abstraction.
