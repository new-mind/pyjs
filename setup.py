#!/usr/bin/env python
import os
from os import path
from setuptools import setup, Extension

#TODO:
os.environ['CC'] = 'c++'

def parse_path_environ(key):
    env = os.environ.get(key)
    if not env:
        return None
    return env.split(':')

MOZJS_INCLUDE_DIRS = parse_path_environ('MOZJS_INCLUDE_DIRS')
MOZJS_LIB_DIRS = parse_path_environ('MOZJS_LIB_DIRS')

MOZJS = 'temp/build'
INCLUDE_DIRS = MOZJS_INCLUDE_DIRS or [path.join(MOZJS, 'include/mozjs-31/')]
LIB_DIRS = MOZJS_LIB_DIRS or [path.join(MOZJS, 'lib'),]

def find_sources():
    return ['src/main.cpp', 'src/Runtime.cpp', 'src/Context.cpp', 'src/utils/convert.cpp']
    return [
        os.path.join(d, f)
            for (d, dpath, files) in os.walk('src')
                for f in files if f.endswith('.cpp')
    ]

#TODO:
# extra_compile_args through ./js-config --extraflags
ext = Extension('pyjs', sources=find_sources(),
                        language='c++',
                        include_dirs=INCLUDE_DIRS,
                        library_dirs=LIB_DIRS,
                        libraries=['z', 'm', 'dl'],
                        extra_objects=[path.join(MOZJS, 'lib/libmozjs-31.a')],
                        extra_compile_args=['-std=c++11', '-w'])

setup(name='pyjs',
      version='0.0.1',
      author='jiojiajiu',
      ext_modules=[ext,],
      test_suite="tests",
      )
