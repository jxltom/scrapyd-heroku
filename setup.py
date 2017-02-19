#!/usr/bin/env python

from setuptools import setup, find_packages

from scrapyd_heroku import __version__, __author__

setup(
    name='scrapyd-heroku',
    version=__version__,
    description='A wrapper for running Scrapyd in Heroku '
                'or in console as normal Scrapyd service',
    long_description=
    'Go to https://github.com/jxltom/scrapyd-heroku/ for more information.',
    author=__author__,
    author_email='jxltom@gmail.com',
    url='https://github.com/jxltom/scrapyd-heroku/',
    license='MIT',

    include_package_data=True,

    packages=find_packages(),
    install_requires=[
        'scrapy>=1.3.2',
        'scrapyd>=1.2.0a1',
    ],

    entry_points={
        'console_scripts': [
            'scrapyd-heroku = scrapyd_heroku.__main__:main'
        ],
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
