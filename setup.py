#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

execfile('lib/xapers/version.py')

setup(
    name = 'xapers',
    version = __version__,
    description = 'Xapian article indexing system.',
    author = 'Jameson Rollins',
    author_email = 'jrollins@finestructure.net',
    url = '',

    package_dir = {'': 'lib'},
    packages = [
        'xapers',
        'xapers.parsers',
        'xapers.sources',
        'xapers.nci',
        ],
    scripts = ['bin/xapers'],

    requires = [
        'xapian',
        'pybtex',
        'urwid'
        ],
    )
