import os
from setuptools import setup, Extension

MOZJS = 'src/js/js/src'
INCLUDE_DIRS = os.environ.get('INCLUDE_MOZJS', MOZJS)
LIBRARY_DIRS = os.environ.get('LIBRARY_MOZJS', MOZJS)

ext = Extension('pyjs', sources=['src/Runtime.cpp'],
                        include_dirs=[INCLUDE_DIRS,],
                        library_dirs=[LIBRARY_DIRS,],)

setup(name='pyjs',
      version='0.0.1',
      autho='jiojiajiu',
      email='jiojiajiu@gmail.com',
      ext_modules=[ext,],
      test_suite="tests",
      )
