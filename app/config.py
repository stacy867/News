class Config:
    '''
    General configuration parent class
    '''
    NEWS_ARTICLE_BASE_URL ='https://newsapi.org/v2/everything{}?q=bitcoin&apiKey={}'
    NEWS_SOURCE_BASE_URL='https://newsapi.org/v2/sources{}?apiKey={}'
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