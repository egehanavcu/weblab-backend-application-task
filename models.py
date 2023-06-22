import bcrypt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

def hash_password(plain_password, PASSWORD_HASH):
    return bcrypt.hashpw(plain_password.encode("utf-8"), PASSWORD_HASH)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Input(db.Model):
    __tablename__ = "inputs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    placeholder = db.Column(db.Text, nullable=False)
    
class Application(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    phone_number = db.Column(db.Text, unique=True, nullable=False)
    form_data = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Text, unique=True, nullable=False)
    timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())