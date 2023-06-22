import os

from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from models import db

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config["JWT_SECRET_KEY"] = "ipHPCRtVcyztS4dMN56srvE5b4ap7z8o" # Change this to your own secret key
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

jwt = JWTManager(app)

PASSWORD_HASH = b'$2b$12$4uspPui3ONy6T25nnOc/4e' # Change this to your own hash