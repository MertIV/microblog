#__init__ dosyaları bulunduğu klasörü bir package haline getiriliyor ve projede import edilebiliyor

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app import routes, models
