from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from models import db, Input

inputs_add_blueprint = Blueprint('inputs_add_blueprint', __name__)

@inputs_add_blueprint.route("/inputs/add", methods=["POST"])
@jwt_required()
def add_input():
    name = request.json.get("name", None)
    placeholder = request.json.get("placeholder", None)
    if name and placeholder:
        form_input = Input(name=name, placeholder=placeholder)
        db.session.add(form_input)
        db.session.commit()
        return jsonify({"msg": "Form input added."}), 200
    return jsonify({"msg": "Please enter name and placeholder."}), 401