import logging
from .bpObject import ViewObject
from flask import Blueprint,request
from ..util.common import hmac_sha256_single
from ..util.ext import db,redis
from ..util.config import SHA256_SALT_HEAD,SHA256_SALT_FOOT
from ..models import User

class reg(ViewObject):

    # decorators = []

    def post(self):
        dFunc = [
            [self._check_arg,("username","password","nick","email")],
            [self._check_username,"username"],
            [self._check_password,"password"],
            [self._check_nick,"nick"],
            [self._check_email,"email"]
        ]
        bCheck,sStatus = self._check(dFunc)
        if not bCheck:
            return self._format_retdata(sStatus)

        sUser = request.form.get("username")
        user = User.query.filter_by(u_name=sUser).first()
        if user:
            return self._format_retdata("UserName_Exist")
        sPwd = request.form.get("password")
        sNick = request.form.get("nick")
        sEmail = request.form.get("email")
        sPwd = self.__pwd_format(sPwd)
        user = User(sUser,sPwd,sNick,sEmail)
        try:
            db.session.add(user)
            db.session.commit()
            redis.set("user_"+str(user.u_name),sPwd)
            data = {
                "id": user.u_id,
                "name":user.u_name,
                "nick":user.u_nickname,
                "timestamp":user.u_time
            }
            return self._format_retdata("Success",data)
        except Exception as ex:
            logging.error(ex)
            return self._format_retdata("UserReg_Error")

    def __pwd_format(self,sPwd):
        sPwd = SHA256_SALT_HEAD + sPwd + SHA256_SALT_FOOT
        salt = hmac_sha256_single(sPwd)
        return salt

bp_reg = Blueprint("reg",__name__)
bp_reg.add_url_rule("/userreg",endpoint="bp_reg",view_func=reg.as_view(name="reg"))