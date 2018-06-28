#!/usr/bin/env python

import six
from setuptools import setup

try:
    from pip._internal.req import parse_requirements
except:
    from pip.req import parse_requirements
requirements_path = 'requirements.txt'
if six.PY2:
    requirements_path = 'requirements_py2.txt'
install_reqs = parse_requirements(requirements_path, session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='nlg-eval',
      version='2.0',
      description="Wrapper for multiple NLG evaluation methods and metrics.",
      author='Shikhar Sharma, Hannes Schulz',
      author_email='shikhar.sharma@microsoft.com, hannes.schulz@microsoft.com, justin.harris@microsoft.com',
      url='https://github.com/Maluuba/nlg-eval',
      packages=['nlgeval'],
      scripts=['bin/nlg-eval'],
      install_requires=reqs)