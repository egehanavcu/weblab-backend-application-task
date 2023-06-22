from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from models import User, hash_password
from settings import PASSWORD_HASH

auth_login_blueprint = Blueprint('auth_login', __name__)

@auth_login_blueprint.route("/auth/login", methods=["POST"])
def login_panel():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username and password:
        hashed_password = hash_password(password, PASSWORD_HASH)
        user = User.query.filter_by(username=username, password=hashed_password).first()
        if user:
            access_token = create_access_token(identity={"username": username, "is_admin": user.is_admin})
            return jsonify(access_token=access_token), 200
        return jsonify({"msg": "Bad username or password"}), 401
    return jsonify({"msg": "Please enter username and password."}), 401