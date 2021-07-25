Connection Definitions
=======================================================

Syntax
-----------------------

=========== ===============================================================================================================================================================================================================================================================================
cnectDefs   "CNECTDEF" cnectDef (";" cnectDef )\* "ENDDEF"
cnectDef    cnectName "::=" cnectType cnectItem\*
cnectType   "CLIENTSOCK" \| "SERVERSOCK"
cnectItem     "CHAN" "OUT" channelName "HOST" hostName "PORT" portNumber \| "CHAN" "IN" channelName "HOST" hostName "PORT" portNumber \| "ENCODE" channelName "?" :ref:`varDecl` "->" "!" :ref:`valExpr` \| "DECODE" channelName "!" :ref:`valExpr` "<-" "?" :ref:`varDecl`
cnectName   :ref:`CapsId`
channelName :ref:`CapsId`
hostName    :ref:`String`
portNumber  :ref:`Int`
=========== ===============================================================================================================================================================================================================================================================================

Semantics
-----------------------------

Define connections with outside world, and the mapping from abstract
TorXakis channels to the concrete outside-world connections. Currently,
only socket connections (of type String) are supported. A socket has a
hostname, such as "localhost", and a portNumber.

Examples
---------------------------

The statement

::

   CNECTDEF  Sut
       ::=
           CLIENTSOCK

           CHAN  OUT  Action                         HOST "localhost"  PORT 7890
           ENCODE     Action  ? opn              ->  ! toString(opn)

           CHAN  IN   Result ::                      HOST "localhost"  PORT 7890
           DECODE     Result  ! fromString(s)   <-   ? s

   ENDDEF

specifies a socket connection, called ``Sut``, to the outside world
where

-  *TorXakis* is the client side;
-  there is one outgoing and one incoming channel, ``Action`` and
   ``Result``, respectively;
-  the types of messages communicated on channels ``Action`` and
   ``Result`` can be found in the corresponding channel definition
   CHANDEF;
-  the predefined function ``toString`` is used to map a message of
   channel ``Action`` to a string for the socket (localhost,7890);
-  the predefined function ``fromString`` is used to map a string from
   socket (localhost,7890) to a message on channel ``Result``;
-  both channels the outside world are accessed via one socket on the
   same machine, i.e., localhost on portNumber 7890; one channel is
   ``IN`` and one is ``OUT``.
   Note that
-  ``OUT`` and ``IN`` are viewed from the point of view of *TorXakis*,
   i.e., if this CNECTDEF specifies the connection to the system under
   test (SUT) then ``OUT`` is the input for the SUT, and ``IN`` is the
   output of the SUT;
-  each channel must map uniquely (bijectively) to a triple
   (``IN``/``OUT``,hostName,portNumber).

The statement

::

   CNECTDEF  Sim
       ::=
           SERVERSOCK

           CHAN  IN   Action :: Operation            HOST "localhost"  PORT 7890
           DECODE     Action  ! fromString(s)   <-   ? s

           CHAN  OUT  Result :: Int                  HOST "localhost"  PORT 7890
           ENCODE     Result  ? result           ->  ! toString(result)

   ENDDEF

specifies a socket connection, called ``Sim``, to the outside world,
where

-  *TorXakis* is the server side;
-  there is one incoming and one outgoing channel, ``Action`` and
   ``Result``, respectively;
-  the channel mappings are the inverse of the previous connection
   definition, implying that this connection can be used for a simulator
   simulating the same model as used above for testing.

Technical Details
-----------------

-  Socket streams must have UTF-8 string encoding, without byte order
   mark.
-  The new line format must be Linux (\n). When using the Windows style
   (\r\n) the \\r is considered part of the output string.
