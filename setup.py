from setuptools import setup, Extension

ext = Extension('pyjs', sources = ['src/Runtime.cpp'])

setup(name='pyjs',
      version='0.0.1',
      autho='jiojiajiu',
      email='jiojiajiu@gmail.com',
      ext_modules=[ext,])
