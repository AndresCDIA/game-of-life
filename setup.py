#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

PACKAGE = "gol"
NAME = "gol"
DESCRIPTION = "Python curses implementation of Conway's Game Of Life with an evolutionary twist"
AUTHOR = "Chris Seymour"
AUTHOR_EMAIL = "chris.j.seymour@hotmail.com"
AUTHOR_TWITTER = "@iiSeymour"
URL = "https://github.com/iiSeymour/game-of-life"

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=NAME,
    version=0.7,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=read("LICENSE"),
    url=URL,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Topic :: Games/Entertainment :: Simulation",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'gol=conway.gol:main',
        ]
    }
)
