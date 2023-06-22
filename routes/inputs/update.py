from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from models import db, Input

inputs_update_blueprint = Blueprint('inputs_update_blueprint', __name__)

@inputs_update_blueprint.route("/inputs/update", methods=["POST"])
@jwt_required()
def update_input():
    id = request.json.get("id", None)
    name = request.json.get("name", None)
    placeholder = request.json.get("placeholder", None)
    if id:
        form_input = Input.query.filter_by(id=id).first()
        if name:
            form_input.name = name

        if placeholder:
            form_input.placeholder = placeholder

        db.session.commit()
        return jsonify({"msg": "Form input updated."}), 200
    return jsonify({"msg": "Please enter ID, name and placeholder."}), 401