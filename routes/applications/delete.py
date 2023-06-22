from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, Application

applications_delete_blueprint = Blueprint('applications_delete', __name__)

@applications_delete_blueprint.route("/applications/delete", methods=["POST"])
@jwt_required()
def delete_application():
    current_user = get_jwt_identity()
    if current_user["is_admin"]:
        id = request.json.get("id", None)
        if id:
            form_application = Application.query.filter_by(id=id).first()
            db.session.delete(form_application)
            db.session.commit()
            return jsonify({"msg": "Form application deleted."}), 200
        return jsonify({"msg": "Please enter ID."}), 401
    return jsonify({"msg": "You should be admin to delete."}), 401