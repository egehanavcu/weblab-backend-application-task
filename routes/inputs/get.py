from flask import Blueprint, jsonify

from models import Input

inputs_get_blueprint = Blueprint('inputs_get', __name__)

@inputs_get_blueprint.route("/inputs/get", methods=["POST"])
def get_inputs():
    inputs = Input.query.all()
    fetched_inputs = []
    for input in inputs:
        fetched_inputs.append({
            "id": input.id,
            "name": input.name,
            "placeholder": input.placeholder,
        })
    return jsonify(fetched_inputs), 200