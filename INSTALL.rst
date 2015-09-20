Notice
========
If you have any undescribed troubleshooting during installation please describe it `here <https://github.com/new-mind/pyjs/issues/new>`__ and I will post solution ASAP

First step
==========

| For usage the bridge you should have SpiderMonkey engine v31.2 (mozjs-31.2.0 bellow)
| Here you can find instruction for getting and building the engine
| Also looks `Mozilla reference <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Build_Documentation>`__
| Unfortunatly there is no needfull version in popular linux package managers so we will compile it from binary

Getting
-------

* ``wget https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2``
* ``tar xvf mozjs-31.2.0.rc0.tar.bz2``
* ``cd mozjs-31.2.0``

Building
--------
* ``cd js/src``
* ``./configure``
* ``make -j1``
  (``make -j1`` is `important <https://bugzilla.mozilla.org/show_bug.cgi?id=1006275>`__)
* ``sudo make install``

Dependencies
------------
* autoconf >= 2.13
* 2.7.3 < python < 3
* c/c++ compiler

Troubleshooting
---------------
-
    | checking for gcc... no
    | checking for cc... no
    | configure: error: no acceptable cc found in $PATH

  | It looks like you dont have c compiler on your system or mb in $PATH. Install compiler or edit $PATH variable
  | Ubuntu, for example:
  | ``sudo apt-get install build-essential``

-
    | checking for python2.7... no
    | checking for python... no
    | configure: error: python was not found in $PATH

  | No python right version ^^
  | ``sudo apt-get install python2.7``

-
    | Exception: Could not detect environment shell!
    | configure: error: Python environment does not appear to be sane.

  | ``export SHELL=/bin/bash``

-
    | configure: error: Your toolchain does not support C++0x/C++11 mode properly. Please upgrade your toolchain
  | Upgrade toolchain for support C++11 dialect


Second step
===========
| Now you can install the bridge

* ``pip install py-js``

Troubleshooting
---------------
-

    | $ pip install py-js
    | Downloading/unpacking py-js
    | Could not find a version that satisfies the requirement py-js (from versions: 1.0.0a1)

  ``pip install py-js --pre``
-
    | FileNotFoundError: [Errno 2] No such file or directory: 'js-config'

  Should install mozjs (see above)
