HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_qxy'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

HOSTNAME_REDIS = '127.0.0.1'
PORT_REDIS = '6379'
DATABASE_REDIS = 0
PASSWORD_REDIS = ""
DB_REDIS_URI = {"host":HOSTNAME_REDIS,"port":PORT_REDIS,"password":PASSWORD_REDIS,"db":DATABASE_REDIS}

STATUS_CODE = {
    "Success"               :[0,"成功"],
    "Missing_Parameter"     :[-22,"传入参数缺失"],
    "Email_Error"           :[-104,"邮箱格式不正确"],
    "UserName_Lenght"       :[-101,"用户名长度不合法"],
    "UserName_Exist"        :[-105,"用户名已存在"],
    "PassWord_Lenght"       :[-102,"密码长度不合法"],
    "UserReg_Error"         :[-31,"未知异常"],
    "Login_Error"           :[-101,"用户名或密码不正确"],
    "Token_Error"           :[-31,"未知异常"]
}