from . import consts

DEBUG = True
HOST = "127.0.0.1"
PORG = "5000"
SECRET_KEY = "GreenLotusx"
SHA256_SALT_HEAD = "20200415"
SHA256_SALT_FOOT = "QXY_GREENLOTUSX"
SQLALCHEMY_DATABASE_URI = consts.DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
REDIS_DB_URL = consts.DB_REDIS_URI
REDIS_TIMEOUT = 15*60
TOKEN_TIMEOUT = 5*60
USERNAME_LENMAX = 12
USERNAME_LENMIN = 4
PASSWORD_LENMAX = 12
PASSWORD_LENMIN = 8
USERNICK_LENMAX = 12
USERNICK_LENMIN = 1