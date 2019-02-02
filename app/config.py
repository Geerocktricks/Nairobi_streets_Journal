class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    SOURCES_ARTICLE_API = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    HEADLINES_API  = "https://newsapi.org/v2/top-headlines?country=us&country=gb&country=au&apiKey={}"


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