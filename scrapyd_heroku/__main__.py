from sys import argv

from twisted.scripts.twistd import run


def main():
    """Entrypoint for script or exe."""
    argv[1:1] = ['-n', '-y', 'app.py']
    run()


if __name__ == '__main__':
    # Entrypoint for Heroku/Dokku/Flynn.
    main()
