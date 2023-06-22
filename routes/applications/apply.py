import json
import sqlalchemy

from flask import Blueprint, request, jsonify

from models import db, Application

applications_apply_blueprint = Blueprint('applications_apply', __name__)

@applications_apply_blueprint.route("/applications/apply", methods=["POST"])
def form_apply():
    email = request.json.get("email", None)
    phone_number = request.json.get("phone_number", None)
    form_data = request.json.get("form_data", None)
    
    if isinstance(form_data, dict):
        stringified_form_data = json.dumps(form_data)
    else:
        return jsonify({"msg": "Form data should be a dictionary."}), 401
    
    if email and phone_number and form_data:
        try:
            form_application = Application(email=email, phone_number=phone_number, form_data=stringified_form_data, ip=request.remote_addr)
            db.session.add(form_application)
            db.session.commit()
            return jsonify({"msg": "Form application submitted."}), 200
        except sqlalchemy.exc.IntegrityError:
            return jsonify({"msg": "You have already submitted."}), 401
    return jsonify({"msg": "Please enter email, phone_number and form_data."}), 401