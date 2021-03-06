|Build Status|

Python bridge for javascript on base SpiderMonkey

At this moment library does not support converting python variables to javascript variables and back. Use ``json.dumps`` and ``JSON.parse`` to communicate each other.

`Installing <INSTALL.rst>`__
============================

`API <http://docs.pyjs.apiary.io/>`__
=====================================

Usage
=====

.. code:: python

    import pyjs

    cx = pyjs.Context()
    cx.eval('var a = 1')

.. code:: python

    import pyjs

    cx = pyjs.Context()
    cx.setGlobal("intVar", 1)
    cx.setGlobal("object", {'type': 'someGlobalObject'})
    cx.eval('intVar * 2')


Testing
=======

-  python setup.py test

Thanks
======

-  Paul J. Davis
   (`python-spidermonkey <https://pypi.python.org/pypi/python-spidermonkey>`__)
-  Flier Lu (`pyv8 <https://code.google.com/p/pyv8/>`__)

.. |Build Status| image:: https://travis-ci.org/new-mind/pyjs.svg?branch=master
   :target: https://travis-ci.org/new-mind/pyjs
