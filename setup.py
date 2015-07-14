#!/usr/bin/env python
import os
from os import path
from setuptools import setup, Extension

os.environ['CC'] = 'c++'
def parse_path_environ(key):
    env = os.environ.get(key)
    if not env:
        return None
    return env.split(':')

MOZJS_INCLUDE_DIRS = parse_path_environ('MOZJS_INCLUDE_DIRS')
MOZJS_LIB_DIRS = parse_path_environ('MOZJS_LIB_DIRS')

MOZJS = 'temp/build/dist'
INCLUDE_DIRS = MOZJS_INCLUDE_DIRS or [path.join(MOZJS, 'include')]
LIB_DIRS = MOZJS_LIB_DIRS or [path.join(MOZJS, 'lib'),]

ext = Extension('pyjs', sources=['src/main.cpp', 'src/Runtime.cpp', 'src/Context.cpp', 'src/utils/convert.cpp'],
                        language='c++',
                        include_dirs=INCLUDE_DIRS,
                        library_dirs=LIB_DIRS,
                        libraries=['mozjs-31'],
                        extra_compile_args=['-std=c++11'])

setup(name='pyjs',
      version='0.0.1',
      author='jiojiajiu',
      ext_modules=[ext,],
      test_suite="tests",
      )
