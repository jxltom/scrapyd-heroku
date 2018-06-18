#!/usr/bin/env python

from os.path import join, dirname
from sys import argv

from twisted.scripts.twistd import run

import scrapyd_heroku as project


def main():
    argv[1:1] = ['-n', '-y', join(dirname(project.__file__), 'app.py')]
    run()


if __name__ == '__main__':
    main()
