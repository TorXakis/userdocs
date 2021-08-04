Installation
------------

Windows
~~~~~~~

For Windows systems an installer is provided in the TorXakis github project's `releases page`_.

Linux
~~~~~

For all distributions and (recent) releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TorXakis's AppImage
+++++++++++++++++++

We provide  `TorXakis` packaged as an AppImage which is a portable package format which works on al 
linux distributions and releases. Every AppImage contains an app and all the files the app needs to run. 
In other words, each AppImage has no dependencies other than what is included in the targeted base operating system(s). 
The  `TorXakis` Appimage also contains `cvc4` and `z3`.

To run the AppImage, simply download it from the github's release page, make it executable 
and we then can just run it:

.. code:: sh

    $ wget https://github.com/TorXakis/TorXakis/releases/download/v0.9.0/torxakis-0.9.0.x86_64.AppImage
    $ chmod a+x torxakis-0.9.0.x86_64.AppImage
    $ ./torxakis-0.9.0.x86_64.AppImage

Note: most Docker installations do not permit the use FUSE inside containers for security reasons. Instead, you can extract and run an AppImage without using FUSE by setting the following environment variable: 

.. code:: sh

   export APPIMAGE_EXTRACT_AND_RUN=1

Commandline integration of AppImage
+++++++++++++++++++++++++++++++++++

By convention AppImages are placed in ``~/Applications`` which is also added to ``$PATH`` environment variable to allow the AppImage applications to be easily launched from the commandline. We also add a simpler name for the commandline by soft linking the AppImage to that name:

.. code:: sh

   $ mkdir -p ~/Applications 
   $ mv torxakis-0.9.0.x86_64.AppImage ~/Applications
   $ echo 'export PATH=~/Applications/:$PATH' >> ~/.bashrc
   $ source ~/.bashrc
   $ ln -s torxakis-0.9.0.x86_64.AppImage ~/Applications/torxakis

Now you can start ``TorXakis`` from any path in your terminal just by typing ``torxakis``:

.. code:: sh

   $ torxakis
   
    TXS >>  TorXakis :: Model-Based Testing

    TXS >>  txsserver starting: "::ffff:127.0.0.1" : 41975
    TXS >>  Solver "z3" initialized : Z3 [4.8.5]
    TXS >>  TxsCore initialized
    TXS >>  LPEOps version 2019.07.05.02
    TXS >>  input files parsed:
    TXS >>  []
    TXS >> 

Desktop integration of AppImage
+++++++++++++++++++++++++++++++

You can even launch the AppImage from the Desktop Environment by integrating AppImages To Application Menu Using `AppImageLauncher`_. 
The following instructions installs `AppImageLauncher`_ on an Ubuntu linux installation:

.. code:: sh

    $ sudo add-apt-repository ppa:appimagelauncher-team/stable
    $ sudo apt update
    $ sudo apt install appimagelauncher

Now you can launch ``TorXakis`` from the desktop's application menu.

Note: for AppImage's which are GUI applications you get on first launch the integrate option into the desktop, however for AppImage's which are  commandline applications this doesn't happen and you must put the application in ``~/Applications/`` yourself. The reason for not automatically integrating commandline applications is because that some commandline applications need arguments to run, so running them from the desktop's application menu without arguments makes then no sense. Such a commandline application can better be placed in ``~/bin/`` instead of ``~/Applications/`` making it available on the commandline, but not on the desktop's application menu.

For debian based systems
^^^^^^^^^^^^^^^^^^^^^^^^

We provide a ``deb`` package for Debian based systems (Debian, Ubuntu, etc).
Below we give instructions on how to install ``TorXakis`` on Ubuntu 20.04.

Download the latest deb package for TorXakis from the TorXakis github
project's `releases page`_ and then run the following commands:

.. code:: sh

   apt-get update
   apt-get install ./torxakis_0.9.0-ubuntu_20.04-amd64.deb -y

Now you can launch ``TorXakis`` from the commandline with the command ``torxakis``.

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
.. _AppImageLauncher: 
