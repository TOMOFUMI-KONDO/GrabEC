class BaseConfig(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'mysql',
        'password': 'mysql',
        'host': 'localhost',
        'db_name': 'grabec'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
