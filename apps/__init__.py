import logging

from apps.blueprint import login,userreg
from apps.util.ext import db
from apps.util import config
from flask import Flask
from apps.models import User,File,Identity

app = Flask("__name__")
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(userreg.bp_reg)
app.register_blueprint(login.bp_login)

with app.app_context():
    db.create_all()

if not config.DEBUG:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='error.log')
