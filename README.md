#[![Build Status](https://travis-ci.org/new-mind/pyjs.svg)](https://travis-ci.org/new-mind/pyjs) NOT READY YET!
Python bridge for javascript on base SpiderMonkey


mozjs-31.2.0

#Usage

```python
import pyjs

rt = pyjs.Runtime()
context = rt.Context()
rt.execute('var a = 1')
```

#Installing

##Pyjs

* python setup.py build/install

##Mozjs

For compiling mozjs needed 2.7.3 < python < 3

* `./install.sh --download`
* `./install.sh --build`

##Testing

* `python setup.py test`
