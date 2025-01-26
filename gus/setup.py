from __future__ import print_function

"""Setup script for GUS API Python client.

Also installs included versions of third party libraries, if those libraries
are not already installed.
"""

import io
import os

import sys
from pathlib import Path

if sys.version_info < (3, 12):
    print("google-api-python-client requires python3 version >= 3.12.", file=sys.stderr)
    sys.exit(1)


from setuptools import setup, find_packages
from gus_api.version import __version__
author = 'Radek Miernicki'
author_email = 'radoslaw.miernicki@ecoloopgroup.pl',
setup(
    name='gus-api-client',
    version = __version__,
    author = author,
    packages = find_packages(),
    description = 'GUS API client.',
    url = 'https://github.com/RadekMiernicki/GusApi',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires = '>=3.12',
    install_requires = [
        'requests',
        'pydantic',
        'lxml',
        'zeep',
    ]
)

