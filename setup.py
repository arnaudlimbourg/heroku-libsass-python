#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import heroku-libsass-python
version = heroku-libsass-python.__version__

setup(
    name='heroku-libsass-python',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'heroku-libsass-python',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['heroku-libsass-python/manage.py'],
)
