Type Definitions
===========================================

In TorXakis, the user can define data types using the TYPEDEF keyword.

TorXakis will generate equality, type checking, and accessors
`functions <Function>`__ for the user defined data types.

Syntax
-----------------------

================= ==========================================
typeDefs          "TYPEDEF" typeDef (";" typeDef)\* "ENDDEF"
typeDef           typeName "::=" neConstructorList
neConstructorList constructor ("|" constructor)\*
constructor       constructorName ("{" neFieldsList "}")?
neFieldsList      fields (";" fields)\*
fields            neFieldNameList "::" typeName
neFieldNameList   fieldName ("," fieldName )\*
typeName          :ref:`CapsId`
constructorName   :ref:`CapsId`
fieldname         :ref:`SmallId`
================= ==========================================

Semantics
-----------------------------

| Define data types.
| A data type has a unique typeName.

| A data type must contain one or more constructors.
| A data type cannot contain constructors with the same constructorName.

| A constructor can contain zero or more fields.
| A data type cannot contain fields with the same fieldname.
| Hence, a constructor cannot contain fields with the same fieldname,
| and multiple constructors cannot contain a field with the same
  fieldname.

| The typeName associated with fields refers to a `data
  type <Data_Type>`__: either a `predefined data type <Data_Type>`__ or
  a `user defined data type <TypeDefs>`__.
| A data type is called recursive when one or more fields refer to
  itself.

Examples
---------------------------

The statement

::

   TYPEDEF Point ::= CPoint { x, y :: Int } ENDDEF

defines the data type Point as the Cartesian product of two integers.
These integers are referred to as x and y.

The statement

::

   TYPEDEF Conditional_Int ::=
             CAbsent_Int
           | CPresent_Int { value :: Int }
   ENDDEF

defines the data type Conditional_Int as the union of the absence of a
value and the presence of any integer value.

The statement

::

   TYPEDEF List_Int ::=
            CNil_Int    
         |  Cstr_Int { head :: Int; tail :: List_Int } ENDDEF

defines the recursive data type List_Int as the union of the empty list
and the list constructor: The Cartesian product of an integer referred
to as head, and a List_Int referred to as tail.
