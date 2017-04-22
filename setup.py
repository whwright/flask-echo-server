#!/usr/bin/env python

from setuptools import setup

setup(name='flask-echo-server',
      version='1.0',
      description='JSON echo server written with Flask',
      author='W. Harrison Wright',
      author_email='me@whw.io',
      url='https://github.com/whwright/flask-echo-server',
      py_modules=['echo'],
      requires=['flask'],
      install_requires=['flask>=0.10'],
      entry_points={
        'console_scripts': [
            'flask-echo = echo:main'
        ]
      }
     )
