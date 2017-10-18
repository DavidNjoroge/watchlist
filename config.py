import os


class Config:
    '''
    General configurations
    '''
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    # MOVIE_API_KEY = os.environ.get('b96866fa1f778899854a43cab55ba554')
    SECRET_KEY=os.environ.get('SECRET_KEY')


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
    pass

    DEBUG = True

config_options={
'development':DevConfig,
'production':ProdConfig
}
