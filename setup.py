from setuptools import setup

from phantomas import __version__

setup(
    name='phantomas',
    version=__version__,
    description='Python module for easy integration with phantomas',
    url='https://github.com/macbre/phantomas-python',
    author='Maciej Brencz',
    author_email='maciej.brencz@gmail.com',
    install_requires=[
        'pytest==2.6.4',
    ],
    include_package_data=True,
)
