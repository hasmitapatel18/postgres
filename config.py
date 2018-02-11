class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """
#set debug to true in development. Allows for exceptions to be raised should there be errors and allows for the reloading of the app once it has been updated. set to true in development (the default is set to false)
    DEBUG = True

#allows for the logging of errors when set to true
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """
#set debug to false in production
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
