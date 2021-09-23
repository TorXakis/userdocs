Command Line Interface
======================

``TorXakis`` ships with a command line interface.

To see the available commands type ``help`` on the ``TorXakis`` prompt.
The output is shown in the :ref:`Torxakis help appendix<torxakis help>`.

For an example how to use the command line interface take a look at the next
chapter :ref:`Trace and replay functionality` or take a look at one of the examples
in the :ref:`exampleschapter` chapter.

Command history
---------------

Command history can be navigated with the up and down arrows, or using
``Ctrl-P`` and ``Ctrl-N``.

To reverse-search in the command history type ``Ctrl+R``.

The command history is kept in the user's home directory (whose location varies
depending on the operating system), in a file called:

.. code-block:: text

  .torxakis-hist.txt


Configuration file
------------------

TorXakis can be configured by using a configuration file
``.torxakis.yaml``. The configuration file is expected either

-  in the working directory or
-  in the home directory.

The working directory has precedence over the latter. An example of a
``.torxakis.yaml`` file can be found in the ``TorXakis`` github
repository at this
`page <https://github.com/TorXakis/TorXakis/blob/develop/.torxakis.yaml>`__.

Example
^^^^^^^

To configure ``TorXakis`` to use `CVC4 <http://cvc4.cs.stanford.edu/>`__
instead of `Z3 <https://github.com/Z3Prover/z3>`__ we use the
``~/.torxakis.yaml`` configuration file to change the default
`SMT <https://en.wikipedia.org/wiki/Satisfiability_modulo_theories>`__
solver being used, which we can create using the following commands:

.. code:: sh

   echo 'selected-solver: "cvc4" ' > ~/.torxakis.yaml


From now on ``TorXakis`` will use
`CVC4 <http://cvc4.cs.stanford.edu/>`__ instead of
`Z3 <https://github.com/Z3Prover/z3>`__.

Logs
----

``TorXakis`` stores also logs of the command line interface in the ``.torxakis/`` folder in the user’s home directory.
The file ``.torxakis/txs-cli-latest.log`` contains the log of the latest session with the
command line interface.