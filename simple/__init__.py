from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)
db=SQLAlchemy(app)
login_manager=LoginManager(app)

login_manager.init_app(app)

from . import views


