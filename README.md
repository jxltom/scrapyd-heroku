# scrapyd-heroku

A wrapper for running [Scrapyd](https://github.com/scrapy/scrapyd) in [Heroku](https://heroku.com/) or in console as normal Scrapyd service.

## Features

- Support running Scrapyd service in ```80``` port with http or ```443``` port with https in Heroku
- Support running Scrapyd in console as normal Scrapyd service
- Support latest version of Scrapy ```1.3.2``` and Scrapyd ```1.2.0a1```
    
## Getting Started

- Add ```scrapyd-heroku``` which is available in PyPI to ```requirements.txt``` in your application and add ```web: scrapyd-heroku``` to ```Procfile```. Thre is a demo in [heroku-demo](https://github.com/jxltom/scrapyd-heroku/tree/heroku-demo) branch.

- Or you can [fork this repository](https://github.com/jxltom/scrapyd-heroku/fork) and deploy it in Heroku directly.
