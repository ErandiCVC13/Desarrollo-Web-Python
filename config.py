class Config:
    SECRET_KEY = "99minutos"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='99minutos', server='localhost', database='project_web')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='99minutos', server='localhost', database='project_web_test')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
    "development": DevelopmentConfig,
    "default": DevelopmentConfig,
    "test": TestConfig
}