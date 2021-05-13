Communications\ `¶ <#Communications>`__
=======================================

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

communications

.. raw:: html

   </td>

.. raw:: html

   <td>

communication (“`\| <Synchronous_Operator>`__” communication)\*
(`condition <Condition>`__)?

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

communication

.. raw:: html

   </td>

.. raw:: html

   <td>

channelName (“!” `valExpr <ValExpr>`__ \| “?” `varDecl <VarDecl>`__ )\*

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

| Specify communication.
| The direction of communication is NOT specified.

| Zero or more data can be communicated.
| The list of data types of the provided data must match
| the list of data types as specified in the channel definition.

| The operator ! denotes that the data item is fully specified: a known
  value is communicated.
| The operator ? denotes that the data item is underspecified: (part of)
  the value that is communicated is unknown.

| The predefined channel `EXIT <EXIT>`__ must be used to communicate
  process termination.
| Communication over the predefined channel `EXIT <EXIT>`__ might
  include exit values.

Examples\ `¶ <#Examples>`__
---------------------------

Communication without data\ `¶ <#Communication-without-data>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel be a channel over which can be communicated without any
  data.
| The statement

.. raw:: html

   <pre>Channel
   </pre>

specifies that the process wants to communicate.

| Besides channels that communicate without any data,
| this construct can also be used to obtain simpler models by
  abstracting away the actual data that is communicated.

Communication of fully specified data\ `¶ <#Communication-of-fully-specified-data>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

.. raw:: html

   <pre>Channel_Int ! 3
   </pre>

| specifies that the process wants to communicate the integer value 3.
| **Note** The same statement can be used to both send and receive the
  Integer value 3.

The statement

.. raw:: html

   <pre>Channel_Int ! id
   </pre>

| specifies that the process wants to communicate the integer value of
  variable id .
| **Note** No new variable is introduced for id.

Communication of underspecified data\ `¶ <#Communication-of-underspecified-data>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

.. raw:: html

   <pre>Channel_Int ? x
   </pre>

| specifies that the process wants to communicate an integer value.
| After communication, the value will be stored in the newly introduced
  variable x.
| **Note** The same statement can be used to both send and receive the
  underspecified variable x.

The actual communication might be

.. raw:: html

   <pre>Channel_Int ! 3
   </pre>

.. raw:: html

   <pre>Channel_Int ! -3
   </pre>

or

.. raw:: html

   <pre>Channel_Int ! -12345678901234567890
   </pre>

Communication of constrained data\ `¶ <#Communication-of-constrained-data>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

.. raw:: html

   <pre>Channel ? x [[ x >= 0 ]]
   </pre>

| specifies that the process wants to communicate a constrained integer
  value.
| The integer value is constrained to be larger than or equal to zero.
| The value is stored in the newly introduced variable x.

The actual communication might be

.. raw:: html

   <pre>Channel ! 3
   </pre>

but NOT a negative value like

.. raw:: html

   <pre>Channel ! -3
   </pre>

Communication of multiple data items\ `¶ <#Communication-of-multiple-data-items>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int_List be a channel over which one integer and one list
  at a time can be communicated.
| The statement

.. raw:: html

   <pre>Channel_Int_List ! id ? list [[ isCstr_Int(list) ]]
   </pre>

specifies that the process wants to communicate the following two data:
the value of the variable id and a non-empty list.
