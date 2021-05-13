Function\ `¶ <#Function>`__
===========================

TorXakis has predefined, implicitly defined `TYPEDEF <TypeDefs>`__, and
user defined functions.

Predefined Functions\ `¶ <#Predefined-Functions>`__
---------------------------------------------------

TorXakis has the following predefined functions; grouped by predefined
data type to enhance readability.

Bool\ `¶ <#Bool>`__
~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

function

.. raw:: html

   </th>

.. raw:: html

   <th>

description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

==(a,b :: Bool) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

<>(a,b :: Bool) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Not Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

toString(a :: Bool) ::= String

.. raw:: html

   </td>

.. raw:: html

   <td>

Bool to String function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

fromString(s :: String) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Bool from String function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

not(b :: Bool) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

not function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

/(a,b :: Bool) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

and Infix Operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

/(a,b :: Bool) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

or Infix Operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

\|/(a,b :: Bool) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

xor Infix Operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

=>(a,b :: Bool) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

implies Infix Operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Int\ `¶ <#Int>`__
~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

function

.. raw:: html

   </th>

.. raw:: html

   <th>

description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

==(a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

<>(a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Not Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

toString(a :: Int) ::= String

.. raw:: html

   </td>

.. raw:: html

   <td>

Int to String function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

fromString(s :: String) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Int from String function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

+(i :: Int) :: Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Prefix Operator +

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

-(i :: Int) :: Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Prefix Operator -

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

abs(i :: Int) :: Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Absolute value function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

+(a,b :: Int) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Addition Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

-(a,b :: Int) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Substraction Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

\*(a,b :: Int) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Multiplication Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

/(a,b :: Int) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Division Infix operator according to Boute’s Euclidean definition.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

%(a,b :: Int) ::= Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Modulo Infix operator according to Boute’s Euclidean definition.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

<(a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Less Then Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

<=(a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Less Equal Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

..

   =(a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Greater Equal Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

..

   (a,b :: Int) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Greater Then Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Boute’s Euclidean Definition\ `¶ <#boutes-euclidean-definition>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The definitions of div ``/`` and mod ``%`` are according to Boute’s
Euclidean definition [1], that is, so as to satisfy the formula

::

   (for all ((m Int) (n Int))
     (=> (distinct n 0)
         (let ((q (div m n)) (r (mod m n)))
           (and (= m (+ (* n q) r))
                (<= 0 r (- (abs n) 1))))))

[1] Boute, Raymond T. (April 1992). The Euclidean definition of the
functions div and mod. ACM Transactions on Programming Languages and
Systems (TOPLAS) ACM Press. 14 (2): 127 - 144.
doi:10.1145/128861.128862.

String\ `¶ <#String>`__
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

function

.. raw:: html

   </th>

.. raw:: html

   <th>

description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

==(a,b :: String) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

<>(a,b :: String) ::= Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Not Equals Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

++(a,b :: String) ::= String

.. raw:: html

   </td>

.. raw:: html

   <td>

Concat Infix operator

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

len(s ::String) :: Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Length of String function

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

at(s :: String; i :: Int) :: String

.. raw:: html

   </td>

.. raw:: html

   <td>

Character at position i of s.
The index of position starts at 0. When the index is out of range
(either i < 0 or i > len(s)) the empty string ("") will be returned.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Regex\ `¶ <#Regex>`__
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

function

.. raw:: html

   </th>

.. raw:: html

   <th>

description

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

strinre(s :: String; r :: Regex) :: Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Adheres string to regex?

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

Implicitly Defined `TYPEDEF <TypeDefs>`__ Functions\ `¶ <#Implicitly-Defined-TYPEDEF-Functions>`__
--------------------------------------------------------------------------------------------------

| TorXakis will automatically generate equality, type checking, and
  accessors functions for the user defined data types.
| **Note** accessor functions associated with a particular constructor
  are only defined for instances of that constructor.

Example\ `¶ <#Example>`__
~~~~~~~~~~~~~~~~~~~~~~~~~

When the user defines

.. raw:: html

   <pre>TYPEDEF List_Int ::=
         CNil_Int
       | Cstr_Int { head :: Int; tail :: List_Int }
   ENDDEF
   </pre>

TorXakis defines the equality operator

.. raw:: html

   <pre>==(a,b :: List_Int) :: Bool
   </pre>

the type checking functions (according to the pattern is)

.. raw:: html

   <pre>isCNil_Int(x :: List_Int) :: Bool
   isCstr_Int(x :: List_Int) :: Bool 
   </pre>

and the accessor functions

.. raw:: html

   <pre>head(x :: List_Int) :: Int
   tail(x :: List_Int) :: List_Int
   </pre>

which satisfy

.. raw:: html

   <pre>head(Cstr_Int(h,t)) == h
   tail(Cstr_Int(h,t)) == t
   </pre>

| Note that these accessor functions are only defined for instances of
  the Cstr_Int constructor, i.e.,
| instances of List_Int for which isCstr_Int(x) returns True.
  head(CNil_Int) and tail(CNil_Int) are thus not defined.

One should guard the usage of accessor functions with the constructor
check, using `IF THEN ELSE FI <IteValExpr>`__ .

.. raw:: html

   <pre>IF isCstr_Int(x) THEN head(x) == 5 ELSE False FI
   </pre>

User Defined Functions\ `¶ <#User-Defined-Functions>`__
-------------------------------------------------------

| In TorXakis, the user can define functions, including recursive
  functions, using
| `FUNCDEF <FuncDefs>`__.
