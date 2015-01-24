#!/usr/bin/env python
from setuptools import setup, find_packages

from phantomas import __version__

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='phantomas',
    version=__version__,
    description='Python module for easy integration with phantomas',
    long_description=long_description,
    url='https://github.com/macbre/phantomas-python',
    license='MIT',
    keywords=[
        "high performance web sites",
        "metrics",
        "monitoring",
        "phantomas",
        "phantomjs",
        "web development",
        "webperf"
    ],
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    install_requires=[
        "coverage==3.7.1",
        'pytest==2.6.4',
        "pep8==1.5.7",
        "pylint==1.2.1",
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
