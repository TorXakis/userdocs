Installation
------------

Windows
~~~~~~~

For Windows systems an installer is provided in the TorXakis github project's `releases page`_.

Linux
~~~~~



We provide a ``deb`` package for Debian based systems (Debian, Ubuntu, etc).
Below we give instructions on how to install ``TorXakis`` on Ubuntu 18.04.

Download the latest deb package for TorXakis from the TorXakis github
project's `releases page`_ and then run the following commands:

.. code:: sh

   apt-get update
   apt-get install ./torxakis_0.9.0-ubuntu_18.04-amd64.deb -y

The ``deb`` package was tested on Ubuntu version ``16.04``, ``17.10``,
and ``18.04``.


MacOS
~~~~~

For macOS systems we provide a homebrew package. To install ``TorXakis``
run:

.. code:: sh

   brew tap torxakis/torxakis
   brew install torxakis

For more detailed instructions see the `Homebrew tap for TorXakis`_.

.. _Homebrew tap for TorXakis: https://github.com/TorXakis/homebrew-TorXakis
.. _releases page: https://github.com/TorXakis/TorXakis/releases
