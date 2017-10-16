class Config:
    '''
    General configurations
    '''
    # MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'


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
