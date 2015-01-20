#!/usr/bin/env python
from setuptools import setup

from phantomas import __version__

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='phantomas',
    version=__version__,
    description='Python module for easy integration with phantomas',
    long_description=long_description,
    url='https://github.com/macbre/phantomas-python',
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    install_requires=[
        'pytest==2.6.4',
    ],
    include_package_data=True,
)
