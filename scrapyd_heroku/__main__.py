from os.path import join, dirname
from sys import argv

from twisted.scripts.twistd import run

import scrapyd_heroku


def main():
    """Entrypoint for script or exe."""
    argv[1:1] = ['-n', '-y', join(dirname(scrapyd_heroku.__file__), 'app.py')]
    run()


if __name__ == '__main__':
    # Entrypoint for Heroku/Dokku/Flynn.
    main()
