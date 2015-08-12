Python bridge for javascript on base SpiderMonkey (mozjs-31.2.0) |Build
Status|

**Support yet only static linking**

Usage
=====

.. code:: python

    import py_js as pyjs

    rt = pyjs.Runtime()
    cx = rt.Context()
    cx.eval('var a = 1')

Installing
==========

From PIP
--------

-  python install py-js

From source
-----------

-  python setup.py build/install

Mozjs (installing)
------------------

For compiling mozjs needed 2.7.3 < python < 3 (``MOZJS_PYTHON`` env
variable)

-  ``./setup.sh --download``
-  ``PYTHON=pythonExc ./setup.sh --build``, ``pythonExc`` - name of
   python executable
-  ``./setup.sh --install``

Mozjs (local)
-------------

-  ``MOZJS_INCLUDE_DIRS`` - path to jsapi headers
-  ``MOZJS_LIB_DIRS`` - path to libmozjs-31
-  ``MOZJS_PYTHON`` - 2.7.3 < python < 3, default=\ ``python2.7.5``

Depencencies
~~~~~~~~~~~~

-  2.7.3 < python < 3 - for mozjs
-  CC = clang
-  CXX = clang++

Testing
=======

-  python setup.py test

Thanks
======

-  Paul J. Davis
   (`python-spidermonkey <https://pypi.python.org/pypi/python-spidermonkey>`__)

.. |Build Status| image:: https://travis-ci.org/new-mind/pyjs.svg?branch=master
   :target: https://travis-ci.org/new-mind/pyjs
