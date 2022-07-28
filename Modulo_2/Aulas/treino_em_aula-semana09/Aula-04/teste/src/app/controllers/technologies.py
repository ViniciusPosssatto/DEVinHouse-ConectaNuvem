from flask import Blueprint, request
from src.app.db import read, save
from src.app.utils import exist_key


technology = Blueprint('technology', __name__, url_prefix="/technology")


@technology.route('/', methods=["GET"])
def list_all_technologies():
    return {"data": ["Java", "JavaScript", "Python"]}


@technology.route('/', methods=["POST"])
def list_new_technologies():
    list_keys = ["id", "tech"]

    data = exist_key(request.get_json(), list_keys)

    print(data)
    return data

    