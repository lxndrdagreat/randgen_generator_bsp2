#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import randgen_generator_bsp2

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='randgen_generator_bsp2',
    version=randgen_generator_bsp2.__version__,
    description="A BSP random map generator module for randgen.io",
    long_description=readme + '\n\n' + history,
    author="Dan Alexander",
    author_email='lxndrdagreat@gmail.com',
    url='https://github.com/lxndrdagreat/randgen_generator_bsp2',
    packages=[
        'randgen_generator_bsp2',
    ],
    package_dir={'randgen_generator_bsp2':
                 'randgen_generator_bsp2'},
    entry_points={
        'console_scripts': [
            'randgen_generator_bsp2=randgen_generator_bsp2.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    dependency_links=[
        'git+git@github.com:lxndrdagreat/randgen_maptools.git',
        'git+git@github.com:lxndrdagreat/randgen_generator_bsp.git'
    ],
    license="MIT license",
    zip_safe=False,
    keywords='randgen_generator_bsp2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
