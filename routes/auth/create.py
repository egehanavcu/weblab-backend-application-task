import sqlalchemy

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, User, hash_password
from settings import PASSWORD_HASH

auth_create_blueprint = Blueprint('auth_create', __name__)

@auth_create_blueprint.route("/auth/create", methods=["POST"])
@jwt_required()
def create_panel_account():
    current_user = get_jwt_identity()
    if current_user["is_admin"]:
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        is_admin = request.json.get("is_admin", None)
        if username and password:
            try:
                hashed_password = hash_password(password, PASSWORD_HASH)
                user = User(username=username, password=hashed_password, is_admin=is_admin)
                db.session.add(user)
                db.session.commit()
                return jsonify({"msg": "User created."}), 200
            except sqlalchemy.exc.IntegrityError:
                return jsonify({"msg": "Account exists."}), 401
        return jsonify({"msg": "Please enter username and password."}), 401
    return jsonify({"msg": "You should be admin to create user."}), 401