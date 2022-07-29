from flask import Blueprint, jsonify


developers = Blueprint('developers', __name__, url_prefix="/developer")


@developers.route('/', methods=["GET"])
def list_all_developers():
    return jsonify({"data": ["alguém", "outrão", "fulâano"]})


@developers.route('/', methods=["POST"])
def list_new_developers():
    return {"data": ["alguém", "outrão", "fulâano"]}