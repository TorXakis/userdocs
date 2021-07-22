Function
===========================

TorXakis has predefined, implicitly defined `TYPEDEF <TypeDefs>`__, and
user defined functions.

Predefined Functions
---------------------------------------------------

TorXakis has the following predefined functions; grouped by predefined
data type to enhance readability.

Bool
~~~~~~~~~~~~~~~~~~~

================================ =========================
function                         description
================================ =========================
==(a,b :: Bool) ::= Bool         Equals Infix operator
<>(a,b :: Bool) ::= Bool         Not Equals Infix operator
toString(a :: Bool) ::= String   Bool to String function
fromString(s :: String) ::= Bool Bool from String function
not(b :: Bool) :: Bool           not function
/\(a,b :: Bool) :: Bool          and Infix Operator
\\/(a,b :: Bool) :: Bool         or Infix Operator
\\|/(a,b :: Bool) :: Bool        xor Infix Operator
=>(a,b :: Bool) :: Bool          implies Infix Operator
================================ =========================

Int
~~~~~~~~~~~~~~~~~

=============================== ==================================================================
function                        description
=============================== ==================================================================
==(a,b :: Int) ::= Bool         Equals Infix operator
<>(a,b :: Int) ::= Bool         Not Equals Infix operator
toString(a :: Int) ::= String   Int to String function
fromString(s :: String) ::= Int Int from String function
+(i :: Int) :: Int              Prefix Operator +
-(i :: Int) :: Int              Prefix Operator -
abs(i :: Int) :: Int            Absolute value function
+(a,b :: Int) ::= Int           Addition Infix operator
-(a,b :: Int) ::= Int           Substraction Infix operator
\*(a,b :: Int) ::= Int          Multiplication Infix operator
/(a,b :: Int) ::= Int           Division Infix operator according to Boute's Euclidean definition.
%(a,b :: Int) ::= Int           Modulo Infix operator according to Boute's Euclidean definition.
<(a,b :: Int) ::= Bool          Less Then Infix operator
<=(a,b :: Int) ::= Bool         Less Equal Infix operator
>=(a,b :: Int) ::= Bool         Greater Equal Infix operator
>(a,b :: Int) ::= Bool          Greater Then Infix operator
=============================== ==================================================================

Boute's Euclidean Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The definitions of div ``/`` and mod ``%`` are according to Boute's
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

String
~~~~~~~~~~~~~~~~~~~~~~~

=================================== ====================================================================================================================================================================
function                            description
=================================== ====================================================================================================================================================================
==(a,b :: String) ::= Bool          Equals Infix operator
<>(a,b :: String) ::= Bool          Not Equals Infix operator
++(a,b :: String) ::= String        Concat Infix operator
len(s ::String) :: Int              Length of String function
at(s :: String; i :: Int) :: String Character at position i of s. The index of position starts at 0. When the index is out of range (either i < 0 or i > len(s)) the empty string ("") will be returned.
=================================== ====================================================================================================================================================================

Regex
~~~~~~~~~~~~~~~~~~~~~

========================================= ========================
function                                  description
========================================= ========================
strinre(s :: String; r :: Regex) :: Bool Adheres string to regex?
========================================= ========================

Implicitly Defined `TYPEDEF <TypeDefs>`__ Functions
--------------------------------------------------------------------------------------------------

| TorXakis will automatically generate equality, type checking, and
  accessors functions for the user defined data types.
| **Note** accessor functions associated with a particular constructor
  are only defined for instances of that constructor.

Example
~~~~~~~~~~~~~~~~~~~~~~~~~

When the user defines

::

   TYPEDEF List_Int ::=
         CNil_Int
       | Cstr_Int { head :: Int; tail :: List_Int }
   ENDDEF

TorXakis defines the equality operator

::

   ==(a,b :: List_Int) :: Bool

the type checking functions (according to the pattern is)

::

   isCNil_Int(x :: List_Int) :: Bool
   isCstr_Int(x :: List_Int) :: Bool 

and the accessor functions

::

   head(x :: List_Int) :: Int
   tail(x :: List_Int) :: List_Int

which satisfy

::

   head(Cstr_Int(h,t)) == h
   tail(Cstr_Int(h,t)) == t

| Note that these accessor functions are only defined for instances of
  the Cstr_Int constructor, i.e.,
| instances of List_Int for which isCstr_Int(x) returns True.
  head(CNil_Int) and tail(CNil_Int) are thus not defined.

One should guard the usage of accessor functions with the constructor
check, using `IF THEN ELSE FI <IteValExpr>`__ .

::

   IF isCstr_Int(x) THEN head(x) == 5 ELSE False FI

User Defined Functions
-------------------------------------------------------

| In TorXakis, the user can define functions, including recursive
  functions, using
| `FUNCDEF <FuncDefs>`__.
