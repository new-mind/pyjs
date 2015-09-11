#!/usr/bin/env python
import os
from os import path
from setuptools import setup, Extension
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.build_ext import build_ext
from setuptools.command.test import test
import subprocess
from copy import deepcopy

def parse_path_environ(key):
    env = os.environ.get(key)
    if not env:
        return None
    return env.split(':')

MOZJS_INCLUDE_DIRS = parse_path_environ('MOZJS_INCLUDE_DIRS')
MOZJS_LIB_DIRS = parse_path_environ('MOZJS_LIB_DIRS')
MOZJS_PYTHON = os.environ.get('MOZJS_PYTHON', 'python2.7')
MOZJS_PYTHON = subprocess.check_output(['which', MOZJS_PYTHON])

MOZJS = 'temp/build'
INCLUDE_DIRS = MOZJS_INCLUDE_DIRS or [path.join(MOZJS, 'include/mozjs-31/')]
LIB_DIRS = MOZJS_LIB_DIRS or [path.join(MOZJS, 'lib'),]

def find_sources():
    return [
        os.path.join(d, f)
            for (d, dpath, files) in os.walk('src')
                for f in files if f.endswith('.cpp')
    ]


class CustomBuildExt(build_ext):
    user_options = build_ext.user_options + [
        ('static', None, 'create with static linking',),
        ('mozjs', None, 'download and build mozjs'),]

    def initialize_options(self):
        self.mozjs = None
        self.static = None
        build_ext.initialize_options(self)

    def finalize_options(self):
        build_ext.finalize_options(self)
        self.pyjs_ext = next(ext for ext in self.extensions if ext.name == 'py-js')

        self.pyjs_ext.languages = 'c++'
        self.pyjs_ext.library_dirs = LIB_DIRS
        self.pyjs_ext.include_dirs = INCLUDE_DIRS
#TODO:
        self.pyjs_ext.libraries = ['z', 'm', 'dl']
        self.pyjs_ext.extra_compile_args = ['-std=gnu++0x']
        if self.static:
            self.pyjs_ext.extra_objects = [path.join(MOZJS, 'lib/libmozjs-31.a')]

    def run(self):
        if self.mozjs:
            self.run_mozjs()

        build_ext.run(self)

    def run_mozjs(self):
        subprocess.check_call(['bash', 'setup.sh', '--download'])

        env = deepcopy(os.environ)
        env['PYTHON'] = MOZJS_PYTHON
        resp = subprocess.Popen(['bash', 'setup.sh', '--build'], env=env).wait()
        if resp != 0:
            raise Exception("There is an exception in --build step")
        subprocess.check_call(['bash', 'setup.sh', '--install'])

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='py-js',
      cmdclass={
          'build_ext': CustomBuildExt
      },
      version='1.0.0a2',
      description='Python-javascript bridge',
      long_description=read('README.rst'),
      url="https://github.com/new-mind/pyjs",
      author='jiojiajiu',
      author_email='jiojiajiu@gmail.com',
      license='MIT',
#TODO:
# extra_compile_args through ./js-config --extraflags
      ext_modules=[Extension('py-js', sources=find_sources()) ],
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
