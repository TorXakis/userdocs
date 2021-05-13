TorXakis\ `¶ <#TorXakis>`__
===========================

TorXakis uses a `specification <Language_Definition>`__ to test a
System-Under-Test (SUT) or simulate a System.

A TorXakis `specification <Language_Definition>`__ contains three parts:

-  `Model <ModelDefs>`__ - Composition of processes instances that
   models the behavior of the SUT
-  `Adapter <AdapDefs.html>`__ - Map abstract specification on actual
   SUT interfaces.
-  `Connection <CnectDefs>`__ - Describe external interfaces to SUT or
   of simulated system.

| TorXakis uses the Input-Output Conformance (IOCO) theory to
| check the actual against the specified externally observable
  behaviour.

| TorXakis is a command line tool that takes zero or more
  `specification <Language_Definition>`__ files as input.
| TorXakis has many `commands <Commands>`__: the command ‘help’ provides
  a short summary of all `commands <Commands>`__.

A TorXakis Editor for the Eclipse IDE is provided as a plug-in. See
`Eclipse <Eclipse>`__.

| Copyright © 2015-2016 TNO and Radboud University
| All rights reserved.


