class Config:
    '''
    This is the parent configuration class
    '''
    NEWS_BASE_URL='https://newsapi.org/v2/everything/{}?&apikey={}'
    pass


class ProdConfig(Config):
    '''
    production configuration class which is a child of config class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class, child of the class Config
    '''
    DEBUG=True