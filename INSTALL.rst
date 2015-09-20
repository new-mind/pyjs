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
* ``make -j1 && make install``
  (``make -j1`` is `important <https://bugzilla.mozilla.org/show_bug.cgi?id=1006275>`__)

Dependencies
------------
* autoconf >= 2.13
* 2.7.3 < python < 3

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
