|Build Status|

Python bridge for javascript on base SpiderMonkey

`Installing <INSTALL.rst>`__
============================


Usage
=====

.. code:: python

    import py_js as pyjs

    rt = pyjs.Runtime()
    cx = rt.Context()
    cx.eval('var a = 1')


Testing
=======

-  python setup.py test

Thanks
======

-  Paul J. Davis
   (`python-spidermonkey <https://pypi.python.org/pypi/python-spidermonkey>`__)

.. |Build Status| image:: https://travis-ci.org/new-mind/pyjs.svg?branch=master
   :target: https://travis-ci.org/new-mind/pyjs
