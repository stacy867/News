import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_ARTICLE_BASE_URL ='https://newsapi.org/v2/everything?q={}&apiKey={}'
    # NEWS_ARTICLE_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_SOURCE_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}