First step
==========

For usage the bridge you should have SpiderMonkey engine v31.2 (mozjs-31.2.0 bellow)
Here you can find instruction for getting and building the engine
Also looks `Mozilla reference <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey/Build_Documentation>`__

Getting
-------

* ``wget https://people.mozilla.org/~sstangl/mozjs-31.2.0.rc0.tar.bz2``
* ``tar xvf mozjs-31.2.0.rc0.tar.bz2``
* ``cd mozjs-31.2.0.rc0``

Building
--------
* ``cd js/js/src``
* ``./configure``
* ``make -j1 && make install``
    ``make -j1`` is `important <https://bugzilla.mozilla.org/show_bug.cgi?id=1006275>`__
