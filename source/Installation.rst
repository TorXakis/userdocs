Installation
------------

Windows
~~~~~~~

For Windows systems an installer is provided in the TorXakis github project's `releases page`_.

Linux
~~~~~

For all distributions and (recent) releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We provide  `TorXakis` packaged as an AppImage which is a portable package format which works on al 
linux distributions and releases. Every AppImage contains an app and all the files the app needs to run. 
In other words, each AppImage has no dependencies other than what is included in the targeted base operating system(s). 
The  `TorXakis` Appimage also contains `cvc4` and `z3`.

To run the AppImage, simply download it from the github's release page, make it executable 
and then just run it:

.. code:: sh

    $ wget https://github.com/TorXakis/TorXakis/releases/download/v0.9.0/TorXakis-0.9.0.x86_64.AppImage
    $ chmod a+x TorXakis-0.9.0.x86_64.AppImage
    $ ./TorXakis-0.9.0.x86_64.AppImage


Note: Most Docker installations do not permit the use FUSE inside containers for security reasons. Instead, you can extract and run an AppImage without using FUSE by setting the following environment variable: 

.. code:: sh

   export APPIMAGE_EXTRACT_AND_RUN=1


For debian based systems
^^^^^^^^^^^^^^^^^^^^^^^^

We provide a ``deb`` package for Debian based systems (Debian, Ubuntu, etc).
Below we give instructions on how to install ``TorXakis`` on Ubuntu 18.04.

Download the latest deb package for TorXakis from the TorXakis github
project's `releases page`_ and then run the following commands:

.. code:: sh

   apt-get update
   apt-get install ./torxakis_0.9.0-ubuntu_18.04-amd64.deb -y

The ``deb`` package was tested on Ubuntu version ``16.04``, ``17.10``, ``18.04`,
and ``20.04``.


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
