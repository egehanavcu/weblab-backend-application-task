import json

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, Application

applications_edit_blueprint = Blueprint('applications_edit', __name__)

@applications_edit_blueprint.route("/applications/edit", methods=["POST"])
@jwt_required()
def edit_application():
    current_user = get_jwt_identity()
    if current_user["is_admin"]:
        id = request.json.get("id", None)
        email = request.json.get("email", None)
        phone_number = request.json.get("phone_number", None)
        form_data = request.json.get("form_data", None)
        
        if id:
            form_application = Application.query.filter_by(id=id).first()
            if email:
                form_application.email = email
            
            if phone_number:
                form_application.phone_number = phone_number

            if form_data:
                if isinstance(form_data, dict):
                    form_application.form_data = json.dumps(form_data)
                else:
                    return jsonify({"msg": "Form data should be a dictionary."}), 401
                
            db.session.commit()
            return jsonify({"msg": "Form application updated."}), 200
        return jsonify({"msg": "Please enter ID."}), 401
    return jsonify({"msg": "You should be admin to edit."}), 401