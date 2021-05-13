Sequence Operator\ `¶ <#Sequence-Operator>`__
=============================================

Syntax\ `¶ <#Syntax>`__
-----------------------

`communications <Communications>`__ “>->”
`processBehaviour <ProcessBehaviour>`__

Semantics\ `¶ <#Semantics>`__
-----------------------------

After the communications have occurred (in a single step), the described
process behaviour is exposed.

Examples\ `¶ <#Examples>`__
---------------------------

The statement

.. raw:: html

   <pre>Channel1_Int ? x >-> Channel2_Int ! x
   </pre>

describes the process that

-  first communicates over ``Channel1_Int`` (the value can be referred
   to as variable ``x``)
-  and next communicates the value of variable ``x`` on ``Channel2_Int``

The statement

.. raw:: html

   <pre>Channel1_Int ? x | Channel2_Int ? y >-> P[Channel3_Int](x,y)
   </pre>

describes the process that

-  first simultaneously communicates over ``Channel1_Int`` and
   ``Channel2_Int`` (the values can be referred to as variable ``x``
   over variable ``y``, respectively)
-  and next instantiates the process ``P`` with ``Channel3_Int`` as
   channel and the value of the variables ``x`` and ``y`` as arguments.
