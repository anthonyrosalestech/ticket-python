from decouple import config
config.encoding = 'cp1251'
# SECRET_KEY = config('SECRET_KEY')


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
