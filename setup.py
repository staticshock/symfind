#!/usr/bin/env python

from distutils.core import setup
import symfind

PROJECT = u'symfind'
AUTHOR = u'Anton Backer'
AUTHOR_EMAIL = u'olegov@gmail.com'
DESC = u'Find out which linked libs undefined symbols live in'


setup(
    name=PROJECT,
    version=symfind.__version__,
    description=DESC,
    long_description=open('README.rst').read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license='MIT',
    entry_points={
        'console_scripts': [
            u'symfind = symfind:main',
        ],
    },
    py_modules=[u'symfind'])
