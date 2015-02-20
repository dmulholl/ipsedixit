#!/usr/bin/env python3
"""
Ipse Dixit
==========

This package runs a Markov chain algorithm over the surviving works of
the Roman historian Tacitus to generate naturalistic-looking pseudo-Latin
gibberish.

Can be used whenever you need to generate dummy text as a placeholder
in templates, etc.

Installs both as a library module and as a command line script.

See the project's `Github homepage <https://github.com/dmulholland/ipsedixit>`_
for further details.

Note that this package requires Python 3.

"""

import os
import re
import io

from setuptools import setup


filepath = os.path.join(os.path.dirname(__file__), 'ipsedixit', 'meta.py')
with io.open(filepath, encoding='utf-8') as metafile:
    regex = r'''^__([a-z]+)__ = ["'](.*)["']'''
    meta = dict(re.findall(regex, metafile.read(), flags=re.MULTILINE))


setup(
    name = 'ipsedixit',
    version = meta['version'],
    packages = ['ipsedixit'],
    package_data = {'': ['*.txt']},
    entry_points = {
        'console_scripts': [
            'ipsedixit = ipsedixit:cli',
        ],
    },
    author = 'Darren Mulholland',
    url = 'https://github.com/dmulholland/ipsedixit',
    license = 'Public Domain',
    description = 'Lorem ipsum on steroids.',
    long_description = __doc__,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'License :: Public Domain',
        'Intended Audience :: Developers',
    ],
    zip_safe = False,
)
