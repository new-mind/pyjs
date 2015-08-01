#[![Build Status](https://travis-ci.org/new-mind/pyjs.svg)](https://travis-ci.org/new-mind/pyjs) NOT READY YET!
Python bridge for javascript on base SpiderMonkey


mozjs-31.2.0

#Usage

```python
import pyjs

rt = pyjs.Runtime()
cx = rt.Context()
cx.eval('var a = 1')
```

#Installing

Support yet only static linking

##Pyjs

* python setup.py build/install

##Mozjs (installing)

For compiling mozjs needed 2.7.3 < python < 3

* `./setup.sh --download`
* `PYTHON=pythonExc ./setup.sh --build`  
   `pythonExc` - name of python executable
* `./setup.sh --install`

##Mozjs (local)

* `MOZJS_INCLUDE_DIRS` - path to jsapi headers
* `MOZJS_LIB_DIRS` - path to libmozjs-31

##Testing

* `python setup.py test`

##Thanks

* Paul J. Davis (python-spidermonkey)
