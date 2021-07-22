Communications
=======================================

Syntax
-----------------------

============== =====================================================================================
communications communication (":ref:`|`" communication)\* ([condition](Condition))?
communication  channelName ("!" :ref:`valExpr` \| "?" [varDecl](VarDecl) )\*
channelName    :ref:`CapsId`
============== =====================================================================================

Semantics
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

Examples
---------------------------

Communication without data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel be a channel over which can be communicated without any
  data.
| The statement

::

   Channel

specifies that the process wants to communicate.

| Besides channels that communicate without any data,
| this construct can also be used to obtain simpler models by
  abstracting away the actual data that is communicated.

Communication of fully specified data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

::

   Channel_Int ! 3

| specifies that the process wants to communicate the integer value 3.
| **Note** The same statement can be used to both send and receive the
  Integer value 3.

The statement

::

   Channel_Int ! id

| specifies that the process wants to communicate the integer value of
  variable id .
| **Note** No new variable is introduced for id.

Communication of underspecified data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

::

   Channel_Int ? x

| specifies that the process wants to communicate an integer value.
| After communication, the value will be stored in the newly introduced
  variable x.
| **Note** The same statement can be used to both send and receive the
  underspecified variable x.

The actual communication might be

::

   Channel_Int ! 3

::

   Channel_Int ! -3

or

::

   Channel_Int ! -12345678901234567890

Communication of constrained data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int be a channel over which one integer at a time can be
  communicated.
| The statement

::

   Channel ? x [[ x >= 0 ]]

| specifies that the process wants to communicate a constrained integer
  value.
| The integer value is constrained to be larger than or equal to zero.
| The value is stored in the newly introduced variable x.

The actual communication might be

::

   Channel ! 3

but NOT a negative value like

::

   Channel ! -3

Communication of multiple data items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Let Channel_Int_List be a channel over which one integer and one list
  at a time can be communicated.
| The statement

::

   Channel_Int_List ! id ? list [[ isCstr_Int(list) ]]

specifies that the process wants to communicate the following two data:
the value of the variable id and a non-empty list.
