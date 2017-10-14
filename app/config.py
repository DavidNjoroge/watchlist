class Config:
    '''
    General configurations
    '''
    pass

class ProdConfig(Config):
    '''
    production configuration child class

    args:
        config: the parent class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    args:
        config: the parent class
    '''

    DEBUG = True
