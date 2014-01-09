#!/usr/bin/env python
#
#  Copyright (c) 2010-2012 Corey Goldberg (corey@goldb.org)
#  License: GNU LGPLv3
#
#  This file is part of Multi-Mechanize | Performance Test Framework
#


"""
setup.py for pyak47
"""

import os

from setuptools import setup, find_packages

from pyak47 import __version__


this_dir = os.path.abspath(os.path.dirname(__file__))


NAME = 'pyak47'
VERSION = __version__
PACKAGES = find_packages(exclude=['ez_setup'])
DESCRIPTION = 'pyak47 - Performance Test Framework'
URL = 'https://github.com/kakwa/pyak47/'
LICENSE = 'GNU LGPLv3'
LONG_DESCRIPTION = open(os.path.join(this_dir, 'README.rst')).read()
REQUIREMENTS = filter(None, open(os.path.join(this_dir, 'requirements.txt')).read().splitlines())
AUTHOR = 'Pierre-Francois Carpentier'
AUTHOR_EMAIL = 'carpentier.pf@gmail.com'
KEYWORDS = ('performance', 'scalability', 'load', 'test', 'testing', 'benchmark')
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Testing',
    'Topic :: Software Development :: Testing :: Traffic Generation',
    'Topic :: System :: Benchmark',
]
CONSOLE_SCRIPTS = [
    'pyak47-run = multimechanize.utilities.run:main',
    'pyak47-newproject = multimechanize.utilities.newproject:main',
    'pyak47-gridgui = multimechanize.utilities.gridgui:main',
]


params = dict(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    install_requires = REQUIREMENTS,

    # metadata for upload to PyPI
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    entry_points = { 'console_scripts': CONSOLE_SCRIPTS }
)

setup(**params)
