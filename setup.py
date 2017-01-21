#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

setup(
    name='pyprofile',
    version='0.0.1',
    license='Private',
    description='profile tools for python',
    author='lyc@zhihu.com',
    packages=['pyprofile'],
    install_requires='''
        gevent
        numpy
    ''',
    entry_points='''
    [console_scripts]
    ''',
)
