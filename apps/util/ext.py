import redis
from flask_sqlalchemy import SQLAlchemy
from .config import REDIS_DB_URL,REDIS_TIMEOUT

class Redis(object):
    conn = None

    def __init__(self):
        self.conn = redis.Redis(**REDIS_DB_URL)

    def get(self,key):
        data = self.conn.get(key)
        if data:
            data = str(data, encoding="utf-8")
            return eval(data)
        return None

    def set(self,key,val,time=None):
        bData = str(val).encode("utf-8")
        sData = str(bData, encoding="utf-8")
        try:
            self.conn.set(
                name=key,
                value=sData,
                ex=time or REDIS_TIMEOUT
            )
            return True
        except:
            return False

db = SQLAlchemy()
redis = Redis()