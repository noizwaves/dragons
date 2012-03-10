#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Dragons',
    version='0.0.1a',
    description='Dragons is a web scale psuedo-realistic load generator for web servers.',
    author='Adam Neumann',
    author_email='adam@noizwaves.com',
    url='http://dragons.noizwaves.com',
    packages=find_packages(),
    install_requires=['gevent==0.13.6', ], # TODO: geventhttpclient
    entry_points={
        'console_scripts': [
            'dragons = dragons.main:main',
        ]
    },
    classifiers=[
        'Development Status :: 1 - Alpha/Unstable',
    ],
)