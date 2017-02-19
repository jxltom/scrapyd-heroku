import os

from scrapy.utils.misc import load_object
from scrapyd.config import Config


def get_application(config=None):
    """Overide default get_application in Scrapy."""
    if config is None:
        config = Config()
        # Overide http_port by $PORT environment variable in Heroku.
        # Note that the http_port has to be a string intead of int.
        config.cp['scrapyd'].update(
            http_port=os.environ.get('PORT', config.get('http_port')))
    apppath = config.get('application', 'scrapyd.app.application')
    appfunc = load_object(apppath)
    return appfunc(config)

# Create Twisted application.
application = get_application()
