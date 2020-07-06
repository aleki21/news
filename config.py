import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    # CAT_API_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    CAT_API_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    NEWS_API_KEY= 'f7fd95001a4d451d9bdbd52c83f61b27'


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
