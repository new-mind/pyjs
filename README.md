#NOT READY YET!
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
* Available environment variables:
  INCLUDE_MOZJS - include dir
  LIBRARY_MOZJS - library dir

##Mozjs

For compiling mozjs needed python > 3

* ./install.sh
* cd temp/js/js/src/
* ./compile --prefix=../../../build
* make

##Testing

* python setup.py test
