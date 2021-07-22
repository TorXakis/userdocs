Process Call
===================================

Syntax
-----------------------

================= ==========================================================
procCall          procName "[" neChannelNameList? "]" "(" neValExprList? ")"
neChannelNameList channelName ("," channelName)\*
neValExprList     :ref:`valExpr` ("," [valExpr](ValExpr))\*
procName          :ref:`SmallId`
channelName       :ref:`CapsId`
================= ==========================================================

Semantics
-----------------------------

| Call a user defined process, defined with `PROCDEF <ProcDefs>`__.
| Channel name must refer to a predefined channel name.
