# -*- coding: utf-8 -*-
"""
:author: Pawel Chomicki
"""
from setuptools import setup


requires = [
    'mock>=1.0.1',
]


setup(
    name="pytest_spec",
    version="0.1",
    entry_points={'pytest11': ['pytest_spec = pytest_spec.plugin']},
    description="Pytest plugin to print more spec report than only execution result",
    author="Pawel Chomicki",
    author_email="pawel.chomicki@gmail.com",
    install_requires=requires,
)