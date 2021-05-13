Language Definition\ `¶ <#Language-Definition>`__
=================================================

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

specification

.. raw:: html

   </td>

.. raw:: html

   <td>

( `modelDefs <ModelDefs>`__
\| `cnectDefs <CnectDefs>`__
\| `chanDefs <ChanDefs>`__
\| `typeDefs <TypeDefs>`__
\| `constDefs <ConstDefs>`__
\| `funcDefs <FuncDefs>`__
\| `procDefs <ProcDefs>`__
\| `stautDef <StautDef>`__
) \*

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

| A specification contains zero or more definitions.
| A `Model Definition <ModelDefs>`__ is needed to step a TorXakis model.
| A `Model Definition <ModelDefs>`__ and `Connection
  Definition <CnectDefs>`__ are minimally needed to test a SUT or
  simulate a system using a TorXakis model.
