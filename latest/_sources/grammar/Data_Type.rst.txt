Data Type\ `¶ <#Data-Type>`__
=============================

TorXakis has predefined and user defined data types.

Predefined Data Types\ `¶ <#Predefined-Data-Types>`__
-----------------------------------------------------

TorXakis has the following four predefined data types.

.. raw:: html

   <table>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <th>

data type name

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

Bool

.. raw:: html

   </td>

.. raw:: html

   <td>

Boolean value: True and False

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Int

.. raw:: html

   </td>

.. raw:: html

   <td>

Unbounded Integer values

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

String

.. raw:: html

   </td>

.. raw:: html

   <td>

“Sequence of ASCII characters”

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

Regex

.. raw:: html

   </td>

.. raw:: html

   <td>

`‘W3C XSD Regular Expression
String’ <http://www.w3.org/TR/xmlschema11-2/#regexs>`__
Note: The regular expressions are also translate to
`POSIX <https://en.wikibooks.org/wiki/Regular_Expressions/POSIX-Extended_Regular_Expressions>`__
Some limitations of POSIX are not solved.
Consequence: regular expression like (a{0}) and [a-]] will fail. Of
course, they can be rewritten to a POSIX valid regular expression.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

User Defined Data Types\ `¶ <#User-Defined-Data-Types>`__
---------------------------------------------------------

| In TorXakis, one can defined datatypes, including unions, Cartesian
  Products, and recursive types, using
| `TYPEDEF <TypeDefs>`__.
