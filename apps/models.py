import time
from apps.util.ext import db

class User(db.Model):
    __tablename__ = "tab_user"
    u_id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    u_name = db.Column(db.String(20),unique=True,nullable=False)
    u_salt = db.Column(db.String(120),nullable=False)
    u_time = db.Column(db.BigInteger,nullable=False)
    u_nickname = db.Column(db.String(20),nullable=False)
    u_email = db.Column(db.String(32),unique=True,nullable=False)
    u_data = db.Column(db.String(120),nullable=False)
    u_size = db.Column(db.BigInteger,nullable=False)
    u_totalsize = db.Column(db.BigInteger,nullable=False)
    ui_identity = db.Column(db.Integer,nullable=False)

    def __init__(self,sName,sSalt,sNick,sEmail,dData=None,iSize=None,iTotal=None,iIdent=None):
        self.u_name = sName
        self.u_salt = sSalt
        self.u_time = int(time.time())
        self.u_nickname = sNick
        self.u_email = sEmail
        self.u_data = str(dData or {})
        self.u_size = iSize or 10*1024*1024
        self.u_totalsize = iTotal or 10*1024*1024
        self.ui_identity = iIdent or 2

    def __repr__(self):
        return '<User %r>' % self.u_name

class File(db.Model):
    __tablename__ = "tab_file"
    f_id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    f_type = db.Column(db.String(20),nullable=False)
    f_inittime = db.Column(db.BigInteger,nullable=False)
    f_inituse = db.Column(db.Integer,nullable=False)
    f_size = db.Column(db.Integer,nullable=False)
    f_count = db.Column(db.Integer,nullable=False)
    f_md5 = db.Column(db.String(120),nullable=False)
    f_path = db.Column(db.String(120),nullable=False)

    def __init__(self,sType,iInituser,iSize,iCount,sMd5,sPath):
        self.f_type = sType,
        self.f_inittime = int(time.time())
        self.f_inituse = iInituser
        self.f_size = iSize
        self.f_count = iCount
        self.f_md5 = sMd5
        self.f_path = sPath


class Identity(db.Model):
    __tablename__ = "tab_identity"
    i_id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    i_lv = db.Column(db.Integer,nullable=False)
    i_limitup = db.Column(db.Integer,nullable=False,default=0)
    i_limitdown = db.Column(db.Integer,nullable=False,default=0)
    i_view = db.Column(db.String(120),nullable=False)

    def __init__(self,iLv,iLimitup,iLimitdown,sView):
        self.i_lv = iLv
        self.i_limitup = iLimitup
        self.i_limitdown = iLimitdown
        self.i_view = sView