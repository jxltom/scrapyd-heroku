# scrapyd-heroku

Wrapper for running [Scrapyd](https://github.com/scrapy/scrapyd) in [Heroku](https://heroku.com/) or locally as a service

## Features

- Support running Scrapyd service in Heroku
- Support running Scrapyd service locally
- Support latest version of Scrapy ```2.4.1``` and Scrapyd ```1.2.1```
    
## Getting Started

- Simply [fork this repository](https://github.com/jxltom/scrapyd-heroku/fork), update custom configurations in ```scrapy.conf```, and deploy it to Heroku

- Or [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/jxltom/scrapyd-heroku) from this repo directly, and then the service will be exposed such as in ```https://scrapyd-heroku.herokuapp.com/```

- Or ```pip install scrapyd-heroku``` and run ```scrapyd-heroku``` locally

- Or [fork this repository](https://github.com/jxltom/scrapyd-heroku/fork) and run ```python manage.py``` locally
