from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, Input

inputs_delete_blueprint = Blueprint('inputs_delete_blueprint', __name__)

@inputs_delete_blueprint.route("/inputs/delete", methods=["POST"])
@jwt_required()
def delete_input():
    current_user = get_jwt_identity()
    if current_user["is_admin"]:
        id = request.json.get("id", None)
        if id:
            form_input = Input.query.filter_by(id=id).first()
            db.session.delete(form_input)
            db.session.commit()
            return jsonify({"msg": "Form input deleted."}), 200
        return jsonify({"msg": "Please enter ID."}), 401
    return jsonify({"msg": "You should be admin to delete."}), 401