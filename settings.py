class Config(object):
    DEBUG = True

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    pass