import os

basedir = os.path.abspath(os.path.dirname(__file__))
mysql_host = "database"
mysql_database = os.environ.get("MYSQL_DATABASE")
mysql_user = os.environ.get("MYSQL_USER")
mysql_user_password = os.environ.get("MYSQL_PASSWORD")

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}".format(mysql_user, mysql_user_password, mysql_host, mysql_database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}".format(mysql_user, mysql_user_password, mysql_host, mysql_database)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:3306/{}".format(mysql_user, mysql_user_password, mysql_host, mysql_database)

config = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)