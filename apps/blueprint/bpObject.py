import re
from flask import views,request,jsonify
from ..util.consts import STATUS_CODE
from ..util.common import check_num_maxmin
from ..util.config import USERNAME_LENMAX,USERNAME_LENMIN,USERNICK_LENMAX,\
    USERNICK_LENMIN,PASSWORD_LENMAX,PASSWORD_LENMIN

class ViewObject(views.MethodView):

    def _check(self,lFunc):
        for item in lFunc:
            func,args = item[0],item[1]
            if isinstance(args,str):
                args = request.form.get(args)
            bCheck,sStatus = func(args)
            if not bCheck:
                return bCheck,sStatus
        return True,"Success"

    def _check_arg(self,argslist):
        for arg in argslist:
            if not request.values.get(arg):
                return False,"Missing_Parameter"
        return True,None

    def _check_email(self,sEmail):
        str = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        bCheck = re.match(str, sEmail)
        if not bCheck:
            return False,"Email_Error"
        return True,None

    def _check_username(self,sUser):
        bCheck = check_num_maxmin(len(sUser),USERNAME_LENMAX,USERNAME_LENMIN)
        if not bCheck:
            return False,"UserName_Lenght"

        return True,None

    def _check_password(self,sPassword):
        bCheck = check_num_maxmin(len(sPassword), PASSWORD_LENMAX, PASSWORD_LENMIN)
        if not bCheck:
            return False,"PassWord_Lenght"
        return True,None

    def _check_nick(self,sNick):
        bCheck = check_num_maxmin(len(sNick), USERNICK_LENMAX, USERNICK_LENMIN)
        if not bCheck:
            return False,"PassWord_Lenght"
        return True,None

    def _format_retdata(self,sStatus,dData=None):
        info = STATUS_CODE[sStatus]
        data = {
            "status":info[0],
            "msg":info[1],
            "data":dData
        }
        if dData is None:
            del data["data"]
        return jsonify(data)