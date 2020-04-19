from .bpObject import ViewObject
from flask import Blueprint,request

bp_login = Blueprint("login",__name__)

class login(ViewObject):

    # decorators = []

    def post(self):
        args = ("user", "password", "nick", "email")
        bCheck,sStatus = self._check_arg(args)
        if not bCheck:
            return self._format_retdata(sStatus)
        sName = request.form.get(args[0])
        sPwd = request.form.get(args[1])
        sNick = request.form.get(args[2])
        sEmail = request.form.get(args[3])

        return self._format_retdata("Success")

bp_login.add_url_rule("/login",endpoint="bp_login",view_func=login.as_view(name="login"))