#__init__ dosyaları bulunduğu klasörü bir package haline getiriliyor ve projede import edilebiliyor

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy #db operations
from flask_migrate import Migrate #to easily migrate db
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
