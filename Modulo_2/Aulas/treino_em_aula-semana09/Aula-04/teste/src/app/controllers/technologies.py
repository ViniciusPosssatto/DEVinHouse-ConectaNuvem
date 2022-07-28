from flask import Blueprint, request


technology = Blueprint('technology', __name__, url_prefix="/technology")


@technology.route('/', methods=["GET"])
def list_all_technologies():
    return {"data": ["Java", "JavaScript", "Python"]}


@technology.route('/', methods=["POST"])
def list_new_technologies():
    data = request.get_json()
    print(data)
    return {"data": ["Ruby", "flask", "css"]}