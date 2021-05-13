Type Definitions\ `¶ <#Type-Definitions>`__
===========================================

In TorXakis, the user can define data types using the TYPEDEF keyword.

TorXakis will generate equality, type checking, and accessors
`functions <Function>`__ for the user defined data types.

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

typeDefs

.. raw:: html

   </td>

.. raw:: html

   <td>

“TYPEDEF” typeDef (“;” typeDef)\* “ENDDEF”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

typeDef

.. raw:: html

   </td>

.. raw:: html

   <td>

typeName “::=” neConstructorList

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neConstructorList

.. raw:: html

   </td>

.. raw:: html

   <td>

constructor (“\|” constructor)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

constructor

.. raw:: html

   </td>

.. raw:: html

   <td>

constructorName (“{” neFieldsList “}”)?

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neFieldsList

.. raw:: html

   </td>

.. raw:: html

   <td>

fields (“;” fields)\*

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

fields

.. raw:: html

   </td>

.. raw:: html

   <td>

neFieldNameList “::” typeName

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

neFieldNameList

.. raw:: html

   </td>

.. raw:: html

   <td>

fieldName (“,” fieldName )\*

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

   <tr>

.. raw:: html

   <td>

constructorName

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

fieldname

.. raw:: html

   </td>

.. raw:: html

   <td>

`SmallId <SmallId>`__

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

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>TYPEDEF Point ::= CPoint { x, y :: Int } ENDDEF
   </pre>

defines the data type Point as the Cartesian product of two integers.
These integers are referred to as x and y.

The statement

.. raw:: html

   <pre>TYPEDEF Conditional_Int ::=
             CAbsent_Int
           | CPresent_Int { value :: Int }
   ENDDEF
   </pre>

defines the data type Conditional_Int as the union of the absence of a
value and the presence of any integer value.

The statement

.. raw:: html

   <pre>TYPEDEF List_Int ::=
            CNil_Int    
         |  Cstr_Int { head :: Int; tail :: List_Int } ENDDEF
   </pre>

defines the recursive data type List_Int as the union of the empty list
and the list constructor: The Cartesian product of an integer referred
to as head, and a List_Int referred to as tail.
