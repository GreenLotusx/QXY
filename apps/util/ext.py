import redis
from flask_sqlalchemy import SQLAlchemy
from .config import REDIS_DB_URL,REDIS_TIMEOUT

class Redis(object):
    conn = None

    def __init__(self):
        self.conn = redis.Redis(**REDIS_DB_URL)

    def get(self,key):
        data = self.conn.get(key)
        return data

    def set(self,key,val,time=None):
        data = val
        self.conn.set(
            name=key,
            value=data,
            ex=time or REDIS_TIMEOUT
        )

db = SQLAlchemy()
redis = Redis()