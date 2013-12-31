#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

__version__ = '0.1.0'

meta = dict(
    name='cleaner',
    version=__version__,
    description='Tool to clean out a filesystem path at fixed intervals.',
    long_description=open('README').read(),
    author="Ryan Faulkner",
    author_email="bobs.ur.uncle@gmail.com",
    url='https://github.com/rfaulkner/cleaner',
    scripts=['clean'],
    entry_points={
        'console_scripts': [
            'git-deploy = git_deploy.git_deploy_console:cli'
        ]
    },
    keywords=['scripts', 'cli'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: Version Control",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "License :: OSI Approved :: MIT License",
    ],
    zip_safe=False,
    license="License :: OSI Approved :: BSD License",
)

# Automatic conversion for Python 3 requires distribute.
if False and sys.version_info >= (3,):
    meta.update(dict(
        use_2to3=True,
    ))

setup(**meta)