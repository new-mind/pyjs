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
                        extra_compile_args=['-std=gnu++0x',])

setup(name='pyjs',
      version='1.0.0dev1',
      description='Python-javascript bridge',
      url="https://github.com/new-mind/pyjs",
      author='jiojiajiu',
      author_email='jiojiajiu@gmail.com',
      license='MIT',
      ext_modules=[ext,],
      test_suite="tests",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
      ],
      keywords='javascript development spidermonkey')
