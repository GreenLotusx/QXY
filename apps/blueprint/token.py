import uuid as uuid
from ..util.config import SHA256_SALT_HEAD,SHA256_SALT_FOOT,TOKEN_TIMEOUT
from ..util.common import hmac_sha256_single
from ..util.ext import redis


class Token(object):

    @property
    def token(self):
        token_str = SHA256_SALT_HEAD + str(uuid.uuid4()) + SHA256_SALT_FOOT
        return hmac_sha256_single(token_str)

    def set(self,sName,sToken,iTime=TOKEN_TIMEOUT):
        return redis.set("token_"+sName,sToken,iTime)

    def get(self,sName):
        return redis.get("token_"+sName)

token = Token()