Python bridge for javascript on base SpiderMonkey (mozjs-31.2.0) |Build
Status|

Usage
=====

.. code:: python

    import py_js as pyjs

    rt = pyjs.Runtime()
    cx = rt.Context()
    cx.eval('var a = 1')

Installing
==========

-  python install --global-opition="build_ext --mozjs" py-js

Options (build_ext)
-------------------
- ``--mozjs`` - download, build and install mozjs, see below
- ``--static`` - compile extension with static linking, see below


Dependencies
------------

-  2.7.3 < python < 3 - for mozjs

Mozjs (installing)
~~~~~~~~~~~~~~~~~
Notice: Compiling mozjs spend much time (above 10minute) cause mozjs is compiling on one core, relax and take coffee

For compiling mozjs needed 2.7.3 < python < 3 (``MOZJS_PYTHON`` env
variable)

-  ``python setup.py build_ext --mozjs``, for make all the steps below

or

-  ``./setup.sh --download``
-  ``PYTHON=pythonExc ./setup.sh --build``, ``pythonExc`` - name of
   python executable
-  ``./setup.sh --install``

Mozjs ENV build variables 
++++++++++++++++++++++++

-  ``MOZJS_INCLUDE_DIRS`` - path to jsapi headers
-  ``MOZJS_LIB_DIRS`` - path to libmozjs-31
-  ``MOZJS_PYTHON`` - 2.7.3 < python < 3, default=\ ``python2.7``

Static linking
--------------
For compile py-js extension with static linking use command

``python setup.py build_ext --static``

Troubleshooting
---------------

- 

    | $ pip install py-js
    | Downloading/unpacking py-js
    | Could not find a version that satisfies the requirement py-js (from versions: 1.0.0a1)

  pip install py-js --pre


Testing
=======

-  python setup.py test

Thanks
======

-  Paul J. Davis
   (`python-spidermonkey <https://pypi.python.org/pypi/python-spidermonkey>`__)

.. |Build Status| image:: https://travis-ci.org/new-mind/pyjs.svg?branch=master
   :target: https://travis-ci.org/new-mind/pyjs
