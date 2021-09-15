Installation
------------

Binary Install
^^^^^^^^^^^^^^

Windows
~~~~~~~

For Windows systems an installer is provided in the TorXakis github project's `releases page`_.

MacOS
~~~~~

For macOS systems we provide a homebrew package. To install ``TorXakis``
run:

.. code:: sh

   brew tap torxakis/torxakis
   brew install torxakis

For more detailed instructions see the `Homebrew tap for TorXakis`_.


Linux
~~~~~

We provide  `TorXakis` packaged as an `AppImage`_ which is a portable package format which works on all 
linux distributions and (recent) releases. The  `TorXakis` Appimage is a software bundle which contains everything to run `TorXakis`.
It therefore also contains the specific versions of `cvc4` and `z3` tools which `TorXakis` requires when running.

To run the AppImage, simply download it from the github's release page, make it executable 
and we then can just run it:

.. code:: sh

    $ wget https://github.com/TorXakis/TorXakis/releases/download/v0.9.0/torxakis-0.9.0.x86_64.AppImage
    $ chmod a+x torxakis-0.9.0.x86_64.AppImage
    $ ./torxakis-0.9.0.x86_64.AppImage


Install the AppImage in a directory in your shell's PATH with the convenient ``torxakis`` alias:

.. code:: sh

    $ BINDIR=/usr/local/bin    # an alternative is ~/bin in your home directory
    $ mv torxakis-0.9.0.x86_64.AppImage $BINDIR/
    $ ln -s torxakis-0.9.0.x86_64.AppImage $BINDIR/torxakis

By using a softlink for ``torxakis`` we can easily switch to a different version of the AppImage.

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


Running the AppImage without FUSE support (eg. in a Docker Container)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

When the AppImage is run, then by its `architecture <AppImageArch_>`_, its runtime part is executed which mounts its diskimage part using FUSE readonly. Then it runs the application on the mounted image using all libraries and depending utilities within the image. Only libraries which are always available on every linux system are not included in the AppImage. In this way the AppImage can guarantee it will run on every (recent) release of any linux distribution.

However some linux distributions do no support FUSE directly out of the box. You can either `install FUSE`_  or you can `extract and run an AppImage`_ without using FUSE. You can easily run the AppImage, without using FUSE, by just setting the following environment variable: 

.. code:: sh

   export APPIMAGE_EXTRACT_AND_RUN=1
   
Most Docker installations do not permit the use of FUSE inside containers for security reasons. So running without FUSE is required to run an AppImage in a Docker container.  So just by setting the  above environment variable in the Docker container lets Docker still run the AppImage. 
   



Source build
^^^^^^^^^^^^

One can also build torxakis from source yourself. The latest stable source
is provided in the TorXakis github project's `releases page`_. The latest development
source code can fetch from the ``develop`` branch on the ``TorXakis`` github project
site at https://github.com/TorXakis/TorXakis/. Look at the developers
documentation for `the build instructions`_.

.. _Homebrew tap for TorXakis: https://github.com/TorXakis/homebrew-TorXakis
.. _releases page: https://github.com/TorXakis/TorXakis/releases
.. _the build instructions: https://torxakis.org/develdocs/stable/building.html
