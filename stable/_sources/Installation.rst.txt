Installation
------------

Windows
~~~~~~~

For Windows systems an installer is provided in the [releases][13]
section.

Linux
~~~~~

We provide a ``deb`` package from Debian based systems (Debian, Ubuntu,
etc), and an ``rpm`` package for distros using the RPM package manager.
Below we give instructions on how to install ``TorXakis`` on Ubuntu.

Download the latest ``deb`` release of ``TorXakis``
(``torxakis_0.6.0_amd64.deb`` in the example below) and then run the
following commands:

.. code:: sh

   apt-get update
   apt-get install ./torxakis_0.6.0_amd64.deb -y

The ``deb`` package was tested on Ubuntu version ``16.04``, ``17.10``,
and ``18.04``.

For installing ``TorXakis`` in RPM based distros please check your Linux
distro manual.

macOS
~~~~~

For macOS systems we provide a homebrew package. To install ``TorXakis``
run:

.. code:: sh

   brew tap torxakis/torxakis
   brew install torxakis

For more detailed instructions see the `Homebrew tap for TorXakis`_.

.. _Homebrew tap for TorXakis: https://github.com/TorXakis/homebrew-TorXakis
