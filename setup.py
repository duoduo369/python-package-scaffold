# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup

PACKAGE_NAME = ''
PACKAGE_PATH = ''

version = __import__(PACKAGE_PATH).__version__

SHORT_DESCRIPTION = ''''''

LONG_DESCRIPTION = ''''''

def long_description():
    """Return long description from README.md if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name=PACKAGE_NAME,
      version=version,
      author='duoduo369',
      author_email='duoduo3369@gmail.com',
      description= SHORT_DESCRIPTION,
      license='MIT',
      keywords='',
      url='',
      download_url='',
      packages=[''],
      long_description=long_description(),
      install_requires=[],
      classifiers=[
                   'Development Status :: 4 - Beta',
                   'Topic :: Internet',
                   'License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 2.7'],
      zip_safe=False)
