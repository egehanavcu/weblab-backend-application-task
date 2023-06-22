from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from models import Application

applications_get_blueprint = Blueprint('applications_get', __name__)

@applications_get_blueprint.route("/applications/get", methods=["POST"])
@jwt_required()
def get_applications():
    applications = Application.query.all()
    fetched_applications = []
    for application in applications:
        fetched_applications.append({
            "id": application.id,
            "email": application.email,
            "phone_number": application.phone_number,
            "form_data": application.form_data,
            "ip": application.ip,
            "timestamp": application.timestamp
        })
    return jsonify(fetched_applications), 200