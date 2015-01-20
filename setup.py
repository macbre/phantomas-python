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
        'pytest==2.6.4',
    ],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP"
    ]
)
