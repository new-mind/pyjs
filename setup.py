import os
from os import path
from setuptools import setup, Extension

os.environ['CC'] = 'g++'

MOZJS = 'temp/js/js/src/dist'
INCLUDE_DIRS = [path.join(MOZJS, 'include'),]
LIB_DIRS = [path.join(MOZJS, 'lib'),]

ext = Extension('pyjs', sources=['src/main.cpp', 'src/Runtime.cpp'],
                        language='c++',
                        include_dirs=INCLUDE_DIRS,
                        library_dirs=LIB_DIRS,
                        libraries=['mozjs-31',],
                        extra_compile_args=['-std=c11'])

setup(name='pyjs',
      version='0.0.1',
      author='jiojiajiu',
      ext_modules=[ext,],
      test_suite="tests",
      )
