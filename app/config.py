class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-02&sortBy=publishedAt&apiKey=f7fd95001a4d451d9bdbd52c83f61b27'


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
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