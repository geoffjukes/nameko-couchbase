from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='nameko_couchbase',
    version='0.1.0',
    description='Nameko dependency for Couchbase',
    url='https://github.com/geoffjukes/nameko-couchbase',
    author='Geoff Jukes',
    license="Apache License, Version 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    keywords='nameko dependency couchbase',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['couchbase==2.5.1'],
)