Variable Declaration
===================================================

Syntax
-----------------------

======== ========================
varDecl  varName ("::" typeName)?
varName  :ref:`SmallId`
typeName :ref:`CapsId`
======== ========================

Semantics
-----------------------------

Declare a variable. The type can only be left out when the type can be
deducted from the context.

Examples
---------------------------

The statement

::

   s :: String

declares a variable named s of type String.
