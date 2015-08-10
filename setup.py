#!/usr/bin/env python
import os
from os import path
from setuptools import setup, Extension
from setuptools.command.install import install
import subprocess

#TODO:
os.environ['CC'] = 'clang'

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
    return [
        os.path.join(d, f)
            for (d, dpath, files) in os.walk('src')
                for f in files if f.endswith('.cpp')
    ]

#TODO:
# extra_compile_args through ./js-config --extraflags
ext = Extension('py-js', sources=find_sources(),
                        language='c++',
                        include_dirs=INCLUDE_DIRS,
                        library_dirs=LIB_DIRS,
                        libraries=['z', 'm', 'dl'],
                        extra_objects=[path.join(MOZJS, 'lib/libmozjs-31.a')],
                        extra_compile_args=['-std=gnu++0x',])

class CustomInstall(install):
    def run(self):
        subprocess.call(['bash', 'setup.sh', '--download'])
        subprocess.call(['bash', 'setup.sh', '--build'])
        subprocess.call(['bash', 'setup.sh', '--install'])
        install.run(self)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='py-js',
      cmdclass={'install': CustomInstall},
      version='1.0.0.dev3',
      description='Python-javascript bridge',
      long_description = read('README.rst'),
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
