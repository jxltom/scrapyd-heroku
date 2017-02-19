# scrapyd-heroku

A wrapper for running [Scrapyd](https://github.com/scrapy/scrapyd) in [Heroku](https://heroku.com/) or in console as normal Scrapyd service.

## Features

- Support running Scrapyd service in ```80``` port in Heroku
- Support running Scrapyd in console as normal Scrapyd service
- Support latest version of Scrapy ```1.3.2``` and Scrapyd ```1.2.0a1```
    
## Getting Started

- Add ```scrapyd-heroku``` which is available in PyPI to ```requirements.txt``` in your application and add ```web: scrapyd_heroku``` to ```Procfile```.

- Or you can [fork this repository](https://github.com/jxltom/scrapyd-heroku#fork-destination-box) and deploy it in Heroku directly.
