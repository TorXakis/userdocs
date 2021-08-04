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

We provide  `TorXakis` packaged as an `AppImage`_ which is a portable package format which works on all 
linux distributions and (recent) releases. The  `TorXakis` Appimage is a software bundle which contains everything to run `TorXakis`. It therefore also contains the specific versions of `cvc4` and `z3` tools which `TorXakis` requires when running.

To run the AppImage, simply download it from the github's release page, make it executable 
and we then can just run it:

.. code:: sh

    $ wget https://github.com/TorXakis/TorXakis/releases/download/v0.9.0/torxakis-0.9.0.x86_64.AppImage
    $ chmod a+x torxakis-0.9.0.x86_64.AppImage
    $ ./torxakis-0.9.0.x86_64.AppImage


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

Note: for AppImage's which are GUI applications you get on first launch the integrate option into the desktop, however for AppImage's which are  commandline applications this doesn't happen and you must put the application in ``~/Applications/`` yourself. The reason for not automatically integrating commandline applications is that some commandline applications need arguments to run. So running them from the desktop's application menu without arguments makes then no sense. Such commandline applications can better be placed in ``~/bin/`` instead of ``~/Applications/``. Making them available on the commandline, but not on the desktop's application menu.

Running within a Docker Container
+++++++++++++++++++++++++++++++++

When the AppImage is run, then by its `architecture <AppImageArch_>`_, its runtime part is executed which mounts its diskimage part using FUSE readonly. Then it runs the application on the mounted image using all libraries and depending utilities within the image. Only libraries which are always available on every linux system are not included in the AppImage. In this way the AppImage can guarantee it will run on every (recent) release of any linux distribution.

However most Docker installations do not permit the use of FUSE inside containers for security reasons. Instead, you can `extract and run an AppImage`_ without using FUSE. To run the AppImage within a Docker container, without using FUSE, you must set the following environment variable: 

.. code:: sh

   export APPIMAGE_EXTRACT_AND_RUN=1


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
.. _AppImageLauncher: https://github.com/TheAssassin/AppImageLauncher
.. _AppImage: https://appimage.org
.. _AppImageArch: https://docs.appimage.org/reference/architecture.html
.. _extract and run an AppImage: https://docs.appimage.org/user-guide/troubleshooting/fuse.html#extract-and-run-type-2-appimages

