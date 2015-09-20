#!/usr/bin/env python
import os
from os import path
from setuptools import setup, Extension
import subprocess

def find_sources():
    return [
        os.path.join(d, f)
            for (d, dpath, files) in os.walk('src')
                for f in files if f.endswith('.cpp')
    ]

class JSConfig(object):
    def get_cflags(self):
        return subprocess.check_output(['js-config', '--cflags']).split()
    def get_library_dirs(self):
        return subprocess.check_output(['js-config', '--libdir']).split()
    def get_library_dirs(self):
        return subprocess.check_output(['js-config', '--libdir']).split()

js_config = JSConfig()
pyjs = Extension('py_js', sources=find_sources(),
        language = 'c++',
        library_dirs = js_config.get_library_dirs(),
        libraries = ['mozjs-31', 'm', 'dl'],
        extra_compile_args = js_config.get_cflags())

setup(name='py_js',
      version='1.0.1.dev1',
      description='Python-javascript bridge',
      url="https://github.com/new-mind/pyjs",
      author='jiojiajiu',
      author_email='jiojiajiu@gmail.com',
      license='MIT',
      ext_modules=[pyjs],
      test_suite="tests",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: JavaScript'
      ],
      keywords='javascript development spidermonkey')
