from sqlalchemy.orm.exc import NoResultFound
from .token import token
from .bpObject import ViewObject
from flask import Blueprint,request

from ..models import User
from ..util.ext import redis,db

bp_login = Blueprint("login",__name__)

class Login(ViewObject):

    # decorators = []

    def post(self):
        dFunc = [
            [self._check_arg,("username","password")],
            [self._check_username,"username"],
            [self._check_password,"password"],
        ]
        bCheck,sStatus = self._check(dFunc)
        if not bCheck:
            return self._format_retdata(sStatus)
        sName = request.form.get("username")
        sPwd = request.form.get("password")
        user = redis.get("user_"+sName)
        if not user:
            try:
                userobj = User.query.filter_by(u_name="root").first()
                user = userobj._getall()
                redis.set("user_"+user.get("name"),user)
            except NoResultFound:
                return self._format_retdata("Login_Error")

        sUserPwd = user.get("pwd")
        sPwd = self._format_pwd(sPwd)
        if sUserPwd != sPwd:
            return self._format_retdata("Login_Error")
        else:
            sToken = token.token
            if not token.set(sName,sToken):
                return self._format_retdata("Token_Error")
            data = {
                "token":sToken,
                "file":eval(user.get("file")),
                "size":user.get("size"),
                "total":user.get("total"),
                "ident":user.get("ident"),
                "nick":user.get("nick"),
                "id":user.get("id")
            }
            return self._format_retdata("Success",data)

bp_login.add_url_rule("/login",endpoint="bp_login",view_func=Login.as_view(name="login"))